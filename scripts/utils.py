from bs4 import BeautifulSoup
from typing import List

def find_tables(soup: BeautifulSoup, aim_headers: List[str], tables: List[BeautifulSoup] = None) -> List[BeautifulSoup]:
    """
    Finds all tables by their set of headers, among all tables in the given file content (soup).
    Returns a list of tables.
    """
    if not tables:
        tables = soup.find_all('table')

    aim_tables = []

    for table in tables:
        headers = [header.text.strip().lower() for header in table.find_all('th')]  # Convert each Table Header (th) to lowercase
        if headers == [aim_header.lower() for aim_header in aim_headers]:  # Compare with aim_headers in lowercase
            aim_tables.append(table)

    return aim_tables

