import os
import re
import argparse
import requests
import json
from typing import List, Dict, Any
import markdown
from bs4 import BeautifulSoup
from datetime import datetime
from utils import find_tables, collect_sop_files, get_gh_issues

# GitHub authentication
gh_token = os.getenv("GITHUB_TOKEN")

sop_id_regex = r"(GDI-SOP\d{4})"

# Regular expression to match the date in the document history (YYYY.MM.DD)
date_regex = r"\d{4}\.\d{2}\.\d{2}"

def parse_args() -> Any:
    """
    Parses command-line arguments.

    :return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Checks if SOP files are due for review based on the dates in their Document History")
    parser.add_argument(
        "inputs", nargs="+", help="SOP file(s) or directories to check. Given directories will be explored, looking for markdown files following the SOP naming conventions"
    )
    parser.add_argument( # By default one year
        "-dr", "--days-review", type=int, default=365, help="Number of days since last edit for an SOP document to be considered 'due for review'. Default: 365 (a full year)."
    )
    parser.add_argument(
        "-ct", "--create-issues", action="store_true", help="Flag to let the script know that, if an SOP is due for review, you want for it to create the corresponding GH issue."
    )
    parser.add_argument(
        "-r", "--repository", type=str, default="GenomicDataInfrastructure/standard-operating-procedures", help="Repository path where the GH issues will be created. Default: 'GenomicDataInfrastructure/standard-operating-procedures'"
    )
    parser.add_argument(
        "-v", "--verbosity", type=int, default=0, help="Verbosity level (0-2). 0 prints nothing; 1 prints the end report; 2 prints the report of each file at each step"
    )
    return parser.parse_args()

# Function to parse the "Document History" table and extract the last date
def get_last_edit_date(soup: BeautifulSoup, sop_file: str) -> datetime:
    """
    Extracts the most recent date from the Document History table.
    
    :param soup: BeautifulSoup object of the parsed SOP content.
    :param sop_file: Filepath of the file being checked
    :return: Most recent date (datetime object) or None if no valid date is found.
    """
    # Headers to match the Document History table
    aim_headers = ["Template Version", "Instance Version", "Author(s)", "Description of changes", "Date"]
    tables = find_tables(soup, aim_headers)

    if not tables:
        raise ValueError(f"No Document History table was found (based on given headers) for file '{sop_file}'.")

    document_history_table = tables[0]  # Use the first found table (assuming there's only one Document History table)
    first_row = document_history_table.find_all('tr')[1:2][0] # Skip header row, and get first row, which should be the newest entry
    columns = [col.text.strip() for col in first_row.find_all('td')]
    if len(columns) != len(aim_headers):
        raise ValueError(f"First row of the Document History table was found malformed (had '{len(columns)}' where it should have '{len(aim_headers)}') for file '{sop_file}'.")

    date_str = columns[4]  # The last column (5th) is expected to be the date
    if re.match(date_regex, date_str):
        last_date = datetime.strptime(date_str, "%Y.%m.%d")
    else:
        raise ValueError(f"Invalid date format '{date_str}' in the Document History table for file '{sop_file}'")

    return last_date

def check_existing_github_issues(all_issues: List, sop_file: str, verbosity: int = 1) -> int:
    """
    Checks if a GitHub issue already exists for the given SOP file.

    :param sop_file: The SOP file to check.
    :return: The issue HTML URL if an existing issue is found, otherwise None.
    """
    sop_name = os.path.basename(sop_file)
    # We extract the SOP ID from the filename (e.g., "GDI-SOP0003")
    sop_id = re.match(sop_id_regex, sop_name).group(1)

    if not all_issues:
        if verbosity > 1:
            print(f"- Given GitHub issue list was empty. Check filtering parameters if it's not expected.")
        return None

    for issue in all_issues:
        # We have already filtered all issues by the labels, so the SOP ID in the title should do the trick
        if sop_id in issue['title']: 
            issue_url = issue['html_url']
            if verbosity > 1:
                print(f"-- Existing issue found for '{sop_file}', Issue URL: {issue_url}")
            return issue_url
    
    if verbosity > 1:
        print(f"-- No existing issue was found for '{sop_id}' ('{sop_file}') in all '{len(all_issues)}' issues that were fetched.")
    return None

def create_github_issue(gh_repo: str, gh_token: str, sop_file: str, last_edit_date: datetime, days_review: int) -> int:
    """
    Creates a GitHub issue for SOP review if it hasn't been reviewed in the last year.
    
    :param gh_repo: The GH repository where the new issue is created.
    :param gh_token: GitHub token to authorize
    :param sop_file: The SOP file being reviewed.
    :param last_edit_date: The last review date of the SOP.
    :param days_review: The amount of days set as threshold for an SOP to have to go through review
    :return: The GitHub issue ID if the issue is created successfully, otherwise None.
    """
    url = f"https://api.github.com/repos/{gh_repo}/issues"
    headers = {"Authorization": f"token {gh_token}"}
    
    # Payload for the GitHub issue
    sop_name = os.path.basename(sop_file)
    # We extract the SOP ID from the filename (e.g., "GDI-SOP0003")
    sop_id = re.match(sop_id_regex, sop_name).group(1)
    
    # Issue body with proper markdown formatting
    issue_body = (
        f"## Summary\n"
        f"The SOP **'{sop_id}'** is **due for review** and potential revision.\n\n"
        
        f"## Motivation\n"
        f"Part of the SOP life-cycle is the periodic review process. After **'{days_review}' days** (defined at "
        f"`.github/workflows/review_reminder.yml`) since the last entry in the Document History, **every SOP has to be formally reviewed**, "
        f"to make sure that the SOP is still relevant and up to date. Find more information inside the **[Charter](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_charter.md)** "
        f"and **[ISM](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_information-service-management.md)** documents.\n\n"
        
        f"Based on the information in ``{sop_name}``, it was last reviewed/edited on ``{last_edit_date.date()}``. "
        f"This falls beyond the period of '{days_review}' days ago set as threshold for SOPs to be reviewed.\n\n"
        
        f"## Required action\n"
        f"- **Review document `{sop_name}`**. This includes, but not limited to: appointing relevant reviewers within the GDI network, "
        f"bringing the SOP up for discussion within GDI, reviewing that the SOP is still relevant, reviewing that the SOP complies with the styling guide...\n"
        f"- **Modify the SOP document based on the review**. For any content modification of the SOP, follow a similar approach as the one described in "
        f"**[GDI-SOP0007](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/sops/european-level/GDI-SOP0007_SOP-template-creation.md)**.\n\n"
        
        f"## Reminders:\n"
        f"- Remember to **link this GH issue with the respective PR** (i.e., copy-paste the PR URL as a comment below).\n"
        f"- Remember to **add the review/revision row to the Document History**. Even if no change was required, once the review is finished, add the proper row to the Document History of the document. "
        f"This will aid with the automatic review detection and help the maintainers know which SOPs were reviewed and by whom.\n\n"
        
        f"## Disclaimer\n"
        f"This GitHub issue was created automatically through the execution of `scripts/check_sop_reviews.py`, likely triggered through the GitHub workflow `.github/workflows/review_reminder.yml`.\n\n"
        
        f"- To stop this behaviour, remove the automatic trigger (i.e., delete 'schedule' from the workflow file). **Only do so if you are sure** that this automatic review trigger is wrong.\n"
        f"- If this automatic trigger was a fluke, it may be due to the Document History of this SOP being malformed (e.g., recent entries being added at the bottom) "
        f"or other `SOP-review` GitHub issues not being named correctly (e.g., the SOP ID should appear in the title).\n"
    )
    
    issue = {
        "title": f"[SOP Review] Review due: '{sop_name}'",
        "body": issue_body,
        "labels": ["SOP-Review"]
    }
  
    response = requests.post(url, json=issue, headers=headers)
    
    if response.status_code == 201:
        issue_data = response.json()
        issue_url = issue_data['html_url']
        return issue_url
    else:
        print(f"Failed to create issue for '{sop_file}': {response.status_code}, {response.text}")
        return None

def process_sop_file(sop_file: str, args, all_issues: List[Dict]) -> Dict:
    """
    Processes a single SOP file, checks if it is due for review, and creates GitHub issues if necessary.

    :param sop_file: Path to the SOP file being processed.
    :param args: Parsed command-line arguments.
    :param all_issues: List of all open GitHub issues for comparison.
    :return: A dictionary with the status report for the processed SOP file.
    """
    individual_report = {
        "filepath": sop_file,
        "last_edit_date": "",
        "due_review": False,
        "existing_gh_issue": "",
        "new_gh_issue": ""
    }

    with open(sop_file, 'r') as f:
        sop_content = f.read()

    html_content = markdown.markdown(sop_content, extensions=['tables'])
    soup = BeautifulSoup(html_content, 'html.parser')
    last_edit_date = get_last_edit_date(soup, sop_file)
    individual_report["last_edit_date"] = str(last_edit_date)

    # If SOP is due for review
    if last_edit_date and (datetime.now() - last_edit_date).days > args.days_review:
        individual_report["due_review"] = True
        existing_issue_url = check_existing_github_issues(all_issues, sop_file, args.verbosity)

        if not existing_issue_url and args.create_issues:
            issue_url = create_github_issue(
                gh_repo=args.repository, gh_token=gh_token, sop_file=sop_file,
                last_edit_date=last_edit_date, days_review=args.days_review
            )
            individual_report["new_gh_issue"] = issue_url
        else:
            individual_report["existing_gh_issue"] = existing_issue_url

    return individual_report


def generate_report(sop_files: List[str], args, all_issues: List[Dict]) -> Dict:
    """
    Generates a report on all processed SOP files.

    :param sop_files: List of all SOP files to be processed.
    :param args: Parsed command-line arguments.
    :param all_issues: List of all open GitHub issues for comparison.
    :return: A dictionary containing the final report.
    """
    report = {
        "n_input_files": len(sop_files),
        "n_files_due_review": 0,
        "date_now": str(datetime.now()),
        "n_days_threshold": args.days_review,
        "n_created_gh_issues": 0,
        "all_files": []
    }

    for sop_file in sop_files:
        if args.verbosity > 1:
            print(f"- Checking input file '{sop_file}'")

        individual_report = process_sop_file(sop_file, args, all_issues)
        report["all_files"].append(individual_report)

        # Count due reviews and created issues
        if individual_report["due_review"]:
            report["n_files_due_review"] += 1
        if individual_report["new_gh_issue"]:
            report["n_created_gh_issues"] += 1

    return report


def main():
    """
    Main function to check if SOPs need review and create GitHub issues for those due.
    """
    args = parse_args()
    if not gh_token:
        raise EnvironmentError("GitHub token not found. Please set the 'GITHUB_TOKEN' environment variable.")
    sop_files = collect_sop_files(args.inputs)  # Collect all SOP files from the specified directory
    all_issues = get_gh_issues(
        gh_repo=args.repository, gh_token=gh_token, issue_params={"state": "open", "labels": "SOP-Review"}
    )  # Collect all GH issues with the given parameters

    # Generate the final report, check issues and create new ones if needed
    report = generate_report(sop_files, args, all_issues)

    if args.verbosity > 0:
        print(json.dumps(report, indent=2), "\n")


if __name__ == "__main__":
    main()