# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- [``GDI-SOP_github-introduction-for-maintainers.md``](docs/GDI-SOP_github-introduction-for-maintainers.md) - Introductory guide for GDI SOP Repository maintainers.

### Modified
- [``GDI-SOP_github-management.md``](docs/GDI-SOP_github-management.md) - Added reference to recorded session
- [``GDI-SOP0003_SOP-1+MG-DAC-Recommendation-Approval.md``](sops/european-level/GDI-SOP0003_SOP-1+MG-DAC-Recommendation-Approval.md) - Updated references to _[Data Governance for Research](https://docs.google.com/document/d/1P_nzGxMXG4CWzqkVbceY2fA3MQ7PEAwW/edit)_ document.
- [``sop_linter.py``](scripts/sop_linter.py)
   - Added new Linting Rules (LR) modules: ``lr_check_procedure_step_numbering``, ``lr_check_step_consistency``, ``lr_check_glossary_in_charter``, ``lr_check_undefined_acronyms``, ``lr_check_resolvable_references``, ``lr_check_identifier_and_casing``, ``lr_check_title_match``, ``lr_check_image_paths``
   - Improved code and added a new file location check to ``lr_check_metadata_table``.
- [``utils.py``](scripts/utils.py) - Added additional helper functions: ``parse_glossary``, ``is_remote_reference_resolvable``, ``get_image_paths``.
- [``tests/``](tests/) - Updated ``tests/GDI-SOP0000_sop-template-for-linting.md`` to fit testing standards of the linting script.
- [``GDI-SOP_charter.md``](docs/GDI-SOP_charter.md) - Updated Glossary section with new acronyms and terms from other three SOPs.
- [``GDI-SOP_style-guide.md``](docs/GDI-SOP_style-guide.md) - Added section regarding positioning of tables in MD files.

### Fixed
- [``GDI-SOP0002_ncps-veto-edic-decision.md``](sops/node-specific/GDI-SOP0002_ncps-veto-edic-decision.md):
    - ``v1.0.1``: Updated Glossary, fixed Procedure headers, and renamed file (previously in uppercase).
- [``GDI-SOP0003_1+mg-dac-recommendation-approval.md``](sops/european-level/GDI-SOP0003_1+mg-dac-recommendation-approval.md):
    - ``v1.0.2``: Updated Glossary, fixed Procedure headers, fixed SOP title (in doc.), fixed relative references, and renamed file (previously ``GDI-SOP0003_SOP-1+MG-DAC-Recommendation-Approval.md``).
- [``GDI-SOP0007_sop-template-creation.md``](sops/european-level/GDI-SOP0007_sop-template-creation.md):
    - ``v1.0.1``: Updated Glossary, fixed Procedure headers and tables, and renamed file (previously in uppercase).

## [1.0.0](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/releases/tag/v1.0.0) - 2024-10-28

### Added
- [``GDI-SOP0003_SOP-1+MG-DAC-Recommendation-Approval.md``](sops/european-level/GDI-SOP0003_SOP-1+MG-DAC-Recommendation-Approval.md) - European-level SOP describing how the 1+MG DAC is to review data access requests and recommend their rejection or approval.
- [``GDI-SOP0002_NCPs-veto-EDIC-decision.md``](sops/node-specific/GDI-SOP0002_NCPs-veto-EDIC-decision.md) - Node-specific SOP Template describing how NCPs may veto EDIC decisions on data requests.
- [``GDI-SOP0007_SOP-template-creation.md``](sops/european-level/GDI-SOP0007_SOP-template-creation.md) - European-level SOP describing how to develop new SOP templates.
- [``review_reminder.yml``](.github/workflows/review_reminder.yml) - GH Workflow to periodically (monthly) and automatically (through [check_sop_reviews.py](scripts/check_sop_reviews.py)) create SOP review reminders (GH issues)
- [``check_sop_reviews.py``](scripts/check_sop_reviews.py) - Script to automatically check if SOPs are due for review and create GitHub issues if so
- [``GDI-SOP_organisational-roles-and-responsibilities.md``](docs/GDI-SOP_organisational-roles-and-responsibilities.md) - Documentation containing Organisational Roles and Responsibilities for GDI SOPs.
- [``GDI-SOP_information-service-management.md``](GDI-SOP_information-service-management.md) - Framework designed to systematically manage SOPs information flows across the GDI infrastructure
- [``GDI-SOP_review-checklist.md``](docs/GDI-SOP_review-checklist.md) - Documentation guidelines in the form of checklists, for reviewers, approvers and authorizers of SOPs.
- [``compare_index.py``](scripts/compare_index.py) - Script to automatically check if the SOP index table is up to date
- [``sop_index.py``](scripts/sop_index.py) - Script to automatically create the SOP index table
- [``utils.py``](scripts/utils.py) - General functions used by other scripts
- [``sops/README.md``](sops/README.md) - Markdown containing the SOP index table
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
