import argparse
import os
import re
import json
from typing import List, Dict, Any
from packaging.version import Version, InvalidVersion
import markdown
from bs4 import BeautifulSoup

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

    def lint_sop(self, file_path: str):
        """
        Lints a single SOP file for compliance with the required rules.

        :param file_path: Path to the SOP file.
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
        metadata_table = self.find_tables(soup = soup, file_path = file_path, aim_headers = metadata_table_headers)[0]

        if not metadata_table:
            self.report_issue("Metadata table is missing or incorrectly formatted.", file_path, error=True)
            return

        rows = metadata_table.find_all('tr') # Table rows (tr)
        # Expected format of the "Value" column of each row
        expected_metadata = {
            "Template SOP number": r"GDI-SOP\d{4}", # e.g.: GDI-SOP0001
            "Template SOP version": self.is_valid_version, # e.g.: v1
            "Template SOP Type": ["Node-specific SOP", "European-level SOP"],
            "GDI Node": r"^[A-Z]{3}$", # e.g.: SWE (for Sweden)
            "Instance version": self.is_valid_version, # e.g.: v1
        }

        table_dict = {}

        # Iterate over each table row, applying its validation rule
        for row in rows[1:]:  # Skip the header row
            columns = [col.text.strip() for col in row.find_all('td')]
            if not len(columns) == 2:
                self.report_issue(f"Metadata table row is incorrectly formatted (2 columns are expected): '{' | '.join(columns)}'.", file_path, error=True)
                continue
            key, value = columns[0], columns[1]
            table_dict[key] = value

        for key, value in table_dict.items():

            # Linting rules for node-specific SOPs should not apply for european-level ones
            if key == "GDI Node" or key == "Instance version":
                try:
                    if table_dict["Template SOP Type"].lower() == "European-level SOP".lower():
                        continue
                except:
                    pass

            if key in expected_metadata:
                # Depending on the type of format rules for each row, we apply them differently
                if isinstance(expected_metadata[key], str) and not re.match(expected_metadata[key], value):
                    # e.g., GDI-SOP0001
                    self.report_issue(f"{key} is incorrectly formatted: '{value}'.", file_path, error=True)
                elif callable(expected_metadata[key]) and not expected_metadata[key](value):
                    # e.g., v1.0.2
                    self.report_issue(f"{key} is incorrectly formatted: '{value}'.", file_path, error=True)
                elif isinstance(expected_metadata[key], list) and value.lower() not in [item.lower() for item in expected_metadata[key]]:
                    # e.g., Node-specific SOP
                    self.report_issue(f"{key} is invalid: '{value}'. It's value should be one of: {expected_metadata[key]}", file_path, error=True)
            else:
                self.report_issue(f"Unexpected row in metadata table: '{' | '.join(columns)}'.", file_path, warning=True)

        for key in expected_metadata.keys():
            if key not in table_dict.keys():
                self.report_issue(f"Metadata row '{key}' is missing from the metadata table.", file_path, error=True)

        try:
            if table_dict["Template SOP Type"] == "European-level SOP" and (table_dict["GDI Node"] or table_dict["Instance version"]):
                self.report_issue("European-level SOPs should not have 'GDI Node' or 'Instance version' values.", file_path, error=True)
        except Exception: 
            # The missing rows are already reported above
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
        document_history_table = self.find_tables(soup, file_path, aim_headers)[0]

        if not document_history_table:
            self.report_issue("Document History table is missing or incorrectly formatted.", file_path, error=True)
            return
        
        rows = document_history_table.find_all('tr')[1:]  # Skip the header row
        previous_template_version = None
        previous_instance_version = None

        for row in rows:
            columns = [col.text.strip('`').strip() for col in row.find_all('td')]

            if len(columns) != 5:
                self.report_issue(f"Document History table row is incorrectly formatted (expected 5 columns): '{' | '.join(columns)}'.", file_path, error=True)
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
                self.report_issue(f"Template Version is incorrectly formatted: '{template_version}'.", file_path, error=True)
                continue

            if instance_version:
                if self.is_valid_version(instance_version):
                    current_instance_version = Version(instance_version)                    
                else:
                    self.report_issue(f"Instance Version is incorrectly formatted: '{instance_version}'.", file_path, error=True)
                    continue
            else:
                current_instance_version = None

            if previous_template_version:
                # Template versions should be equal or lower than the ones above (more recent)
                if (current_template_version > previous_template_version) or (current_template_version == previous_template_version and not previous_instance_version):
                    self.report_issue(f"Template version ('{current_template_version}') should be lower than the version right above ('{previous_template_version}'). Notice the order of the table: from recent (top) to older (bottom) and address the versioning. Row: '{' | '.join(columns)}'.", file_path, error=True)

                # Instance versions are not always required, only when it's a node instance
                if current_instance_version and previous_instance_version:
                    # Instance versions should always be higher than the previous one
                    if current_instance_version >= previous_instance_version:
                        self.report_issue(f"Instance Version ('{current_instance_version}') should be lower than the version right above ('{previous_instance_version}'). Notice the order of the table: from recent (top) to older (bottom) and address the versioning. Row: '{' | '.join(columns)}'.", file_path, error=True)

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
        roles_table = self.find_tables(soup, file_path, aim_headers)[0]

        if not roles_table:
            self.report_issue("Roles and Responsibilities table is missing or incorrectly formatted.", file_path, error=True)
            return

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
                self.report_issue(f"Section '{section_title}' is missing.", file_path, error=True)
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

    def find_tables(self, soup: BeautifulSoup, file_path: str, aim_headers: List[str]) -> List[BeautifulSoup]:
        """
        Finds all tables by their set of headers, among all tables in the given file content (soup).
        Returns a list of tables.
        """
        if not self.tables[file_path]:
            self.tables[file_path] = soup.find_all('table')

        aim_tables = []

        for table in self.tables[file_path]:
            headers = [header.text.strip() for header in table.find_all('th')]
            if headers == aim_headers:
                aim_tables.append(table)

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

        :return: JSON string of the linting results.
        """
        return json.dumps(self.results, indent=2)

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

def collect_files(inputs: List[str]) -> List[str]:
    """
    Collects SOP markdown files from input paths.

    :param inputs: List of file or directory paths.
    :return: List of SOP markdown file paths.
    """
    sop_files = []
    for path in inputs:
        if os.path.isfile(path):
            sop_files.append(path)
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    if re.match(r"GDI-SOP\d{4}.*\.md", file):
                        sop_files.append(os.path.join(root, file))
    return sop_files

def main():
    """
    Main function to run the SOP linter.
    """
    args = parse_args()
    sop_files = collect_files(args.inputs)

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
        linter.lint_sop(sop_file)

    report = linter.generate_report()
    if args.verbosity > 0:
        print(report)
    return report

if __name__ == "__main__":
    main()