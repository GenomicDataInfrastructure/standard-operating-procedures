# GDI SOP Style Guide

This document outlines the format and style required for all Standard Operating Procedures (SOPs) in the Genomic Data Infrastructure (GDI) repository. By adhering to these guidelines, contributors ensure clarity, consistency, and ease of use for all SOP documents.

## 1. General Style and Tone

- **Tone**: SOPs should be formal but clear and straightforward. Avoid overly technical jargon unless necessary, and make sure to explain any complex terms in the Glossary section.
  - Example: Instead of "_Utilize the methodology outlined_", prefer "_Follow the steps provided_".
- **Clarity**: Each SOP should be written assuming the reader has no prior knowledge of the task. Avoid assumptions about background knowledge, especially for tasks that may vary across nodes.
- **Consistency**: Always use consistent terminology, capitalization, and phrasing across all SOPs. For instance, technical terms, SOP titles, and key phrases should remain uniform across different documents. Check existing SOPs to get a sense of how the language has been built before.

## 2. Headings and Structure

- Use **Markdown headings** to structure the document:
  - The title of the SOP should be an H1 (`#`).
  - Index should be H2 (`##`)
  - Major sections (e.g., Purpose, Procedure) should use H3 (`###`).
  - Subsections within each major section should be H4 or lower (`####`).
  
- Ensure all section and subsection titles are in **title case** (capitalize major words).

### Example:
````markdown
# European GDI - Data Security SOP
## Index
...
### Purpose
...
### Procedure
#### 1. Initial step...
...
````
## 3. Formatting Text and Tables

### 3.1 Text

- **Sentence Structure**: Keep sentences short and active. Break information into small, manageable chunks (e.g., 3-4 sentences per paragraph).
- **Bullet Points**: Use bullet points to list steps or items where appropriate. This improves readability and makes it easier to follow step-by-step instructions.
- **Use of Emphasis**: Use `**bold**` text for emphasis when highlighting important terms or warnings. Avoid excessive use of italics (`_italics_`).

### 3.2 Tables

- Use **Markdown tables**, not HTML, where applicable. This is relevant for scripts automatically parsing the SOPs for different tasks. Tables should be used to organize structured information like roles, metadata, and steps.
- Ensure that all tables are easy to read, with no excessive or complex formatting.
- When possible, keep tables concise and avoid horizontal scrolling.
- **Always** leave an empty line right before a new table (i.e., right above the header). Otherwise, the table may be interpreted as a continuation of the previous paragraph instead. This may lead to tables not being found by the maintenance scripts.

### Example:
````markdown
| Step Number | Description               | Responsible Party |
|-------------|---------------------------|-------------------|
| Step 1      | Review data access request | Data Protection Officer |
````
## 4. Diagrams and Visuals

- Diagrams (e.g., process flows, context summaries) should be included where applicable to visually represent workflows.
- Use **Mermaid** or **PlantUML** diagrams, which are easily rendered in Markdown. Ensure that the diagrams are simple, legible, and closely match the step-by-step description in the text.
- Diagrams should be placed within the **Summary or Context Diagram** section and must have clear labels and flow directions to prevent ambiguity.

If you are new to mermaid diagrams, make use of the [mermaid.live](https://mermaid.live/) playground, where you will be able to get examples of diagrams and see live how yours looks.
### Example of a Mermaid diagram:
````mermaid
graph TD;
  Start -->|Start with| Step1["Item 1"]
  Step1 -->|Which is<br>used by| Step2("Action 2")
  Step2 -->|To create| End["Outcome!"]
````
## 5. Code Blocks

- Use **Markdown code blocks** (four backticks: '`` ```` ``') for any command-line instructions or code snippets. Specify the language (e.g., `bash`, `python`) for proper syntax highlighting.
- Keep the code snippets concise and relevant to the SOP.
- Code blocks must be **standalone**; avoid embedding within paragraphs.

### Example:
````bash
# And now execute... 
python3 scripts/sop_linter.py sops/ -v 1
````
## 6. Hyperlinks and References

- Use **Markdown links** (e.g., `[text](url)`) for references to external resources or other SOPs.
- Always use **relative links** (e.g., ``../sops/README.md``, as opposed to ``github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/sops/README.md``) when linking to other documents in the repository to avoid breaking links after releases. The only exception is the [General SOP template](./GDI-SOP_sop-template.md), which needs absolute URLs for them to make sense in Google Drive.
- Example: `See [SOP index table](../sops/README.md)`.

## 7. File Naming and Folder Structure

See in detail how files are to be named at the [SOP Accessioning documentation](./GDI-SOP_sop-accessioning.md#file-naming-conventions). Overall, assume the following:

- File names should be **all lowercase** (except for ``GDI-SOP...``) and use **hyphens** to separate words. Acronyms may remain uppercase if necessary for clarity.
  - Example: `GDI-SOP_style-guide.md`.
- SOPs must be organized into the correct folder based on their topic or category. Ensure the folder structure follows the logical groupings established in the repository.
- If images are used in an SOP, use the ``docs/images`` folder and reference them from there in the respective SOPs.

### Folder Example:
````text
sops/
    README.md
    european-level/
    node-specific/
````
## 8. SOP Linter and Validation

- The repository includes a **SOP linter** (`scripts/sop_linter.py`) that checks for the basic structural requirements of each SOP. **Test your SOP** using the linter before submission:
    - Example: `python3 scripts/sop_linter.py sops/path/your-sop-file.md -v 1`
  
- Ensure your SOP index is updated by running `compare_index.py` to verify that the `sops/README.md` matches the directory contents.
    - Example: `python3 scripts/compare_index.py sops/README.md sops`

## 9. Style Consistency

- **Language**: Ensure that language is consistent throughout the SOP and across all SOPs. Avoid switching between different terms for the same concept (e.g., "approve" vs. "authorize").
- **Acronyms and Abbreviations**: Define all acronyms the first time they are used in each SOP and include them in the Glossary section.
- **Tone**: Use an instructional, direct tone. Avoid overly technical language unless necessary, and ensure instructions are actionable and easy to follow.
- **Clearly define who the actor of each step is**: Talk in second person as if you were talking to the reader, where applicable. Clearly define who the reader is expected to be (e.g., ``As a Management Board member, do ...``)

## 10. Submitting and Reviewing SOPs

- Ensure that your SOP follows this style guide before submitting it as a pull request (PR).
- The **SOP linter** will automatically check for basic style compliance, but it is the author's responsibility to ensure that the SOP is clear, coherent, and follows the style guidelines.
