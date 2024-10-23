# Introduction to GitHub for GDI SOP Maintainers

This guide is designed to **help maintainers** of the [Genomic Data Infrastructure (GDI) SOP Repository](https://github.com/GenomicDataInfrastructure/standard-operating-procedures) understand and navigate the **basic functionalities of GitHub**. It covers the essentials of creating and managing pull requests, handling issues, working with branches, and using GitHub workflows within the context of SOP maintenance.

## Index
1. [What is GitHub?](#what-is-github)
2. [Understanding the Repository](#understanding-the-repository)
3. [Issues](#issues)
4. [Branches](#branches)
5. [Pull Requests (PRs)](#pull-requests)
6. [Workflows and Linting](#workflows-and-linting)
7. [General Recommendations](#general-recommendations)
8. [Further Reading](#further-reading)

---

## What is GitHub?

GitHub is a platform that allows for collaborative development of projects through version control. For this repository, GitHub allows multiple maintainers and contributors to work on the **Standard Operating Procedures (SOPs)** simultaneously, ensuring that changes are tracked and reviewed before they are added to the main branch. Each repository is made up of a combination of code files, documentation, and workflows that automate certain actions (like verifying formatting).

### Key GitHub Concepts:
- **Repository:** A directory containing project files. In this case, the GDI SOP repository stores the SOPs and their associated metadata.
- **Branch:** A separate version of the repository where you can work on changes without affecting the main codebase.
- **Commit:** A record of changes made to files.
- **Pull Request (PR):** A request to merge changes from one branch to another.
- **Issue:** A way to track tasks, improvements, or bugs in the repository.

Refer to the [GDI-SOP charter](../docs/GDI-SOP_charter.md) for more on the structure and purpose of this repository.

---

## Understanding the Repository

This repository has a specific folder and file structure, including:
- **`/docs/`**: Contains documentation files, including this guide.
- **`/SOPs/`**: Contains the Standard Operating Procedures.
- **`/scripts/`**: Contains scripts that are used in workflows to automate certain processes (like linting).
- **`README.md`**: The main landing page for the repository, explaining its purpose.

Refer to the [SOP accessioning guide](../docs/GDI-SOP_sop-accessioning.md) for more details on how files in this repo are named and organised.

---

## Issues

Issues are used to track tasks, requests, or bugs. When you create an issue, it automatically gets added to the ZenHub board used by GDI for project management.

### Creating an Issue
1. Navigate to the **Issues** tab at the top of the repository.
2. Click on **New Issue**.
3. Select the appropriate template (e.g., "SOP Update", "New SOP", etc.).
4. Fill in the necessary details: Title, Description, and any relevant labels.

    ![Add Screenshot Placeholder for Creating Issues]

Make sure to assign relevant labels, milestones, and the person responsible. The issue will now appear in the issues list and the ZenHub board.

---

## Branches

Branches allow you to work on changes without affecting the main or dev branches.

### Main Branches in the Repository
- **`main`**: The primary branch, representing the most stable version of the repository.
- **`dev`**: A branch where new features and changes are tested before being merged into `main`.

### Creating a New Branch
1. Navigate to the **Code** tab.
2. Click the dropdown next to the current branch (usually `main` or `dev`).
3. Type the name of the new branch and press **Enter**. It will be created from the current branch you're viewing.

    ![Add Screenshot Placeholder for Creating Branch]

### Best Practices
- Never commit directly to the `main` branch.
- Always create a branch from the `dev` branch or another working branch.
- Keep branch names descriptive (e.g., `feature/new-sop` or `bugfix/sop-typo`).

Refer to the [organisational roles and responsibilities guide](../docs/GDI-SOP_organisational-roles-and-responsibilities.md) for branch management roles and responsibilities.

---

## Pull Requests

Pull Requests (PRs) are used to propose changes from one branch to another. They ensure that changes are reviewed before being added to the repository.

### Creating a Pull Request
1. Once you've finished your changes on a branch, go to the **Pull Requests** tab.
2. Click **New Pull Request**.
3. Select the branch you want to merge from and the branch you want to merge into (e.g., `dev`).
4. Provide a clear title and description of your changes.
5. Assign reviewers, labels, and link any related issues.

    ![Add Screenshot Placeholder for Creating a PR]

### Reviewing a Pull Request
1. Navigate to the **Pull Requests** tab and select the PR you want to review.
2. Review the changes by clicking on the **Files Changed** tab.
3. Add comments or approve the changes.

For more details on the reviewing process, refer to the [review checklist](../docs/GDI-SOP_review-checklist.md).

---

## Workflows and Linting

GitHub Workflows help automate certain actions in the repository. In the GDI SOP repository, workflows are used to ensure SOPs follow proper formatting and style guidelines. 

### Common Workflows:
- **Linting**: Checks the SOP formatting. It runs automatically when a PR is opened or updated.
- **Merging**: Automates some aspects of merging once all reviews are complete.

You can find the workflow configurations in the `.github/workflows/` directory, and the scripts they run in the `/scripts/` folder.

To learn more about each specific workflow, see the description at the top of the corresponding workflow file in `.github/workflows/`.

---

## General Recommendations

- **Do not push directly to `main`**: Always use a PR to propose changes.
- **Check PR origin**: Review who submitted the PR and ensure it follows repository guidelines before merging.
- **Ensure workflow checks pass**: Before merging a PR, ensure that all GitHub Actions workflows have passed (e.g., linting).
- **Clear commit messages**: Use descriptive commit messages to help maintain a clean history (e.g., `Fix SOP typo in section 2.3`).

---

## Further Reading

- [GDI SOP GitHub Management](../docs/GDI-SOP_github-management.md): How to manage the GitHub repository.
- [GDI SOP Review Checklist](../docs/GDI-SOP_review-checklist.md): Detailed instructions on how to review SOPs.
- [GDI SOP Style Guide](../docs/GDI-SOP_style-guide.md): Formatting rules for SOPs.

---

