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
| v1      | Marcos Casado Barbero   | Filled in gaps, formatted file, added new sections, resolved comments | 19.08.2024 |
| v0      | Mallory Freeberg, Marcos Casado Barbero | Drafted charter | 26.03.2024 |

## 2. Glossary
The following table defines the abbreviations and terms relevant to GDI SOPs.

| Abbreviation | Description                                                         |
| ------------ | ------------------------------------------------------------------- |
| 1+MG         | [1+ Million Genomes](https://framework.onemilliongenomes.eu/)       |
| AAI          | Authentication and Authorization Infrastructure                     |
| AE           | Associated Entity                                                   |
| AI           | Action Item                                                         |
| BEN          | Beneficiary                                                         |
| DAA          | Data Access Agreement                                               |
| DAC          | Data Access Committee                                               |
| DMP          | Data Management Plan                                                |
| DP           | Data Protection                                                     |
| DPA          | Data Processing Agreement                                           |
| DPbDD        | Data Protection by Design and Default                               |
| DPIA         | Data Protection Impact Assessment                                   |
| EBI          | European Bioinformatics Institute                                   |
| EDIC         | European Digital Infrastructure Consortium                          |
| EMBL         | European Molecular Biology Laboratory                               |
| GDI          | European Genomic Data Infrastructure                                |
| GDI-CO       | GDI Project Management Team (GDI coordinators)                      |
| GDPR         | General Data Protection Regulation                                  |
| GH           | GitHub                                                              |
| HD           | Helpdesk                                                            |
| HRI          | Health Research Infrastructure                                      |
| INSERM       | L'Institut national de la santé et de la recherche médicale (France)|
| ISM          | Information Service Management                                      |
| IST          | Instituto Superior Técnico                                          |
| KT           | Knowledge Transfer                                                  |
| MB           | Management Board                                                    |
| MS           | Milestone                                                           |
| NBIS         | National Bioinformatics Infrastructure Sweden                       |
| NCP          | Node Contact Point                                                  |
| OC           | Operations Committee                                                |
| ORR          | Organisational Roles and Responsibilities                           |
| PR           | Pull Request                                                        |
| QMS          | Quality Management System                                           |
| RFC          | Request For Comments                                                |
| SDPC         | Security and Data Protection Committee                              |
| SOP          | Standard Operating Procedure                                        |
| TBD          | To Be Determined                                                    |
| UI           | User Interface                                                      |
| UU           | University of Uppsala                                               |
| VPN          | Virtual Private Network                                             |
| WG           | Working Group                                                       |
| WP           | Work Package                                                        |
| ZH           | ZenHub                                                              |

| **Term**     | **Definition**                 |
| ------------ | ------------------------------ |
| FitSM        | Standards for lightweight IT Services Management; developed initially through The FedSM Project, funded by the European Commission, now maintained by ITEMO (<https://www.fitsm.eu/>) |

## 3. Roles and Responsibilities
| Role       | Full name       | GDI/node role   | Organisation |
|------------|-----------------|-----------------|--------------|
| **Author**     | Mallory Freeberg | Task 4.3 member | EMBL-EBI |
| **Author**     | Marcos Casado Barbero | Task 4.3 member | EMBL-EBI |
| **Reviewer**   | Elisavet Torstensson | Task 4.3 member | UU / NBIS |
| **Approver**   | Erik Hedman | Task 4.3 member | UU / NBIS |
| **Approver**   | Markus Englund | Task 4.3 member | UU / NBIS |

## 4. Introduction
The [**European Genomic Data Infrastructure (GDI)**](https://gdi.onemilliongenomes.eu) project is a pioneering initiative that aims to **enable access to genomic, phenotypic, and clinical data across Europe**. This access is crucial for advancing research, policymaking, and healthcare on a continental scale. Central to this mission is the 1+ Million Genomes (1+MG) network, which encompasses a diverse array of national human data-sharing projects, each at different stages of development.

Given the diversity of these projects, the **GDI serves as an essential platform for harmonizing operational practices through the development and alignment of Standard Operating Procedures** (SOPs). This harmonization not only facilitates the integration of well-established nodes but also provides critical guidance for those in the early stages of their development.

The governance model within the GDI network is designed to be both collaborative and flexible, **supporting the adoption of European-wide standards while accommodating the unique needs of individual nodes**. This dual approach is reflected in the structure of the GDI SOPs, which are divided into [**European-level SOPs**](../sops/european-level/) that provide standardized procedures applicable across all nodes, and [**Node-specific SOPs**](../sops/node-specific/) that allow for customization based on local requirements.

SOPs will be **version controlled** in GitHub, with a single source of truth: this repository. Furthermore, through GitHub we expect to **collaboratively and transparently** develop and maintain the SOPs. By having the main repository public, yet allowing GDI nodes to privately make their implementations, we comply with the rule of thumb _as open as possible, yet as private as needed_. For further details, refer to the [GitHub management](./GDI-SOP_github-management.md) documentation.

Through this Charter, the GDI underscores its commitment to fostering a unified yet adaptable operational environment, ensuring that all nodes, regardless of their current capabilities, can contribute to and benefit from this pan-European initiative.

## 5. Purpose of this Charter
The purpose of this document is to **define the scope and management of SOPs within the GDI network**. Specifically, it outlines how GDI SOPs will be managed to ensure consistency, quality, and relevance. This Charter serves as a foundational document within the GDI SOP quality management system, providing the necessary guidance and structure for the development, approval, and implementation of SOPs across the network.

## 6. Scope of GDI SOPs
The GDI is not a monolithic entity but a network of existing and emerging infrastructures. While SOPs can encompass various aspects of a team, node, or even project, this repository is not intended to cover every process within all institutions under the GDI umbrella. Instead, it contains **SOPs that are relevant to GDI-specific use cases** and are implemented by the nodes forming the GDI network.

For example, if a GDI node already functions as an archive with submitted datasets, the curation of these datasets, when outside the GDI scope, is not expected to follow a hypothetical "Dataset Curation SOP" from GDI.

Therefore, it is the **responsibility of the GDI nodes to implement these SOPs when the use case pertains to GDI infrastructure**, governance, or data.

The scope of these SOPs is focused on roles, topics, and resources that are essential for establishing or operating node services, ensuring high-quality data management, and maintaining robust technical infrastructure. However, certain items are deliberately excluded from the current scope to maintain focus.

### In-Scope
#### Roles
- People **responding to and resolving user queries and issues** within the node (e.g. Helpdesk Staff and Operations Bioinformaticians)
- People focused on the **preparation, harmonization, and curation of data and metadata** to ensure high-quality data management (e.g. Data Stewards, Data Curators, and Bioinformaticians).
- People tasked with **designing, developing, implementing, deploying, and monitoring software and services** deployed at a node (e.g. Software Developers, Software Engineers, and DevOps Engineers)

#### Topics
- **Data Protection & Security**: Includes procedures related to security incident response, risk assessment, and compliance with data protection regulations (e.g., DPA, DAA, DPIA).
- **Data & Metadata Management**: Covers data management plans (DMPs), and processes for ensuring data quality and harmonization within the node, including interactions with the GDI User Portal.
- **Technical Infrastructure & Software Development**: Focuses on technical certifications, compliance assessment tools, and ensuring that node infrastructure meets GDI standards.
- **Helpdesk & Operations**: Encompasses standard operating procedures for helpdesk interactions with users, including interfacing with the GDI User Portal.

#### Resources
- **SOP Examples & Templates**: Provision of standardized templates for SOPs that can be adapted by nodes.
- **Operational Recommendations & Guidelines**: Guidance on best practices for operating node services within the GDI network.
- **Training on SOP Usage & Management**: Training materials and sessions to ensure that node staff can effectively implement and manage SOPs.
- **Resource Management Plan**: A plan for the management of resources required for SOP implementation.

### Out-of-scope
#### Roles
- **Users of Node Services**: While crucial to the broader GDI network, the specific operational procedures of end-users (e.g., researchers, clinicians, scientists, policy makers or data subjects) are not covered by these SOPs.
- **Training, Outreach, and Communications Officers**: These roles, while important, are not the focus of the current SOP scope.

#### Topics
- **Governance, Strategy & Sustainability**: These high-level topics, including aspects like GDI governance and long-term sustainability strategies, are beyond the scope of these SOPs.
- **User Training on Node Services**: Training materials and programs designed to educate users (researchers) on how to use node services are not covered.
- **Community Outreach & Engagement**: Activities related to building community engagement and outreach are excluded.

#### Resources
- **Node-Specific SOPs**: SOPs tailored to the unique needs of individual nodes are not included, as the focus is on providing standard templates and guidelines.
- **Training Materials for Users**: Resources designed for educating end-users (researchers) are out of scope.
- **Security Audits**: Formal security audits are not covered by the SOPs, although security procedures are included.

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
