# GDI SOP Accessioning System Proposal
## Introduction
This document outlines the **accessioning system for Standard Operating Procedures** (SOPs) within the Genomics Data Infrastructure (GDI) project. It covers the SOP identifier format, file naming conventions, automation workflows, repository structure, version control, and referencing mechanisms. This system aims to streamline the management, versioning, and referencing of SOPs, ensuring clarity, consistency, and ease of use across the project.

## Identifier Format
In this section we cover how identifiers for SOP-related documents are given.

1. **European-level SOP instances**. To be used uniformly across all GDI nodes at European level.
   - **Format:** `GDI-SOPXXXX.vY`
     - `XXXX`: Auto-incremented SOP number.
     - `vY`: Version number starting from `v1`.
   - **Example:** `GDI-SOP0001.v1`

2. **Node-specific SOPs**.
    1. Node-specific **templates**. To be used uniformly across all GDI nodes, adapted by GDI nodes into their node-specific instances.
        - **Format:** `GDI-SOPXXXX.vY`
        - `XXXX`: SOP number from the template.
        - `vY`: Version number starting from `v1`.
    - **Example:** `GDI-SOP0001.v1`
    2. Node-specific **instances**. This format is used for instances of SOP templates that are adapted by specific nodes. The `NodeID` ensures the SOP is identifiable to a particular node, and the `vZ` allows for node-specific versioning.
        - **Format:** `GDI-SOPXXXX.vY_<NodeID>.vZ`
        - `XXXX`: SOP number from the template.
        - `vY`: Template version number.
        - `<NodeID>`: Unique Alpha-3 code for the node (e.g., `SWE` for Sweden). See more at [ISO's OBP](https://www.iso.org/obp/ui/#search/code/).
        - `vZ`: Node-specific version number starting from `v1`.
      - **Example:** `GDI-SOP0001.v1_SWE.v1`

## File Naming Conventions

### SOP documents
Identifiers can be used as unique references to SOPs, nevertheless, they are difficult to read by humans. For this reason, additionally to the identifier, the SOP filenames will have brief titles of what they encompass. 

  - **Filename format**: `<Identifier>_<Title>.md`
  - **Example**: `GDI-SOP0001.v1_Node-Helpdesk-Ticket-Management-Template.md`
    - Identifier: ``GDI-SOP0001.v1``
    - Title: ``Node-Helpdesk-Ticket-Management-Template``

Given the chosen character (``_``) for connecting the identifier and the title, neither of these should contain it within. If needed, replace it with ``-``.

For the sake of traceability through GitHub's features, the filenames of Node-specific SOP templates and instances do not change. Instead, what changes is the repository ownership:
  - Node-specific documents hosted at the [source GitHub repository](https://github.com/GenomicDataInfrastructure/standard-operating-procedures) are considered **templates**.
  - Node-specific documents hosted at GDI nodes' specific repositories are considered **instances**.

In both scenarios, **the node-specific template** (at the source repository) and **instances** (at each GDI node repository) **have the same filename**. This enables efficient traceability of files in their adaptation from templates to instances, and facilitates to resolve merging conflicts when a template is updated (i.e. a new release is provided at the source repository).

For example, see the following diagram:
````mermaid
flowchart TD
    %% Colors
    classDef SOP fill:#FFD700,stroke:#000000,stroke-width:2px;
    classDef Template fill:#87CEEB,stroke:#000000,stroke-width:2px;

    id1("GDI-SOP0001.v1")
    title1("NCPs-veto-EDIC-decision")
    subgraph Source-GitHub
        sopt["`SOP **Template**
    **Filename**: GDI-SOP0001.v1_NCPs-veto-EDIC-decision.md`"]
    end
    id2("SWE.v1")
    subgraph Node's-GitHub
        sopi["`SOP **Instance**
    **Filename**: GDI-SOP0001.v1_**SWE.v1**_NCPs-veto-EDIC-decision.md`"]
    end
    id1 -..->|+| sopt
    title1 -..->|+| sopt
    sopt -->|Node adapts template| sopi
    id2 -..->|+| sopi

    %% Styles
    class sopt Template
    class sopi SOP
````

### Supporting documents
These are additional documents that support the SOPs, such as the Charter, Information Service Management (ISM) or Organisational Roles and Responsibilities (ORR). 
   - **Filename format:** `GDI-SOP_<Title>.vY.md`
     - `<Title>`: Brief text describing the document. Should not contain ``_`` characters (replace by ``-``).
     - `vY`: Version number starting from `v1`.
   - **Example:** `GDI-SOP_Charter.v1.md`

## SOP Repository Structure
  - `sops/`: Contains **all SOPs**, both European-level SOP **instances** and Node-specific SOP **templates**.
    - `european-level/`: Contains European-level SOP Instances
    - `node-specific/`: Contains Node-specific SOP templates
  - `docs/`: Contains all other supporting documents.

## SOP Life-cycle
In this section we briefly describe the common life-cycle of an SOP within the GDI platform. For further details, take a look at the [**summary diagram**](../README.md#summary-diagram).

1. SOP is **requested** by any GDI member by making use of the [**"New SOP request"**](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/issues/new/choose) GitHub Issue Template.
2. SOP Request is evaluated by the 1+MG Working Group, which approves or denies it.
3. The SOP starts its development phase (content filling, review, approval...). This may have multiple steps, based on the chose initial method (e.g. Google Docs, GitHub...). Regardless of the method, the [general SOP template](sop-template.md) is used to construct it.
4. The SOP gets to a level of maturity where it can be added through a Pull Request to the source GitHub repository after approval from authorizers (e.g. Management Board, 1+MG Working Group).
5. PR is merged with the source repository, representing the end of its development cycle, and triggering the SOP release process. This includes steps like the SOP accessioning, where it receives its ``<Identifier>``.

If the SOP is a European-level SOP instance, it enters its own periodic review cycle. On the other hand, if it is a Node-specific SOP Template, the SOP can be then adapted by nodes once these fork/import (see [rubric](/github-management.md)) the source repository. See below an example of how a Node-specific SOP Template could be adapted between the source and a GDI's node repositories.
````mermaid
%%{init: { 'gitGraph': {'mainBranchName': 'Source-repo'}} }%%
gitGraph
    commit id: "Add SOP template"
    commit id: "GDI node forks source"
    branch Node-repo
    checkout Node-repo
    commit id: "Node adapts template"

    checkout Source-repo
    commit id: "Update SOP template"

    checkout Node-repo
    merge Source-repo id: "Node updates their instance"

    checkout Source-repo
    commit id: "Recurrent template updates"

    checkout Node-repo
    commit id: "Recurrent adaptations"
````



#! Create something similar to a version manifest, and with a GitHub action we:
  - Check that the accessioning and naming conventions are correct
  - Check that the SOP identifier is correct, and we place it into the SOP manifest/browser/table somewhere in the repo. 
    - We should have a table with all metadata of the SOPs, with their topics, location, id, title, type, etc.

**Step 3: GitHub Accessioning and Version Control**
- **Automation using GitHub Actions:**
  - **Trigger:** When a Pull Request (PR) is merged.
  - **Actions:**
    - Assign a unique SOP number (`XXXX`) and version (`vY`).
    - Update the identifier in the filename and within the document content.
    - Generate a DOI (if applicable) using a DOI service.
    - Commit the changes with a standardized commit message (e.g., `Add GDI-SOPXXXX.vY`).
    - Create a release in GitHub for the new SOP version.

**Step 4: Referencing SOPs**
- Use relative links within the GitHub repository for referencing SOPs.
- **Example:** `[GDI-SOP0001.v1](./path/to/GDI-SOP0001.v1.md)`
- **Description:** This ensures that all references are stable and linked to the correct version of the SOP.

## Version Control and Updates

- **Versioning SOPs:**
  - Increment version numbers for each approved change.
  - Use GitHub tags and releases to manage versions.

- **Notification System:**
  - Notify nodes of updates via GitHub notifications.
  - Nodes must resolve changes and update their instances accordingly.