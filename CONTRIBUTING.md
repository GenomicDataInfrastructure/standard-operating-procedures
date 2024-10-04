# Contributing to the GDI SOP Repository

## Introduction

Thank you for your interest in contributing to the development of Standard Operating Procedures (SOPs) for the European Genomic Data Infrastructure (GDI) project. This repository serves as the central location for creating, managing, and maintaining SOPs, and your contributions help us ensure these materials evolve to meet the needs of the GDI network. We aim to make the contribution process easy, transparent, and collaborative.

## How to Contribute

### 1. Request Changes via GitHub Issues

**If you have suggestions for improvements or changes** to existing SOPs or documentation, you can submit a GitHub issue:

1. Go to the repository’s [Issues](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/issues) tab.
2. Click "New Issue" and select the ``SOP Content Change Suggestion`` template.
3. Provide information following the issue template: it will guide you through the process.
4. Submit the issue, and one of the repository maintainers will review and provide feedback.

### 2. Request a New SOP via GitHub Issues

**If you think a new SOP is required**, you can request it using a similar process:

1. Navigate to the [Issues](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/issues) tab.
2. Click "New Issue" and select the ``New SOP Request`` template.
3. Provide information following the issue template: it will guide you through the process.
4. Submit the issue, and one of the repository maintainers will review and provide feedback.

### 3. Submit a Pull Request (PR)

For contributors familiar with GitHub, **you can submit changes directly via a pull request (PR)**. This option is mainly for GDI members or node representatives who have forked the main repository and want to contribute updates or new SOPs:

1. Fork (or import) the repository and clone it to your local machine. See how at our [GitHub management guide](docs/GDI-SOP_github-management.md).
2. Make your changes or add new SOPs.
3. Ensure your changes adhere to the repository’s [style guide](docs/GDI-SOP_style-guide.md).
4. Run the relevant tests (see the "[Testing](#testing-your-changes)" section below) to validate any changes.
5. Submit a PR to the `dev` branch, ensuring you include a clear description of the modifications and reference any related issues.
6. The repository maintainers will review your PR and provide feedback.

### 4. Join the Task 4.3 Group

If you are part of the GDI network and would like to actively participate in SOP development, **consider joining the Task 4.3 group**. We are always open to new members to broaden representation across nodes:

1. Express your interest by contacting the Task 4.3 group through our [**Slack channel**](https://gdi-elixir.slack.com/archives/C06RJQJNHFC).
2. As a member, you will be able to contribute to SOP reviews, participate in discussions, and help shape the future of the GDI SOP framework.
3. Regular Task 4.3 meetings are held bi-weekly via Zoom, and new members are welcome to join these sessions.

## Testing Your Changes

Before submitting a PR, you should test your changes to ensure they comply with the repository’s standards.

Depending on your environment, it may be required to install the required python modules:
````
pip install --upgrade --no-deps -r requirements.txt
````

1. **Lint the SOPs**: Use the `sop_linter.py` script to check that the format of your SOP files follows the required structure.
````
# Example of linting the test SOP
python3 scripts/sop_linter.py tests/GDI-SOP0000_sop-template_for_linting.md -v 1

# To know more
python3 scripts/sop_linter.py --help
````

2.  **Check SOP index consistency**: Ensure that the index of SOPs (located in `sops/README.md`) is consistent with the actual contents of the `sops/` directory using the `compare_index.py` script.
````
# Example of linting the test SOP
python3 scripts/compare_index.py sops/README.md sops/

# To know more
python3 scripts/compare_index.py --help
````

Running these scripts before submitting your PR will help maintain consistency and prevent issues during the review process.

## Style Guide

Please refer to the [**style guide**](docs/GDI-SOP_style-guide.md) in `docs/GDI-SOP_style-guide.md` to ensure your contributions are formatted correctly. Adhering to the style guide helps keep the repository organized and ensures that all SOPs follow a unified structure.

## License

By contributing to this repository, **you agree that your contributions will be licensed** under the terms outlined in the [LICENSE](./LICENSE) file. Please review the license if you have any questions about how your contributions will be used.

## Pull Request Checklist

Before submitting a pull request, please ensure:

- [ ] Your changes follow the guidelines in the style guide (`docs/GDI-SOP_style-guide.md`).
- [ ] You have tested your changes with the provided linter and index checker scripts.
- [ ] Your PR description clearly outlines the changes and includes references to related issues (if applicable). We have a PR template in place to help you provide useful information.
- [ ] You are prepared to address any feedback from reviewers.

## Need Help?

If you have any questions or need assistance, please reach out to the team via our [Slack channel](https://gdi-elixir.slack.com/archives/C06RJQJNHFC). We are happy to help!

Thank you for contributing to the GDI project and helping us build a robust and effective SOP framework!
