import os
import re
from bs4 import BeautifulSoup
from typing import List

def find_tables(soup: BeautifulSoup, aim_headers: List[str], tables: List[BeautifulSoup] = None) -> List[BeautifulSoup]:
    """
    Finds all tables by their set of headers, among all tables in the given file content (soup).
    Returns a list of tables.
    
    :param soup: BeautifulSoup object of the parsed content.
    :param aim_headers: List of headers to match.
    :param tables: List of tables in the soup (optional).
    :return: List of tables that match the headers.
    """
    if not tables:
        tables = soup.find_all('table')

    aim_tables = []

    for table in tables:
        headers = [header.text.strip().lower() for header in table.find_all('th')]  # Convert each Table Header (th) to lowercase
        if headers == [aim_header.lower() for aim_header in aim_headers]:  # Compare with aim_headers in lowercase
            aim_tables.append(table)

    return aim_tables

def collect_sop_files(inputs: List[str]) -> List[str]:
    """
    Collects all SOP markdown files from the given input paths.
    

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