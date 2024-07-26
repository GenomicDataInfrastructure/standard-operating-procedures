import argparse
import os
import json
import pandas as pd
from typing import Dict, Any
from io import StringIO
from sop_index import SOPIndexGenerator
from utils import collect_sop_files

class SOPIndexComparator:
    def __init__(self, verbosity: int = 0):
        """
        Initializes the SOPIndexComparator with verbosity settings.

        :param verbosity: Level of verbosity for output messages.
        """
        self.verbosity = verbosity

    def read_existing_index(self, file_path: str) -> pd.DataFrame:
        """
        Reads and parses the existing SOP index markdown file.

        :param file_path: Path to the existing index file.
        :return: DataFrame of the existing index.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File '{file_path}' does not exist.")
        
        if os.path.getsize(file_path) == 0:
            raise ValueError(f"File '{file_path}' is empty.")

        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Identify the start of the markdown table
        start_index = 0
        for i, line in enumerate(lines):
            if line.strip().startswith('|'):
                start_index = i
                break
        
        # Remove leading and trailing '|' characters from each line, to avoid empty columns after read as CSV
        cleaned_lines = [line.strip().strip('|') for line in lines[start_index:]]
        
        # Filter out lines that are just dashes, colons, whitespaces or vert. lines (format rows in Markdown)
        table_lines = [line for line in cleaned_lines if not set(line.strip()) <= {'-', ':', ' ', '|'}]

        table_str = '\n'.join(table_lines)
        existing_index = pd.read_csv(StringIO(table_str), sep='|')
        existing_index.columns = existing_index.columns.str.strip()  # Strip column names

        check_duplicate_identifiers(existing_index, file_path)

        return existing_index

    def compare_indexes(self, existing_index: pd.DataFrame, new_index: pd.DataFrame) -> Dict[str, Any]:
        """
        Compares the existing and new SOP index tables.

        :param existing_index: DataFrame of the existing index.
        :param new_index: DataFrame of the new index.
        :return: Dictionary of comparison results.
        """
        results = {
            "num_existing_sops": len(existing_index),
            "num_new_sops": len(new_index),
            "differences": []
        }

        # Compare the number of rows
        if len(existing_index) != len(new_index):
            results["differences"].append(f"Number of SOPs differs: existing ({len(existing_index)}), new ({len(new_index)})")

        # Strip leading and trailing whitespaces in all string columns
        existing_index = existing_index.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        new_index = new_index.applymap(lambda x: x.strip() if isinstance(x, str) else x)

        # Merge indexes to find differences in rows and column values
        merged_index = existing_index.merge(new_index, on="Identifier", suffixes=('_existing', '_new'), how='outer', indicator=True)

        # Identify rows that are present in one DataFrame but not the other
        differences = merged_index[merged_index['_merge'] != 'both']
        if not differences.empty:
            for _, row in differences.iterrows():
                diff = {"Identifier": row["Identifier"], "Differences": {}}
                if row['_merge'] == 'left_only':
                    diff["Differences"] = "Missing from the new index table."
                elif row['_merge'] == 'right_only':
                    diff["Differences"] = "Missing from the existing index table."
                results["differences"].append(diff)

        # Identify rows that are present in both DataFrames but have differing values
        common_rows = merged_index[merged_index['_merge'] == 'both']
        for _, row in common_rows.iterrows():
            diff = {"Identifier": row["Identifier"], "Differences": {}}
            row_diff = False
            for col in existing_index.columns:
                if col == "Identifier":
                    continue  # Skip the Identifier column
                col_existing = f"{col}_existing"
                col_new = f"{col}_new"
                if row[col_existing] != row[col_new]:
                    diff["Differences"][col] = {"existing": row[col_existing], "new": row[col_new]}
                    row_diff = True
            if row_diff:
                results["differences"].append(diff)

        return results


def parse_args():
    """
    Parses command-line arguments.

    :return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Compares existing SOP index with a newly generated index")
    parser.add_argument("existing_index", type=str, help="Path to the existing SOP index markdown file")
    parser.add_argument("inputs", nargs="+", help="SOP file(s) or directories to include in the new index")
    parser.add_argument("-v", "--verbosity", type=int, default=0, help="Verbosity level (0-2)")
    return parser.parse_args()

def check_duplicate_identifiers(df: pd.DataFrame, source: str, column_header: str = "Identifier"):
    """
    Checks for duplicate identifiers in the given DataFrame and raises an error if any are found.

    :param df: DataFrame to check for duplicate identifiers.
    :param source: Source of the table (e.g., path to the file being checked), used for error message
    """
    df[column_header] = df[column_header].str.strip()  # Strip leading and trailing whitespace from identifiers
    duplicated_identifiers = df[column_header].duplicated()
    if duplicated_identifiers.any():
        duplicated_ids = df[duplicated_identifiers][column_header].str.strip().unique().tolist()
        n_duplicated_ids = len(duplicated_ids)
        raise ValueError(f"Duplicate identifiers ('{n_duplicated_ids}' unique IDs) found in the given index table ({source}). Identifiers should be unique. See list of repeated identifiers: {duplicated_ids}")

def main():
    """
    Main function to run the SOP Index Comparator.
    """
    args = parse_args()
    
    comparator = SOPIndexComparator(verbosity=args.verbosity)

    if args.verbosity > 1:
        print(f"- Reading existing index from '{args.existing_index}'")
    existing_index = comparator.read_existing_index(args.existing_index)

    if args.verbosity > 1:
        print(f"\n- Existing index table\n{existing_index}")

    if args.verbosity > 1:
        print(f"- Generating new index from inputs: {args.inputs}")
    sop_files = collect_sop_files(args.inputs)
    index_generator = SOPIndexGenerator(verbosity=args.verbosity)
    index_generator.parse_all_sops(sop_files)
    new_index = index_generator.index_data
    check_duplicate_identifiers(new_index, f"created using '{args.inputs}' as inputs")

    if args.verbosity > 1:
        print(f"\n- New index table\n{new_index}")

    if args.verbosity > 1:
        print("- Comparing indexes")
    comparison_results = comparator.compare_indexes(existing_index, new_index)

    if args.verbosity > 0:
        print(json.dumps(comparison_results, indent=2),"\n")
    
    # If there are any differences, exit apropriately
    if len(comparison_results["differences"]):
        exit(1)
    else:
        exit(0)

if __name__ == "__main__":
    main()
