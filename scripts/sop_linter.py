import argparse
import os
import re
import json
from typing import List, Dict, Any
from packaging.version import Version, InvalidVersion
import markdown
from bs4 import BeautifulSoup
from utils import find_tables, collect_sop_files, parse_glossary, is_remote_reference_resolvable, get_image_paths

class SOPLinter:
    def __init__(self, verbosity: int = 0, strict: bool = False, required_sections: dict = {}):
        """
        Initializes the SOPLinter with verbosity and strict mode settings.

        :param verbosity: Level of verbosity for output messages.
        :param strict: Whether to treat warnings as errors.
        """
        self.verbosity = verbosity
        self.strict = strict
        self.results = {}
        self.tables = {}
        self.required_sections = required_sections

    def lint_sop(self, file_path: str, all_inputs: List[str] = []):
        """
        Lints a single SOP file for compliance with the required rules.

        :param file_path: Path to the SOP file.
        :param all_inputs: List of all input filepaths to compare with.
        """
        if self.verbosity > 1:
            print(f"- Starting linting for {file_path}")

        self.results[file_path] = {"errors": [], "warnings": []}
        self.tables[file_path] = None
        with open(file_path, 'r') as file:
            content = file.read()

        html_content = markdown.markdown(content, extensions=['tables'])
        soup = BeautifulSoup(html_content, 'html.parser')

        # We iterate one by one over the linting rules
        self.lr_check_title(soup, file_path)
        self.lr_check_required_sections(soup, file_path)
        self.lr_check_non_empty_sections(soup, file_path)
        self.lr_check_metadata_table(soup, file_path)
        self.lr_check_document_history(soup, file_path)
        self.lr_check_roles_and_responsibilities(soup, file_path)
        self.lr_check_procedure_step_numbering(soup, file_path)
        self.lr_check_step_consistency(soup, file_path)
        self.lr_check_glossary_in_charter(soup, file_path)
        self.lr_check_undefined_acronyms(soup, file_path)
        self.lr_check_resolvable_references(soup, file_path)
        self.lr_check_identifier_and_casing(file_path, all_inputs)
        self.lr_check_title_match(soup, file_path)
        self.lr_check_image_paths(soup, file_path)

        if self.verbosity > 1:
            print(f"- Finished linting for {file_path}")
            print(json.dumps(self.results[file_path], indent=2),"\n")

    def lr_check_title(self, soup: BeautifulSoup, file_path: str):
        """
        Checks if the SOP title follows the required format.

        :param soup: BeautifulSoup object of the parsed SOP content.
        :param file_path: Path to the SOP file.
        """
        if self.verbosity > 1:
            print("-- Linting rule: checking title...")

        first_header = soup.find('h1')
        if not first_header or not first_header.text.startswith("European GDI - "):
            self.report_issue(f"Title must start with '# European GDI - ' followed by the SOP title. Current title: '{first_header.text}'", file_path, error=True)

        if self.verbosity > 1:
            print(f"{json.dumps(self.results[file_path], indent=2)}\n")

    def lr_check_metadata_table(self, soup: BeautifulSoup, file_path: str):
        """
        Checks if the metadata table is correctly formatted and contains proper content.

        :param soup: BeautifulSoup object of the parsed SOP content.
        :param file_path: Path to the SOP file.
        """
        if self.verbosity > 1:
            print("-- Linting rule: checking metadata table...")

        metadata_table_headers = ["Metadata", "Value"]
        table_find_result = self.find_tables(soup = soup, file_path = file_path, aim_headers = metadata_table_headers)

        if not table_find_result:
            self.report_issue("Metadata table is missing or incorrectly formatted.", file_path, error=True)
            return
        
        metadata_table = table_find_result[0]
        rows = metadata_table.find_all('tr') # Table rows (tr)
        # Expected format of the "Value" column of each row
        expected_metadata = {
            "template sop number": r"GDI-SOP\d{4}", # e.g.: GDI-SOP0001
            "template sop version": self.is_valid_version, # e.g.: v1,
            "topic": ["Data protection & security", "Data & metadata management", "Technical infrastructure & software development", "Helpdesk & operations"],
            "template sop type": ["Node-specific SOP", "European-level SOP"],
            "gdi node": r"^[A-Z]{3}$", # e.g.: SWE (for Sweden)
            "instance version": self.is_valid_version, # e.g.: v1
        }

        table_dict = {}

        # Iterate over each table row, applying its validation rule
        for row in rows[1:]:  # Skip the header row
            columns = [col.text.strip() for col in row.find_all('td')]
            if not len(columns) == 2:
                self.report_issue(f"Metadata table row is incorrectly formatted (2 columns are expected): '{' | '.join(columns)}'.", file_path, error=True)
                continue
            key, value = columns[0], columns[1]
            table_dict[key.lower()] = value

        for key, value in table_dict.items():
            # Linting rules for node-specific SOPs should not apply for european-level ones
            node_specific_keys = ["gdi node", "instance version"]
            if key in node_specific_keys:
                try:
                    if table_dict["template sop type"].lower() == "European-level SOP".lower():
                        continue
                except:
                    pass

                # We only want to evaluate each key Node-specific key format if any is present.
                #   Otherwise, it could be a Node-specific SOP template (correct without these keys)
                if all(table_dict.get(key) in [None, "", []] for key in node_specific_keys):
                    self.report_issue(f"At the metadata table, value column for '{key}' was empty. If the SOP is a Node-specific SOP Instance (not a template), it should have a value.", file_path, warning=True)
                    continue

            if key in expected_metadata:
                # Depending on the type of format rules for each row, we apply them differently
                if isinstance(expected_metadata[key], str) and not re.match(expected_metadata[key], value):
                    # e.g., GDI-SOP0001
                    self.report_issue(f"At the metadata table, value column for '{key}' is incorrectly formatted: '{value}'. It should follow the regex '{expected_metadata[key]}'", file_path, error=True)
                elif callable(expected_metadata[key]) and not expected_metadata[key](value):
                    # e.g., v1.0.2
                    self.report_issue(f"At the metadata table, value column for '{key}' is incorrectly formatted: '{value}'.", file_path, error=True)
                elif isinstance(expected_metadata[key], list) and value.lower() not in [item.lower() for item in expected_metadata[key]]:
                    # e.g., Node-specific SOP
                    self.report_issue(f"At the metadata table, value column for '{key}' is invalid: '{value}'. It's value should be one of: {expected_metadata[key]}", file_path, error=True)
            else:
                self.report_issue(f"Unexpected row in the metadata table: '{' | '.join([key, value])}'.", file_path, warning=True)

        for key in expected_metadata.keys():
            if key.lower() not in table_dict.keys():
                self.report_issue(f"Metadata row '{key}' is missing from the metadata table.", file_path, error=True)

        try:
            if table_dict["template sop type"] == "European-level SOP" and (table_dict["gdi node"] or table_dict["instance version"]):
                self.report_issue("European-level SOPs should not have 'GDI Node' or 'Instance version' values in the metadata table.", file_path, error=True)
        except Exception:
            # The missing rows are already reported above
            pass
        
        try:
            sop_type = table_dict["template sop type"].lower()
            expected_folder = sop_type.split(" ", 1)[0]  # "european-level" or "node-specific"
            parent_directory = os.path.basename(os.path.dirname(file_path)).lower()
            
            # Check if the immediate parent directory matches the expected folder name
            if parent_directory != expected_folder:
                self.report_issue(
                    f"SOP type '{table_dict['template sop type']}' should be in the '{expected_folder}' folder, but the file path shows it's in '{parent_directory}'.",
                    file_path,
                    error=True
                )
        except KeyError:
            # SOP type errors (e.g., missing type) should be reported by metadata checks
            pass

        if self.verbosity > 1:
            print(f"{json.dumps(self.results[file_path], indent=2)}\n")

    def lr_check_required_sections(self, soup: BeautifulSoup, file_path: str):
        """
        Checks if all required sections are present in the SOP.

        :param soup: BeautifulSoup object of the parsed SOP content.
        :param file_path: Path to the SOP file.
        """
        if self.verbosity > 1:
            print("-- Linting rule: checking required sections...")       

        for section, selector in self.required_sections.items():
            if not soup.select_one(selector):
                self.report_issue(f"Required section '{section}' is missing.", file_path, error=True)

        if self.verbosity > 1:
            print(f"{json.dumps(self.results[file_path], indent=2)}\n")

    def lr_check_document_history(self, soup: BeautifulSoup, file_path: str):
        """
        Checks the 'Document History' table for proper version increments, non-empty change descriptions, 
        valid author names, and valid date formats.

        :param soup: BeautifulSoup object of the parsed SOP content.
        :param file_path: Path to the SOP file.
        """
        if self.verbosity > 1:
            print("-- Linting rule: checking Document History table...")

        aim_headers = ["Template Version", "Instance version", "Author(s)", "Description of changes", "Date"]
        table_find_result = self.find_tables(soup, file_path, aim_headers)

        if not table_find_result:
            self.report_issue("Document History table is missing or incorrectly formatted.", file_path, error=True)
            return
        
        document_history_table = table_find_result[0]        
        rows = document_history_table.find_all('tr')[1:]  # Skip the header row
        previous_template_version = None
        previous_instance_version = None

        for row in rows:
            columns = [col.text.strip('`').strip() for col in row.find_all('td')]

            if len(columns) != 5:
                self.report_issue(f"Document History table row is incorrectly formatted (expected 5 columns). Row: '{' | '.join(columns)}'.", file_path, error=True)
                continue

            template_version = columns[0]
            instance_version = columns[1]
            author = columns[2]
            description = columns[3]
            date = columns[4]

            # Check versioning rules
            if self.is_valid_version(template_version):
                current_template_version = Version(template_version)
            else:
                self.report_issue(f"At the Document History table, Template Version ('{template_version}') is incorrectly formatted. Row: '{' | '.join(columns)}'.", file_path, error=True)
                continue

            if instance_version:
                if self.is_valid_version(instance_version):
                    current_instance_version = Version(instance_version)                    
                else:
                    self.report_issue(f"At the Document History table, Instance Version ('{instance_version}') is incorrectly formatted. Row: '{' | '.join(columns)}'.", file_path, error=True)
                    continue
            else:
                current_instance_version = None

            if previous_template_version:
                # Template versions should be equal or lower than the ones above (more recent)
                if (current_template_version > previous_template_version) or (current_template_version == previous_template_version and not previous_instance_version):
                    self.report_issue(f"At the Document History table, Template version ('{current_template_version}') should be lower than the version right above ('{previous_template_version}'). Notice the order of the table: from recent (top) to older (bottom) and address the versioning. Row: '{' | '.join(columns)}'.", file_path, error=True)

                # Instance versions are not always required, only when it's a node instance
                if current_instance_version and previous_instance_version:
                    # Instance versions should always be higher than the previous one
                    if current_instance_version >= previous_instance_version:
                        self.report_issue(f"At the Document History table, Instance Version ('{current_instance_version}') should be lower than the version right above ('{previous_instance_version}'). Notice the order of the table: from recent (top) to older (bottom) and address the versioning. Row: '{' | '.join(columns)}'.", file_path, error=True)

            # Assigned for the next iteration to use for comparisons
            previous_template_version = current_template_version
            previous_instance_version = current_instance_version

            # Check author name
            if not author:
                self.report_issue(f"Author name is missing. Row: '{' | '.join(columns)}'.", file_path, error=True)

            # Check description
            if not description:
                self.report_issue(f"Description of changes is missing. Row: '{' | '.join(columns)}'.", file_path, error=True)

            # Check date format
            if not re.match(r"\d{4}\.\d{2}\.\d{2}", date):
                self.report_issue(f"Date is incorrectly formatted (expected format is YYYY.MM.DD): '{date}'. Row: '{' | '.join(columns)}'.", file_path, error=True)

        if self.verbosity > 1:
            print(f"{json.dumps(self.results[file_path], indent=2)}\n")

    def lr_check_roles_and_responsibilities(self, soup: BeautifulSoup, file_path: str):
        """
        Checks if the Roles and Responsibilities table exists and has at least one non-empty Full Name for roles Author, Reviewer, and Approver.

        :param soup: BeautifulSoup object of the parsed SOP content.
        :param file_path: Path to the SOP file.
        """
        if self.verbosity > 1:
            print("-- Linting rule: checking Roles and Responsibilities table...")

        aim_headers = ["Role", "Full name", "GDI/node role", "Organisation"]
        table_find_result = self.find_tables(soup, file_path, aim_headers)

        if not table_find_result:
            self.report_issue("Roles and Responsibilities table is missing or incorrectly formatted.", file_path, error=True)
            return
        
        roles_table = table_find_result[0]
        required_roles = ["Author", "Reviewer", "Approver"]
        found_roles = {role: False for role in required_roles}

        rows = roles_table.find_all('tr')[1:]  # Skip the header row
        for row in rows:
            columns = [col.text.strip() for col in row.find_all('td')]
            if len(columns) != 4:
                self.report_issue(f"Roles and Responsibilities table row is incorrectly formatted (expected 4 columns): '{' | '.join(columns)}'.", file_path, error=True)
                continue

            role, full_name = columns[0], columns[1]

            # If we haven't already found one, and this one is required and has a full name value
            if role in required_roles and full_name:
                if not found_roles[role]:
                    found_roles[role] = True

        for role, found in found_roles.items():
            if not found:
                self.report_issue(f"Role '{role}' is missing a non-empty Full Name row in the Roles and Responsibilities table.", file_path, error=True)

        if self.verbosity > 1:
            print(f"{json.dumps(self.results[file_path], indent=2)}\n")

    def lr_check_non_empty_sections(self, soup: BeautifulSoup, file_path: str):
        """
        Checks if required sections are non-empty.
        
        :param soup: BeautifulSoup object of the parsed SOP content.
        :param file_path: Path to the SOP file.
        """
        if self.verbosity > 1:
            print("-- Linting rule: checking non-empty required sections...")

        for section_title, selector in self.required_sections.items():
            header = soup.select_one(selector)
            if not header:
                # No need to report the missing section as an error, since 
                #   that's the role of a different linting rule
                continue

            # Get all siblings of the header until the next header of the same or higher level
            section_content = []
            for sibling in header.find_next_siblings(): # Create iterator of headers
                # Only capture content within the current section and stop if we reach a new section of the same or higher level
                if re.match(r'^h[1-6]$', sibling.name) and sibling.name <= header.name:
                    break
                section_content.append(sibling)

            if not section_content or all(not sibling.text.strip() for sibling in section_content):
                self.report_issue(f"The section '{section_title}' is empty.", file_path, error=True)

        if self.verbosity > 1:
            print(f"{json.dumps(self.results[file_path], indent=2)}\n")

    def lr_check_procedure_step_numbering(self, soup: BeautifulSoup, file_path: str):
        """
        Checks that the headers under "### 8. Procedure" section are sequentially numbered 
        as "#### 8.1", "#### 8.2", etc., without skipping any numbers and ensure they start with "8.".
        
        :param soup: BeautifulSoup object of the parsed SOP content.
        :param file_path: Path to the SOP file.
        """
        if self.verbosity > 1:
            print("-- Linting rule: checking header numbering in Procedure section...")

        # Locate the "### 8. Procedure" header
        procedure_header = soup.find('h3', string=re.compile(r"^8\.\s*Procedure", re.IGNORECASE))
        if not procedure_header:
            self.report_issue("Missing '### 8. Procedure' section header.", file_path, error=True)
            return

        # Initialize the expected step number
        current_step_number = 1

        # Iterate through all h4 headers within the Procedure section
        for header in procedure_header.find_all_next('h4'):
            # Stop if we reach a new section at the same or higher level than the Procedure header
            if re.match(r'^h[1-3]$', header.name) and header.name <= procedure_header.name:
                break

            # Check if the header starts with "8." followed by the expected step number
            match = re.match(r'^8\.(\d+)', header.text.strip())
            if not match:
                # If the header doesn't start with "8.", report it as an error
                self.report_issue(
                    f"Header formatting error in '8. Procedure' section. Expected '#### 8.{current_step_number} ...' or similar correct numbering, but found '#### {header.text.strip()}'.",
                    file_path,
                    error=True
                )
            else:
                step_number = int(match.group(1))
                if step_number != current_step_number:
                    self.report_issue(
                        f"Step numbering error in '8. Procedure' section. Expected '#### 8.{current_step_number}' or similar correct numbering, but found '#### {header.text.strip()}'.",
                        file_path,
                        error=True
                    )
                    # Update to the actual step number to attempt to continue checking from this point
                    current_step_number = step_number

                # Increment the expected step number for the next header
                current_step_number += 1

        if self.verbosity > 1:
            print(f"{json.dumps(self.results[file_path], indent=2)}\n")

    def lr_check_step_consistency(self, soup: BeautifulSoup, file_path: str):
        """
        Checks that each header in the "### 8. Procedure" section has a matching "Step identifier"
        in the following table, consistent with the step number in the header, allowing for complex 
        identifiers (e.g., 8.1, 8.2.1, 8.2.1.1) and capturing any header level.
        
        :param soup: BeautifulSoup object of the parsed SOP content.
        :param file_path: Path to the SOP file.
        """
        if self.verbosity > 1:
            print("-- Linting rule: checking step consistency in Procedure section...")

        # Locate the "### 8. Procedure" header
        procedure_header = soup.find('h3', string=re.compile(r"^8\.\s*Procedure$", re.IGNORECASE))
        if not procedure_header:
            self.report_issue("Missing '### 8. Procedure' section header.", file_path, error=True)
            return

        # Iterate through all headers within the Procedure section that start with "8."
        for header in procedure_header.find_all_next(string=re.compile(r"^8\.(?!Procedure\b)")):
            # Stop if we reach a new section at the same or higher level than the Procedure header
            if header.name and re.match(r'^h[1-3]$', header.name) and header.name <= procedure_header.name:
                break
            
            if header == '8. Procedure':
                continue

            # Extract only the numeric part of the step identifier from header text
            step_match = re.match(r'^(8(?:\.\d+)+)', header.strip())
            if not step_match:
                # Report if a header in the Procedure section doesn't start with the expected format
                self.report_issue(
                    f"Header formatting error in Procedure section. Expected a header starting with '8.' but found '{header.strip()}'.",
                    file_path,
                    error=True
                )
                continue

            # Capture the stripped numeric identifier for comparison with "Step identifier"
            step_identifier = step_match.group(1).lstrip("8.")

            # Locate the next table after the header to check the "Step identifier" field
            next_table = header.find_next('table')
            if not next_table:
                self.report_issue(
                    f"No table found immediately after step header '{header.strip()}'. Each step must have an associated table.",
                    file_path,
                    error=True
                )
                continue

            # Find the "Step identifier" (first column) cell in the first row of the table
            step_identifier_cell = next_table.find('td')
            if not step_identifier_cell:
                self.report_issue(
                    f"Table immediately following '{header.strip()}' does not contain a 'Step identifier' entry.",
                    file_path,
                    error=True
                )
                continue

            # Compare the numeric part of the header identifier with the table's Step identifier
            table_step_identifier = step_identifier_cell.text.strip()
            if table_step_identifier != step_identifier:
                self.report_issue(
                    f"Step identifier mismatch for '{header.strip()}'. Expected 'Step identifier' '{step_identifier}', but found '{table_step_identifier}' in the table.",
                    file_path,
                    error=True
                )

        if self.verbosity > 1:
            print(f"{json.dumps(self.results[file_path], indent=2)}\n")
    
    def lr_check_glossary_in_charter(self, sop_soup: BeautifulSoup, file_path: str):
        """
        Checks that all abbreviations and terms in the SOP's glossary are also present in the Charter glossary.

        :param sop_soup: BeautifulSoup object of the SOP content.
        :param file_path: Path to the SOP file.
        """
        if self.verbosity > 1:
            print("-- Linting rule: checking SOP glossary terms against Charter glossary...")

        # Get the Charter soup, parsing if it hasn't been done already
        charter_soup = self.get_charter_soup(file_path)

        # Parse glossaries from SOP and Charter
        sop_glossary = parse_glossary(sop_soup)
        charter_glossary = parse_glossary(charter_soup)

        # Check if all items in the SOP glossary are also in the Charter glossary
        for term in sop_glossary.keys():
            if term not in charter_glossary:
                self.report_issue(
                    f"Glossary mismatch: '{term}' in SOP glossary is not found in Charter glossary. Make sure that the Charter is updated accordingly with new acronyms from this SOP.",
                    file_path,
                    error=True
                )

        if self.verbosity > 1:
            print(f"{json.dumps(self.results[file_path], indent=2)}\n")

    def lr_check_undefined_acronyms(self, sop_soup: BeautifulSoup, file_path: str):
        """
        Detects any acronyms in the SOP content that are not defined in the SOP glossary.

        :param sop_soup: BeautifulSoup object of the SOP content.
        :param file_path: Path to the SOP file.
        """
        if self.verbosity > 1:
            print("-- Linting rule: checking for undefined acronyms in SOP...")

        # Parse glossary from SOP
        sop_glossary = parse_glossary(sop_soup)

        # Identify any acronyms in SOP content
        sop_text = sop_soup.get_text()
        # Regex for uppercase acronyms of 2+ characters, with possible "s" ending (e.g., SOPs)
        detected_acronyms = re.findall(r'\b[A-Z]{2,}s?\b', sop_text)
        for acronym in set(detected_acronyms):
            if acronym not in sop_glossary:
                if acronym[-1] == 's' and acronym[:-1] in sop_glossary:
                    # We skip acronym plurals (e.g., SOPs) that would be false positives (e.g., since SOP is already there)
                    continue
                self.report_issue(
                    f"Undefined acronym detected: '{acronym}' is used in the SOP but is not defined in the SOP glossary.",
                    file_path,
                    warning=True
                )

        if self.verbosity > 1:
            print(f"{json.dumps(self.results[file_path], indent=2)}\n")

    def lr_check_resolvable_references(self, soup: BeautifulSoup, file_path: str):
        """
        Checks if GitHub references in the SOP content are resolvable.
        Relative paths are checked against the file system, and remote GitHub links are checked via HTTP.

        :param soup: BeautifulSoup object of the SOP content.
        :param file_path: Path to the SOP file.
        """
        if self.verbosity > 1:
            print("-- Linting rule: checking resolvable GitHub references...")

        # Find all <a> tags with href attributes in the HTML content
        links = soup.find_all('a', href=True)

        # Check each link to classify and verify its resolvability
        for link in links:
            href = link['href']
            
            # Relative path check (starts with ./ or ../)
            if href.startswith('./') or href.startswith('../'):
                path_only = href.split('#')[0]
                absolute_path = os.path.abspath(os.path.join(os.path.dirname(file_path), path_only))
                if not os.path.exists(absolute_path):
                    self.report_issue(
                        f"Unresolvable relative reference: '{href}' cannot be resolved (i.e., the target file does not exist).",
                        file_path,
                        error=True
                    )
            
            # Remote GitHub link check (starts with https://github.com/)
            elif href.startswith('https://github.com/'):
                if not is_remote_reference_resolvable(href):
                    self.report_issue(
                        f"Unresolvable GitHub reference: '{href}' returns a 404 (not found).",
                        file_path,
                        error=True
                    )

        if self.verbosity > 1:
            print(f"{json.dumps(self.results[file_path], indent=2)}\n")

    def lr_check_identifier_and_casing(self, file_path: str, all_files: List[str]):
        """
        Checks if the SOP filename has a unique SOP identifier, and follows proper casing rules:
        Identifier is uppercase, followed by an underscore-separated, lowercase title.

        :param file_path: Path to the current SOP file.
        :param all_files: List of all SOP file paths for uniqueness checks.
        """
        filename = os.path.basename(file_path)
        filename_without_extension = os.path.splitext(filename)[0]

        # Enforce filename structure with uppercase identifier and lowercase title
        sop_identifier_match = re.match(r"^(GDI-SOP\d{4})_(.+)$", filename_without_extension)
        if sop_identifier_match:
            identifier = sop_identifier_match.group(1)
            title_part = sop_identifier_match.group(2)
            
            # Validate title format
            if title_part != title_part.lower():
                self.report_issue(
                    f"Filename '{filename}' must be in lowercase after the identifier. See further details at 'docs/GDI-SOP_sop-accessioning.md'.",
                    file_path,
                    error=True
                )

            # Check for unique identifier
            if sum(1 for f in all_files if identifier in f) > 1:
                self.report_issue(
                    f"Duplicate SOP identifier found among the SOPs filenames: '{identifier}'.",
                    file_path,
                    error=True
                )
        else:
            self.report_issue(
                "Filename must follow the format 'GDI-SOPXXXX_lowercase-title.md'. See further details at 'docs/GDI-SOP_sop-accessioning.md'.", 
                file_path, 
                error=True
            )

        if self.verbosity > 1:
            print(f"{json.dumps(self.results[file_path], indent=2)}\n")

    def lr_check_title_match(self, soup: BeautifulSoup, file_path: str):
        """
        Checks if the title in the SOP document matches the title implied by the filename,
        ensuring it starts with "European GDI - ".

        :param soup: BeautifulSoup object of the SOP content.
        :param file_path: Path to the SOP file.
        """
        filename = os.path.basename(file_path)
        filename_without_extension = os.path.splitext(filename)[0]

        # Extract the human-readable title part from the filename after the identifier
        title_from_filename = filename_without_extension.split("_", 1)[1].replace("-", " ").capitalize()
        expected_document_title = f"European GDI - {title_from_filename}"
        
        # Find the first h1 header and check if it matches the expected format
        title_header = soup.find('h1')
        if title_header:
            document_title = title_header.text.strip()
            if document_title.lower() != expected_document_title.lower():
                self.report_issue(
                    f"Document title '{document_title}' does not match the expected format (regardless of upper/lowercase) based on the filename: '{expected_document_title}'",
                    file_path,
                    error=True
                )
        else:
            self.report_issue("Document does not contain a title header (h1).", file_path, error=True)

        if self.verbosity > 1:
            print(f"{json.dumps(self.results[file_path], indent=2)}\n")

    def lr_check_image_paths(self, soup: BeautifulSoup, file_path: str):
        """
        Checks that all image references in the SOP contain the correct 'docs/images' folder in their file paths.

        :param soup: BeautifulSoup object of the parsed SOP content.
        :param file_path: Path to the SOP file.
        """
        image_paths = get_image_paths(soup)
        incorrect_images = [img_path for img_path in image_paths if "docs/images" not in img_path]

        for img_path in incorrect_images:
            self.report_issue(
                f"Referenced image '{img_path}' should be located in the 'docs/images' folder or a subdirectory within it.",
                file_path,
                error=True
            )

    def get_charter_soup(self, input_file: str) -> BeautifulSoup:
        """
        Parses the Charter document into a BeautifulSoup object if it hasn't been parsed already.
        Dynamically determines the Charter path based on the input file's repository structure.
        
        :param input_file: Path to one of the input SOP files, used to determine the repo root.
        :return: BeautifulSoup object of the parsed Charter document.
        """
        if hasattr(self, 'charter_soup') and self.charter_soup:
            return self.charter_soup

        # Determine the repository root by searching for .git in parent directories
        repo_root = os.path.dirname(os.path.abspath(input_file))
        while not os.path.isdir(os.path.join(repo_root, '.git')):
            parent_dir = os.path.dirname(repo_root)
            if parent_dir == repo_root:  # We've reached the root of the file system
                raise ValueError("Repository root not found. Ensure the script is run within a GitHub repository.")
            repo_root = parent_dir

        # Construct the Charter path relative to the repository root
        charter_path = os.path.join(repo_root, 'docs', 'GDI-SOP_charter.md')

        # Parse the Charter document
        try:
            with open(charter_path, 'r') as charter_file:
                charter_content = charter_file.read()
            charter_html = markdown.markdown(charter_content, extensions=['tables'])
            self.charter_soup = BeautifulSoup(charter_html, 'html.parser')
        except FileNotFoundError:
            raise ValueError(f"Charter document not found at '{charter_path}'. Please verify the file path.")
        except Exception as e:
            raise ValueError(f"Error parsing the Charter document: {str(e)}")

        return self.charter_soup

    def find_tables(self, soup: BeautifulSoup, file_path: str, aim_headers: List[str]) -> List[BeautifulSoup]:
        """
        Uses imported function to find all tables by their set of headers
        Returns a list of tables.
        """
        if not self.tables[file_path]:
            self.tables[file_path] = soup.find_all('table')
        aim_tables = find_tables(soup=soup, aim_headers=aim_headers, tables=self.tables[file_path]) 
        return aim_tables

    def is_valid_version(self, version: str) -> bool:
        """
        Checks if the given version string follows semantic versioning.

        :param version: Version string to check.
        :return: True if the version string is valid, False otherwise.
        """
        try:
            Version(version)
            return True
        except InvalidVersion:
            return False

    def report_issue(self, message: str, file_path: str, error: bool = False, warning: bool = False):
        """
        Reports an issue found during linting.

        :param message: Description of the issue.
        :param file_path: Path to the SOP file.
        :param error: Whether the issue is an error (True) or a warning (False).
        """
        issue_type = "errors" if error or self.strict else "warnings"
        self.results[file_path][issue_type].append(message)

    def generate_report(self) -> str:
        """
        Generates a JSON formatted report of all linting results.

        :return: JSON string of the linting results and a boolean on whether there are errors or not
        """
        has_errors = any(file_results['errors'] for file_results in self.results.values())
        return json.dumps(self.results, indent=2), has_errors

