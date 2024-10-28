import os
import re
from bs4 import BeautifulSoup
from typing import List, Dict
import requests

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

def count_procedure_steps(soup: BeautifulSoup, procedure_header: str = "Procedure") -> int:
    """
    Counts the number of steps in the 'Procedure' section of an SOP.

    :param soup: BeautifulSoup object of the parsed SOP content.
    :param procedure_header: Keyword to identify the procedure header (optional)
    :return: Number of steps in the 'Procedure' section.
    """
    procedure_section = soup.find(re.compile('^h3$'), text=re.compile(rf'^\d*\.*\s*{procedure_header}$', re.IGNORECASE))
    num_steps = 0
    if procedure_section:
        for sibling in procedure_section.find_next_siblings():
            if re.match(r'^h[1-6]$', sibling.name) and sibling.name <= procedure_section.name:
                break
            if re.match(r'^h4$', sibling.name):
                # We count as steps the headers of each step "#### ..." in the SOP
                num_steps += 1
    else:
        return None
    
    return num_steps

def build_hyperlink(file_path: str, relative_directory: str = "sops"):
    """
    Builds a filename with a relative path to a given directory.
    Example output: "[GDI-SOP0000_test.md](european-level/GDI-SOP0000_test.md)"

    :param file_path: File path of the file.
    :param relative_directory: directory to which the filepath will be relative to (optional)
    :return: Filename with relative path reference
    """
    sops_index = file_path.lower().find(f'{relative_directory}/')    
    if sops_index == -1:
        raise ValueError(f"For file '{file_path}', the given '{relative_directory}' directory was not found in its filepath, and could not construct its relative filepath")
    relative_path = file_path[sops_index + len(relative_directory) + 1:]
    file_name = os.path.basename(file_path)
    name_with_link = f"[{file_name}](./{relative_path})"

    return name_with_link

def get_gh_issues(gh_repo: str, gh_token: str, issue_params: Dict):
    """
    Gets all GH issues of the given repository with specific criteria

    :param gh_repo: GitHub repository path (e.g., 'GenomicDataInfrastructure/standard-operating-procedures')
    :param gh_token: GitHub token to authorize
    :param issue_params: Parameters used to filter the GH issues (e.g., '{"state": "open", "labels": "SOP-Review"}')
    """
    url = f"https://api.github.com/repos/{gh_repo}/issues"
    headers = {"Authorization": f"token {gh_token}"}

    response = requests.get(url, headers=headers, params=issue_params)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch GH issues: {response.status_code}, {response.text}")
    
    # GH's API treats issues and pull requests similarly, so we filter them here
    all_issues = [issue for issue in response.json() if "pull_request" not in issue]
    
    return all_issues