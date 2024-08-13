# European GDI - SOP Charter
## Index
1. [Document History](#1-document-history)
1. [Glossary](#2-glossary)
1. [Roles and Responsibilities](#3-roles-and-responsibilities)
1. [Introduction](#4-introduction)
1. [Purpose of this Charter](#5-purpose-of-this-charter)
1. [Scope of GDI SOPs](#6-scope-of-gdi-sops)
1. [GDI SOP Management](#7-gdi-sop-management)
1. [GDI SOP Communication](#8-gdi-sop-communication)
1. [References](#9-references)

## 1. Document History
| Version | Author(s)               | Description of Changes                                   | Date       |
| ------- | ----------------------- | -------------------------------------------------------- | ---------- |
| v1      | Marcos Casado Barbero   | Filled in gaps, formatted file, added new sections, resolved comments | 12.08.2024 |
| v0      | Mallory Freeberg, Marcos Casado Barbero | Drafted charter | 26.03.2024 |

## 2. Glossary
The following table defines the abbreviations and terms relevant to GDI SOPs.

| Abbreviation | Description                    |
| ------------ | ------------------------------ |
| GDI          | European Genomic Data Infrastructure |
| SOP          | Standard Operating Procedure   |
| OC           | Operations Committee           |
| SDPC         | Security and Data Protection Committee |
| WG           | Working Group                  |
| 1+MG         | [1+ Million Genomes](https://framework.onemilliongenomes.eu/) |
| ORR          | Organisational Roles and Responsibilities |
| RFC          | Request For Comments           |
| TBD          | To Be Determined               |
| MB           | Management Board               |
| ISM          | Information Service Management |
| NCP          | Contact Point                  |
| EDIC         | European Digital Infrastructure Consortium |
| PR           | Pull Request                   |
| MS           | Milestone                      |
| WP           | Work Package                   |
| ZH           | ZenHub                         |
| GH           | GitHub                         |
| GDI-CO       | GDI Project Management Team ("GDI coordinators") |
| EBI          | European Bioinformatics Institute |
| EMBL         | European Molecular Biology Laboratory |
| IST          | Instituto Superior Técnico      |
| HRI          | Health Research Infrastructure |
| UU           | University of Uppsala          |
| NBIS         | National Bioinformatics Infrastructure Sweden |
| BEN          | Beneficiary                    |
| AE           | Associated Entity              |
| INSERM       | L'Institut national de la santé et de la recherche médicale (France) |
| DAC          | Data Access Committee          |
| AI           | Action Item                    |
| QMS          | Quality Management System      |
| DPbDD        | Data Protection by Design and Default |
| DP           | Data Protection                |
| DPA          | Data Processing Agreement      |
| KT           | Knowledge Transfer             |
| HD           | Helpdesk                       |
| UI           | User Interface                 |
| AAI          | Authentication and Authorization Infrastructure |
| VPN          | Virtual Private Network        |
| GDPR         | General Data Protection Regulation |

| **Term**     | **Definition**                 |
| ------------ | ------------------------------ |
| FitSM        | Standards for lightweight IT Services Management; developed initially through The FedSM Project, funded by the European Commission, now maintained by ITEMO (<https://www.fitsm.eu/>) |

## 3. Roles and Responsibilities
| Name         | GDI/Node Role      | Organisation  |
| ------------ | ------------------ | ------------- |
| **Author**   | Mallory Freeberg    | EMBL-EBI      |
| **Author**   | Marcos Casado Barbero | EMBL-EBI    |
| **Reviewer** | TBD                 |               |
| **Approver** | TBD                 |               |

## 4. Introduction
The [**European Genomic Data Infrastructure (GDI)**](https://gdi.onemilliongenomes.eu) project is a pioneering initiative aimed at **enabling access to genomic, phenotypic, and clinical data across Europe**. This access is crucial for advancing research, policymaking, and healthcare on a continental scale. Central to this mission is the 1+ Million Genomes (1+MG) network, which encompasses a diverse array of national human data-sharing projects, each at different stages of development.

Given the diversity of these projects, the **GDI serves as an essential platform for harmonizing operational practices through the development and alignment of Standard Operating Procedures** (SOPs). This harmonization not only facilitates the integration of well-established nodes but also provides critical guidance for those in the early stages of their development.

The governance model within the GDI network is designed to be both collaborative and flexible, **supporting the adoption of European-wide standards while accommodating the unique needs of individual nodes**. This dual approach is reflected in the structure of the GDI SOPs, which are divided into [**European-level SOPs**](../sops/european-level/) that provide standardized procedures applicable across all nodes, and [**Node-specific SOPs**](../sops/node-specific/) that allow for customization based on local requirements.

Through this Charter, the GDI underscores its commitment to fostering a unified yet adaptable operational environment, ensuring that all nodes, regardless of their current capabilities, can contribute to and benefit from this pan-European initiative.

## 5. Purpose of this Charter
The purpose of this document is to **define the scope and management of SOPs within the GDI network**. Specifically, it outlines how GDI SOPs will be managed to ensure consistency, quality, and relevance. This Charter serves as a foundational document within the GDI SOP quality management system, providing the necessary guidance and structure for the development, approval, and implementation of SOPs across the network.

## 6. Scope of GDI SOPs
The GDI is not a monolithic entity but a network of existing and emerging infrastructures. While SOPs can encompass various aspects of a team, node, or even project, this repository is not intended to cover every process within all institutions under the GDI umbrella. Instead, it contains SOPs that are relevant to GDI-specific use cases and are implemented by the nodes forming the GDI network.

For example, if a GDI node already functions as an archive with submitted datasets, the curation of these datasets, when outside the GDI scope, is not expected to follow a hypothetical "Dataset Curation SOP" from GDI.

Therefore, it is the **responsibility of the GDI nodes to implement these SOPs when the use case pertains to GDI infrastructure**, governance, or data.

## 7. GDI SOP Management
Given the diverse fields that GDI SOPs may cover, a well-defined set of roles and responsibilities is crucial for ensuring seamless operations across the network. These roles are involved at every step of the SOP lifecycle, from development to node implementation. The most up-to-date definitions of roles and responsibilities can be found [here](./GDI-SOP_organisational-roles-and-responsibilities.md#6-roles-and-responsibilities-definitions).

The process of adding a new SOP or editing an existing one is itself governed by established SOPs, such as the [GDI-SOP0007_SOP-template-creation.md](../sops/european-level/GDI-SOP0007_SOP-template-creation.md). **Repository maintainers must ensure that any changes are justified and consider their impact on both planned and existing GDI node features**. To facilitate this, the OC and SDPC include representatives from all GDI nodes across the three GDI pillars, ensuring that all are informed through mailing lists (see [GDI SOP Communication](#8-gdi-sop-communication)) about any SOP developments or changes. SOPs undergo rigorous review, approval, and authorization processes involving diverse GDI members to ensure quality and relevance.

Flexibility is also essential, ensuring that **GDI SOPs are strict enough to be followed and maintained while allowing GDI nodes the flexibility to implement them as needed**. The responsibility for maintaining the integrity of these implementations (i.e. being _similar enough_ to the templates) lies with the members of each node who participate in the OC/SDPC. This accountability framework allows for quick and flexible node implementation without imposing excessive constraints from the central GDI governance. For more information, refer to the [Roles and Responsibilities](./GDI-SOP_organisational-roles-and-responsibilities.md#6-roles-and-responsibilities-definitions), [GH management](./GDI-SOP_github-management.md) documentation, and the [summary diagram](../README.md#summary-diagram).

## 8. GDI SOP Communication
Effective communication is crucial within the GDI network to ensure that all nodes and pillars participate in the development and maintenance of SOPs. The following channels are used for transparent communication throughout the process:

- **Mailing Lists:** The OC and SDPC are kept informed throughout the process as the main maintainers of the repository and, by extension, the GDI SOPs. More information on these bodies can be found in the [MS10 document](https://docs.google.com/document/d/1Vr5ChMWpkO8LDVi9eGJv6LuegE4vjhHOJ1aISqWhAG4/edit#heading=h.wn4i2ajfycxg).
  - `gdi-oc [at] elixir-europe.org` - Operations Committee (OC)
  - `gdi-sdpc [at] elixir-europe.org` - Security and Data Protection Committee (SDPC)
  - `gdi-mb [at] elixir-europe.org` - Management Board (MB), used for the formal authorization of SOPs and governance decisions.

- **Slack Channels:** These are used for internal discussions related to the maintenance and management of SOPs within GDI.
  - [wp4-sop-discussions](https://gdi-elixir.slack.com/archives/C06RJQJNHFC)
  - [wp4-european_level_operations](https://gdi-elixir.slack.com/archives/C044GTS7JAV)

- **GitHub Forums:** These open discussion threads allow anyone with a GitHub account to participate or observe.
  - [**GitHub Issues**](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/issues): Used to request changes to existing SOPs or the addition of new ones.
  - [**GitHub Discussions**](https://github.com/GenomicDataInfrastructure/rfcs/discussions): RFCs are used to standardize significant changes to the GDI network, including SOPs. This step encourages community feedback during the SOP development and maintenance processes.

## 9. References

| Reference | Description |
| --------- | ----------- |
| [MS10](https://docs.google.com/document/d/1Vr5ChMWpkO8LDVi9eGJv6LuegE4vjhHOJ1aISqWhAG4/edit#heading=h.wn4i2ajfycxg) | Milestone 10 document containing the Committee Overview |
| [ORR](./GDI-SOP_organisational-roles-and-responsibilities.md) | Organisational Roles and Responsibilities |
| [GH management](./GDI-SOP_github-management.md) | Documentation on how GitHub is used as a platform for both GDI-level SOP development and GDI node implementation of SOPs |
| [GDI-SOP0007_SOP-template-creation.md](../sops/european-level/GDI-SOP0007_SOP-template-creation.md) | SOP containing steps to create more SOP templates in this repository |