def parse_args() -> Any:
    """
    Parses command-line arguments.

    :return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Lints SOP markdown files")
    parser.add_argument(
        "inputs", nargs="+", help="SOP file(s) or directories to lint. Given directories will be explored, looking for markdown files following the SOP naming conventions"
    )
    parser.add_argument(
        "-v", "--verbosity", type=int, default=0, help="Verbosity level (0-2). 0 prints nothing; 1 prints the end report; 2 prints the report of each file at each step"
    )
    parser.add_argument(
        "-s", "--strict", action="store_true", help="Treat warnings as errors."
    )
    return parser.parse_args()

def main():
    """
    Main function to run the SOP linter.
    """
    args = parse_args()
    sop_files = collect_sop_files(args.inputs)

    required_sections = {
        "## Index": "h2:contains('Index')",
        "### Document History": "h3:contains('Document History')",
        "### Glossary": "h3:contains('Glossary')",
        "### Roles and Responsibilities": "h3:contains('Roles and Responsibilities')",
        "### Purpose": "h3:contains('Purpose')",
        "### Scope": "h3:contains('Scope')",
        "### Procedure": "h3:contains('Procedure')",
        "### References": "h3:contains('References')"
    }

    linter = SOPLinter(verbosity=args.verbosity, strict=args.strict, required_sections=required_sections)
    for sop_file in sop_files:
        linter.lint_sop(sop_file, sop_files)

    report, has_errors = linter.generate_report()
    if args.verbosity > 0:
        print(report)

    # These exit codes will be interpreted downstream
    if has_errors:
        exit(1)
    else:
        exit(0)

if __name__ == "__main__":
    """
    To run it as a standalone script besides importing bits of it
    """
    main()
