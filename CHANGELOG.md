# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- [``GDI-SOP0003_SOP-1+MG-DAC-Recommendation-Approval.md``](sops/european-level/GDI-SOP0003_SOP-1+MG-DAC-Recommendation-Approval.md) - European-level SOP describing how the 1+MG DAC is to review data access requests and recommend their rejection or approval.
- [``GDI-SOP0002_NCPs-veto-EDIC-decision.md``](sops/node-specific/GDI-SOP0002_NCPs-veto-EDIC-decision.md) - Node-specific SOP Template describing how NCPs may veto EDIC decisions on data requests.
- [``GDI-SOP0007_SOP-template-creation.md``](sops/european-level/GDI-SOP0007_SOP-template-creation.md) - European-level SOP describing how to develop new SOP templates.
- [``review_reminder.yml``](.github/workflows/review_reminder.yml) - GH Workflow to preiodically (monthly) and automatically (through [check_sop_reviews.py](scripts/check_sop_reviews.py)) create SOP review reminders (GH issues)
- [``check_sop_reviews.py``](scripts/check_sop_reviews.py) - Script to automatically check if SOPs are due for review and create GitHub issues if so
- [``GDI-SOP_organisational-roles-and-responsibilities.md``](docs/GDI-SOP_organisational-roles-and-responsibilities.md) - Documentation containing Organisational Roles and Responsibilities for GDI SOPs.
- [``GDI-SOP_information-service-management.md``](GDI-SOP_information-service-management.md) - Framework designed to systematically manage SOPs information flows across the GDI infrastructure
- [``GDI-SOP_review-checklist.md``](docs/GDI-SOP_review-checklist.md) - Documentation guidelines in the form of checklists, for reviewers, approvers and authorizers of SOPs.
- [``GDI-SOP_charter.md``](docs/GDI-SOP_charter.md) - Documentation Charter of the task 4.3
- [``compare_index.py``](scripts/compare_index.py) - Script to automatically check if the SOP index table is up to date
- [``sop_index.py``](scripts/sop_index.py) - Script to automatically create the SOP index table
- [``utils.py``](scripts/utils.py) - General functions used by other scripts
- [``sops/README.md``](sops/README.md) - Markdown containing the SOP index table
- [``GDI-SOP_review-checklist.md``](docs/GDI-SOP_review-checklist.md) - Documentation guidelines in the form of checklists, for reviewers, approvers and authorizers of SOPs.
- [``GDI-SOP_charter.md``](docs/GDI-SOP_charter.md) - Documentation Charter of the task 4.3
- [``tests/``](tests/) - Directory containing tests to run GH repo's code
- [``requirements.txt``](requirements.txt) - Needed modules to run GH repo's code
- [``lint_sops.yml``](.github/workflows/lint_sops.yml) - GH Workflow to trigger linter on PRs
- [``sop_linter.py``](scripts/sop_linter.py) - Python script to lint SOPs
- [``CHANGELOG.md``](CHANGELOG.md) - Repository's changelog
- [``pull_request_template.md``](.github/pull_request_template.md) - PR Template for the repository
- [``new_sop_request.yaml``](.github/ISSUE_TEMPLATE/new_sop_request.yaml) - GH Issue template for new SOP requests
- [``content_suggestion.yaml``](.github/ISSUE_TEMPLATE/content_suggestion.yaml) - GH Issue template for SOP change requests
- [``GDI-SOP_github-management.md``](docs/GDI-SOP_github-management.md) - How GDI nodes can manage implementations through GitHub
- [``GDI-SOP_sop-accessioning.md``](docs/GDI-SOP_sop-accessioning.md) - How documents in this repository, including SOPs, attain their identifiers and filenames
- [``GDI-SOP_sop-template.md``](docs/GDI-SOP_sop-template.md) - General SOP template
- [``GDI-SOP_style-guide.md``](docs/GDI-SOP_style-guide.md) - Draft of styling guide
- [``README.md``](README.md) - Main repository's readme
- [``LICENSE``](LICENSE) - Repository license
