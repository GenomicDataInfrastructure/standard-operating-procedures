# GDI SOP Accessioning Proposal
## Introduction
This document outlines the **accessioning system for Standard Operating Procedures** (SOPs) within the Genomic Data Infrastructure (GDI) project. It covers the SOP identifier format, file naming conventions, automation workflows, repository structure, version control, and referencing mechanisms. This system aims to streamline the management, versioning, and referencing of SOPs, ensuring clarity, consistency, and ease of use across the project.

## Index

1. [Identifier Format](#identifier-format)
1. [File Naming Conventions](#file-naming-conventions)
1. [SOP Repository Structure](#sop-repository-structure)
1. [SOP Life-cycle](#sop-life-cycle)
1. [Automatic SOP accessioning](#automatic-sop-accessioning)
1. [Version Control and Updates](#version-control-and-updates)

## Identifier Format
In this section we cover how identifiers for SOP-related documents are given. The two main categories are European-level and Node-specific SOPs.

1. **European-level SOP instances**. To be used uniformly across all GDI nodes at European level.
   - **Format:** `GDI-SOPXXXX.vY`
     - **Base identifier** (`GDI-SOPXXXX`): being ``XXXX`` an auto-incremented SOP number that is unique across the GDI SOP namespace.
     - `vY`: Version number starting from `v1`.
   - **Example:** `GDI-SOP0001.v1`

2. **Node-specific SOPs**.
    1. Node-specific **templates**. To be used uniformly across all GDI nodes, adapted by GDI nodes into their node-specific instances.
        - **Format:** `GDI-SOPXXXX.vY`
          - **Base identifier** (`GDI-SOPXXXX`): being ``XXXX`` an auto-incremented SOP number that is unique across the GDI SOP namespace.
          - `vY`: Version number starting from `v1`.
        - **Example:** `GDI-SOP0001.v1`
    2. Node-specific **instances**. This format is used for instances of SOP templates that are adapted by specific nodes. The `NodeID` ensures the SOP is identifiable to a particular node, and the `vZ` allows for node-specific versioning.
        - **Format:** `GDI-SOPXXXX.vY_<NodeID>.vZ`
          - **Base identifier** (`GDI-SOPXXXX`): being ``XXXX`` an auto-incremented SOP number that is unique across the GDI SOP namespace.
          - `vY`: Template version number.
          - `<NodeID>`: Unique Alpha-3 code for the node (e.g., `SWE` for Sweden). See more at [ISO's OBP](https://www.iso.org/obp/ui/#search/code/).
          - `vZ`: Node-specific version number starting from `v1`. The version of the instance is restarted everytime the template it is based on changes in version.
        - **Example:** `GDI-SOP0001.v1_SWE.v1`

The details encompassed by these identifiers **must** be added at the _Metadata_ section of each SOP (see [general SOP template](./GDI-SOP_sop-template.md)) for a clear depiction. While the ``<Base identifier>`` may define the filename, the full identifier may be used when referencing a specific version of it in written language from other resources (e.g., "_...some examples of node instances include `GDI-SOP0001.v1_SWE.v1` and `GDI-SOP0002.v3_SWE.v2`..._").

## File Naming Conventions

### SOP documents
Identifiers can be used as unique references to SOPs, nevertheless, they are difficult to read by humans. For this reason, additionally to the identifier, the SOP filenames will have **brief titles** of what they encompass.

Furthermore, before diving into the details of filenaming, we have to define a **major distinction** among documents: those that are hosted in the [main repository](https://github.com/GenomicDataInfrastructure/standard-operating-procedures), and those that are hosted in forks or imports of the main repository (see [github-management](GDI-SOP_github-management.md) document). 

In order to make use of the main features of GitHub (e.g., file changes tracking), it is crucial to **maintain integrity with regards to filenaming**. For example, if any time a file changes its version we modified its filename, we would not be able to automatically track their changes across releases and forks. For this reason, **the filename of an SOP document will be defined exclusively by its ``Base identifier``** (see [identifier format](#identifier-format) section).

  - **Filename format**: `<Base identifier>_<Title>.md`
  - **Example**: `GDI-SOP0001_Node-Helpdesk-Ticket-Management-Template.md`
    - Base identifier: ``GDI-SOP0001``
    - Title: ``Node-Helpdesk-Ticket-Management-Template``

Given the chosen character (``_``) for connecting the base identifier and the title, neither of these should contain it within. Likewise, do not use any forbidden characters for filenames (``\/:*?"<>| ``), including blank spaces. If needed, replace them with ``-``.

As mentioned above, for the sake of traceability through GitHub's features, the filenames of Node-specific SOP templates and their instances do not change. Instead, what changes is the repository ownership:
  - Node-specific documents hosted at the [source GitHub repository](https://github.com/GenomicDataInfrastructure/standard-operating-procedures) are considered **templates**. 
  - Node-specific documents hosted at GDI nodes' specific repositories are considered **instances**.

In both scenarios, **the node-specific template** (at the source repository) and **instances** (at each GDI node repository) **have the same filename**. This enables efficient traceability of files in their adaptation from templates to instances, and facilitates to resolve merging conflicts when a template is updated (i.e. a new release is provided at the source repository). Nevertheless, even if these details are not propagated to the filename, the **content of the _Metadata_ section of each of these documents should change** accordingly.

For example, see the following diagram, where we start with a Node-specific SOP template named ``GDI-SOP0001_NCPs-veto-EDIC-decision.md``, that maintains its filename when cloned by a node. Notice how the template version, node code and instance version are part of the file metadata but not of the filename.
````mermaid
flowchart TB
    %% Colors
    classDef SOP fill:#FFD700,stroke:#000000,stroke-width:2px;
    classDef Template fill:#87CEEB,stroke:#000000,stroke-width:2px;

    subgraph Source-GitHub
        sopt["`SOP **Template**
        **Filename**: GDI-SOP0001_NCPs-veto-EDIC-decision.md`"]
        subgraph SOP-template-metadata
            sopt_m1("`**Base identifier**: GDI-SOP0001`")
            title1("NCPs-veto-EDIC-decision")
            sopt_m2("`**Identifier**: GDI-SOP0001.v1`")
        end
    end
    sopt_m1 -->|+| sopt
    title1 -->|+| sopt
    sopt_m2 -..->|+| sopt
    sopt -->|Node adapts template| sopi

    subgraph Node's-GitHub
        sopi["`SOP **Instance**
    **Filename**: GDI-SOP0001_NCPs-veto-EDIC-decision.md`"]
        subgraph SOP-instance-metadata
            sopi_m2("`**Identifier**: GDI-SOP0001.v1_SWE.v1`")
        end
    end
    sopi_m2 -..->|+|sopi

    %% Styles
    class sopt Template
    class sopi SOP

````

### Supporting documents
These are additional documents that support the SOPs, but are not SOPs in themselves. For example, the SOP [Charter](GDI-SOP_charter.md). Similar to the SOPs, their identifier defines their filename, while any other piece of metadata (e.g., version) remains in their file content at the _Metadata_ section.
   - **Filename format:** `GDI-SOP_<Title>.md`
     - `<Title>`: Brief text describing the document. Should not contain ``_`` nor forbidden characters (replace by ``-``).
   - **Example:** `GDI-SOP_Charter.md`

## SOP Repository Structure
The repository is divided in two main directories:
  - `sops/`: Contains **all SOPs**, both European-level SOP **instances** and Node-specific SOP **templates**. Remember that, at the nodes' cloned repositories, these Node-specific SOPs are considered instances.
    - `european-level/`: Contains European-level SOP Instances.
    - `node-specific/`: Contains Node-specific SOP templates.
  - `docs/`: Contains all other supporting documents.

## SOP Life-cycle
In this section we briefly describe the common life-cycle of an SOP within the GDI platform. For further details, take a look at the [**summary diagram**](../README.md#summary-diagram).

1. SOP is **requested** by any GDI member by making use of the [**"New SOP request"**](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/issues/new/choose) GitHub Issue Template.
2. SOP Request is evaluated by the 1+MG Working Group, which approves or denies it.
3. The SOP starts its development phase (content filling, review, approval...). This may have multiple steps, based on the chose initial method (e.g. Google Docs, GitHub...). Regardless of the method, the [general SOP template](GDI-SOP_sop-template.md) is used to construct it.
4. The SOP gets to a level of maturity where it can be added through a Pull Request to the source GitHub repository after approval from authorizers (e.g. Management Board, 1+MG Working Group).
5. PR is merged with the source repository, representing the end of its development cycle, and triggering the SOP release process. This includes steps like the SOP accessioning, where it receives its ``<Identifier>``.

If the SOP is a European-level SOP instance, it enters its own periodic review cycle. On the other hand, if it is a Node-specific SOP Template, the SOP can be then adapted by nodes once these fork/import (see [rubric](/GDI-SOP_github-management.md)) the source repository. See below an example of how a Node-specific SOP Template could be adapted between the source and a GDI's node repositories.
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

## Automatic SOP accessioning
**#! TO-DO** once the accessioning proposal is approved: 
- To create something similar to a version manifest, making use of GitHub actions to:
  - Check that the accessioning and naming conventions are correct
  - Check that the SOP identifier is correct, and we place it into the SOP manifest/browser/table somewhere in the repo.
  - Metadata in the file-content of each SOP is correct and adecuate.
    - We should have a table with all metadata of the SOPs, with their topics, location, id, title, type, etc. This would be used in Changelogs.
  - Generate DOIs for GDI SOPs.
  - Prepare documentation (Changelog) for tags/releases.

## Version Control and Updates

- **Versioning SOPs:**
  - Increment version numbers for each approved change.
  - Use GitHub tags and releases to manage released versions.

- **Notification System:**
  - Nodes get automatic notification of updates via GitHub.
  - Nodes must resolve changes and update their instances accordingly.