import argparse
import os
import re
import pandas as pd
import markdown
from bs4 import BeautifulSoup
from typing import List, Dict
from utils import find_tables, collect_sop_files, count_procedure_steps, build_hyperlink

class SOPIndexGenerator:
    def __init__(self, verbosity: int = 0):
        """
        Initializes the SOPIndexGenerator with verbosity settings.

        :param verbosity: Level of verbosity for output messages.
        """
        self.verbosity = verbosity
        self.index_data = pd.DataFrame()

    def parse_sop(self, file_path: str) -> Dict:
        """
        Parses a single SOP file to extract relevant metadata.

        :param file_path: Path to the SOP file.
        :return: Dictionary of parsed metadata.
        """
        if self.verbosity > 1:
            print(f"-- Parsing SOP file '{file_path}' to extract information")

        with open(file_path, 'r') as file:
            content = file.read()

        html_content = markdown.markdown(content, extensions=['tables'])
        soup = BeautifulSoup(html_content, 'html.parser')

        metadata = self.extract_metadata(soup, file_path)
        num_steps = count_procedure_steps(soup)
        last_modified_date = self.extract_last_modified_date(soup, file_path)
        name_with_link = build_hyperlink(file_path)

        return {
            "Name": name_with_link,
            "Identifier": metadata.get("template sop number", ""),
            "Template version": metadata.get("template sop version", ""),
            "Topic": metadata.get("topic", ""),
            "Type": metadata.get("template sop type", ""),
            "GDI Node": metadata.get("gdi node", ""),
            "Instance version": metadata.get("instance version", ""),
            "Nº steps": num_steps,
            "Last modified": last_modified_date
        }
    
    def extract_metadata(self, soup: BeautifulSoup, file_path: str) -> Dict[str, str]:
        """
        Extracts metadata from the metadata table in the SOP file.

        :param soup: BeautifulSoup object of the parsed SOP content.
        :param file_path: Path to the SOP file.
        :return: Dictionary of extracted metadata.
        """
        metadata_table_headers = ["Metadata", "Value"]
        try:
            metadata_table = find_tables(soup, metadata_table_headers)[0]
        except IndexError:
            raise IndexError(f"Metadata table is missing from the file '{file_path}'. Could not find the table based on the given headers '{metadata_table_headers}'.")

        metadata = {}
        for row in metadata_table.find_all('tr')[1:]:
            columns = [col.text.strip() for col in row.find_all('td')]
            if len(columns) == 2:
                metadata[columns[0].lower()] = columns[1]
            else:
                raise ValueError(f"Metadata table row is incorrectly formatted (expected 2 columns) for file '{file_path}' at row: '{' | '.join(columns)}'")
        
        return metadata

    def extract_last_modified_date(self, soup: BeautifulSoup, file_path: str) -> str:
        """
        Extracts the last modified date from the 'Document History' section of the SOP.

        :param soup: BeautifulSoup object of the parsed SOP content.
        :param file_path: Path to the SOP file.
        :return: Last modified date as a string.
        """
        document_history_headers = ["Template Version", "Instance version", "Author(s)", "Description of changes", "Date"]
        try:
            document_history_table = find_tables(soup, document_history_headers)[0]
        except IndexError:
            raise IndexError(f"Document History table is missing from the file '{file_path}'. Could not find the table based on the given headers '{document_history_headers}'.")

        # The top row will be the most recent, and thus the last modification
        first_row = document_history_table.find_all('tr')[1]
        date_column = first_row.find_all('td')[4].text.strip()
        last_modified_date = re.sub(r'[`*_]', '', date_column)  # Remove any formatting characters

        return last_modified_date

    def parse_all_sops(self, sop_files: List[str]):
        """
        Parses all provided SOP files and stores the metadata in self.index_data.

        :param sop_files: List of SOP file paths.
        """
        if self.verbosity > 1:
            print("- Parsing of all SOP files")

        parsed_data = [self.parse_sop(file) for file in sop_files]
        self.index_data = pd.DataFrame(parsed_data)

        if self.index_data.empty:
            raise ValueError(f"The newly created index table was empty! Check if there were any inputs (list of files: {sop_files}).")

        self.index_data.sort_values(by="Identifier", inplace=True)

        if self.verbosity > 1:
            print("- Finished parsing all SOP files")

    def generate_index(self, output_format: str = 'markdown') -> str:
        """
        Generates the index table in the specified format.

        :param output_format: Format of the output table ('markdown', 'csv', 'json').
        :return: Formatted index table as a string.
        """
        if self.verbosity > 1:
            print(f"- Generating index table in '{output_format}' format")

        if output_format == 'markdown':
            return self.index_data.to_markdown(index=False)

        elif output_format == 'csv':
            return self.index_data.to_csv(index=False)

        elif output_format == 'json':
            return self.index_data.to_json(orient='records', indent=2)

        return ""

def parse_args():
    """
    Parses command-line arguments.

    :return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Generates an index table of SOPs")
    parser.add_argument("inputs", nargs="+", help="SOP file(s) or directories to include in the index table")
    parser.add_argument("-f", "--format", choices=["markdown", "csv", "json"], default="markdown", help="Output table format")
    parser.add_argument("-o", "--output", type=str, help="Output file path to write table")
    parser.add_argument("-v", "--verbosity", type=int, default=0, help="Verbosity level (0-2)")
    return parser.parse_args()

def main() -> str:
    """
    Main function to run the SOP Index Generator.
    """
    args = parse_args()
    sop_files = collect_sop_files(args.inputs)

    if not sop_files:
        raise FileNotFoundError(f"No SOP documents were found for the given inputs: '{args.inputs}'")

    index_generator = SOPIndexGenerator(verbosity=args.verbosity)
    index_generator.parse_all_sops(sop_files)
    index_table = index_generator.generate_index(args.format)

    if args.output:
        if not os.path.exists(args.output):
            with open(args.output, 'w') as file:
                file.write(index_table)
            if args.verbosity > 0:
                print(f"- Index table generated and saved to {args.output}")
        else:
            raise FileExistsError(f"Output file '{args.output}' already exists and will not be overwritten.")
    else:
        if args.verbosity > 0:
            print(index_table)
    
    return index_table

if __name__ == "__main__":
    main()