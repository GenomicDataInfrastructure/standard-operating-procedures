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
1. [GDI References](#9-references)

## 1. Document History
| Version | Author(s) | Description of changes            | Date |
| ------- | --------- | --------------------------------- | ---- |
| v1      | Marcos Casado Barbero | Filled in the gaps, formatted file, added new sections, resolved comments... | 12.08.2024 |
| v0      | Mallory Freeberg, Marcos Casado Barbero | Drafted charter | 26.03.2024 |


## 2. Glossary
Find abbreviations and term definitions relevant to GDI-SOPs in the tables below.

| Abbreviations | Description                    |
| ------------- | ------------------------------ |
| GDI           | European Genomic Data Infrastructure |
| SOP           | Standard Operating Procedure   |
| OC            | Operations Committee           |
| SDPC          | Security and Data Protection Committee |
| WG            | Working Group                  |
| 1+MG          | [1+ Million Genomes](https://framework.onemilliongenomes.eu/) |
| ORR           | Organisational Roles and Responsibilities |
| RFC           | Request For Comments           |
| TBD           | To Be Determined               |
| MB            | Management Board               |
| ISM           | Information Service Management |
| NCP           | Contact Point |
| EDIC          | European Digital Infrastructure Consortium |
| PR            | Request |
| MS            | Milestone |
| WP            | Work Package |
| ZH            | ZenHub |
| GH            | GitHub |
| GDI-CO        | GDI Project Management Team ("GDI coordinators") |
| EBI           | European Bioinformatics Institute    |
| EMBL          | European Molecular Biology Laboratory    |
| IST           | Instituto Superior Técnico    |
| HRI           | Health Research Infrastructure |
| UU            | University of Uppsala |
| NBIS          | National Bioinformatics Infrastructure Sweden |
| BEN           | Beneficiary |
| AE            | Associated Entity |
| INSERM        | L'Institut national de la santé et de la recherche médicale (France) |
| DAC           | Data Access Committee |
| AI            | Action Item |
| QMS           | Quality Management System |
| DPbDD         | Data Protection by Design and Default |
| DP            | Data Protection |
| DPA           | Data Processing Agreement |
| KT            | Knowledge Transfer |
| HD            | helpdesk |
| UI            | user interface |
| AAI           | authentication and authorisation infrastructure |
| VPN           | Virtual Private Network |
| GDPR          | General Data Protection Regulation |

| **Term**      | **Definition**                 |
| ------------- | -------------------------------|
| FitSM         | Standards for lightweight IT Services Management; developed initially through The FedSM Project, funded by the European Commission, now maintained by ITEMO (<https://www.fitsm.eu/>). |

## 3. Roles and Responsibilities
| Name           | GDI / node role  | Organisation |
| -------------- | ---------------  | ------------ |
| **Author**     | Mallory Freeberg | EMBL-EBI    |
| **Author**     | Marcos Casado Barbero | EMBL-EBI    |
| **Reviewer**   |  TBD |              |
| **Approver**   |  TBD |              |

## 4 Introduction
The **[European Genomic Data Infrastructure (GDI)](https://gdi.onemilliongenomes.eu) project** is a transformative initiative designed to facilitate access to genomic, phenotypic, and clinical data across Europe, thereby advancing research, policymaking, and healthcare. Central to this mission is the 1+ Million Genomes (1+MG) network, which comprises a diverse array of national human data sharing projects, each at varying stages of maturity.

Given the heterogeneity of these projects, the GDI serves as a crucial platform for **harmonizing operational practices, particularly through the development and alignment of Standard Operating Procedures (SOPs)**. This alignment not only supports the integration of well-established nodes but also provides essential guidance to those in the early stages of development.

The governance model within the GDI network is both collaborative and flexible, allowing for the **adoption of European-wide standards while accommodating the unique needs of individual nodes**. This dual approach is reflected in the structure of the GDI SOPs, which are divided into [**European-level SOPs**](../sops/european-level/) that offer standardized procedures applicable across all nodes, and [**Node-specific SOPs**](../sops/node-specific/) that provide a framework for customization based on local requirements.

Through this Charter, the GDI underscores its commitment to fostering a unified yet adaptable operational environment, ensuring that all nodes, regardless of their current capabilities, can contribute to and benefit from this pan-European initiative.

## 5. Purpose of this Charter

This document aims to provide directions for the scope of SOPs which guide the operation of nodes within GDI. More specifically, this document defines how GDI SOPs will be managed to ensure consistency, quality, and usefulness. It serves as a high-level document which will be supported by further resources. Thus, it is fundamental to the GDI SOP quality management system as an initiation document.

## 6. Scope of GDI SOPs
As mentioned above, GDI is not made out of a single blueprint, but a network of existing and emerging infrastructures. SOPs can encompass all aspects of a team, node or even project, yet it is not intended for this repository to englobe every single possible process for all institutions under the GDI flag. Instead, this repository is to **contain a set of SOPs that apply to GDI use-cases**, implemented by the nodes that form GDI, but not to all existing processes in these nodes.

For example, if a GDI node already had submitted datasets and was acting as an archive, the curation of these datasets that may be outside of the GDI space is not expected to follow a hypothetical "Dataset curation SOP" from GDI.

Therefore, it is **the responsibility of those implementing the SOPs, the GDI nodes themselves, to apply them when the use-case concerns GDI**, its infrastructure, governance, or data.

## 7. GDI SOP Management
With the amount of fields that the SOPs may cover, and in order for a heterogeneous network of nodes to work seamlessly, there needs to be a **defined set of roles and their responsibilities**. These actors are involved at every step of the SOP life-cycle, from development to node implementation. Find the up-to-date Roles and Responsibilities at their **definition [here](./GDI-SOP_organisational-roles-and-responsibilities.md#6-roles-and-responsibilities-definitions)**.

Adding a new SOP or editing an existing one is a process in itself, and they are defined in their own SOPs: [GDI-SOP0007_SOP-template-creation.md](../sops/european-level/GDI-SOP0007_SOP-template-creation.md). Maintainers of this GH repository need to **make sure that these changes are justified**, and to **take into account the impact** that they would have on planned and existing features of GDI nodes. In order to do so, the OC and SDPC of GDI contain representation of all GDI nodes across the three GDI pillars, and all are to be informed through mailing lists (see [GDI SOP communication](#8-gdi-sop-communication)) about the development or changes in all SOPs at GDI level. It is for this reason that SOPs go through review, approval and authorization steps, involving multiple and diverse GDI members.

It is also a necessity to reach the point of flexibility where GDI SOPs are **strict enough to be easily followed and maintained**, but **allow for GDI nodes to implement them as needed**. Thus, the SOPs implemented by a GDI node need to be _similar enough_ to the templates that were released in this repository. In order not to constraint GDI nodes, this **responsibility lies on the members of each node that belong to the OC/SDPC**. This accountability layer through internal node approval allows for a quick and flexible node implementation without imposing too many constraints by the main GDI governance. In this repository you can find more information about their [responsibilities](./GDI-SOP_organisational-roles-and-responsibilities.md#6-roles-and-responsibilities-definitions), [GH management](./GDI-SOP_github-management.md) for main and nodes' repositories, and a visual representation of at the main [diagram](../README.md#summary-diagram)

## 8. GDI SOP Communication
Communication is key within the GDI network of nodes and representatives. In order for every node, and every pillar, to be part of the development and maintenance of GDI SOPs, any communication must be transparent. See below channels for communication that are used throughout this process:

- **Mailing lists**. The OC and SDPC are constantly informed throughout the process, as the main maintainers of the repository and, therefore, the GDI SOPs. Find more about these bodies at the [MS10 document](https://docs.google.com/document/d/1Vr5ChMWpkO8LDVi9eGJv6LuegE4vjhHOJ1aISqWhAG4/edit#heading=h.wn4i2ajfycxg).
   - ``gdi-oc [at] elixir-europe.org``. Operations Committee (OC).
   - ``gdi-sdpc [at] elixir-europe.org``. Security and Data Protection Committee (SDPC).
   - ``gdi-mb [at] elixir-europe.org``. Management Board (MB). Used for formal authorization of SOPs and governance decisions.

- **Slack channels**. Use them for internal (to GDI) discussions regarding the maintenance and management of SOPs.
   - [wp4-sop-discussions](https://gdi-elixir.slack.com/archives/C06RJQJNHFC)
   - [wp4-european_level_operations](https://gdi-elixir.slack.com/archives/C044GTS7JAV)

- **GH forums**. These are open discussion threads where anyone with a GH account can participate or observe.
   - [**GH Issues**](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/issues). GH Issues at this repository are used to request changes to existing SOPs or the addition of new ones.
   - [**GH Discussions**](https://github.com/GenomicDataInfrastructure/rfcs/discussions). RFCs are used to standardize substantial changes to the GDI network, including SOPs. It is essentially another step to bring feedback from the community during the development and maintenance of SOPs.

## 9. References

| References | Description |
| ---------- | ----------- |
| [MS10](https://docs.google.com/document/d/1Vr5ChMWpkO8LDVi9eGJv6LuegE4vjhHOJ1aISqWhAG4/edit#heading=h.wn4i2ajfycxg) | Milestone 10 document containing the Committee Overview |
| [ORR](./GDI-SOP_organisational-roles-and-responsibilities.md) | Organisational Roles and Responsibilities |
| [GH management](./GDI-SOP_github-management.md) | Documentation on how GH is used as a platform for both GDI-level SOP development and GDI node implementation of SOPs |
| [GDI-SOP0007_SOP-template-creation.md](../sops/european-level/GDI-SOP0007_SOP-template-creation.md) | SOP containing steps to create more SOP templates in this repository |