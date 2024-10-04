# Genomic Data Infrastructure (GDI) Standard Operating Procedures (SOPs)

Welcome to the GDI Standard Operating Procedures (SOPs) repository! ☀️ This repository is the **central hub for the creation, management, and dissemination of SOPs for the European Genomic Data Infrastructure (GDI) project**. We aim to standardize and harmonize operational procedures across GDI nodes to ensure interoperability and compliance.

This repository is publicly accessible, but GDI nodes may also maintain their own forks or cloned versions with node-specific SOP implementations.

## SOP Materials

All SOP documents are stored in the `sops/` folder. The SOPs are categorized as:
- **European-level SOPs**: SOPs that can be implemented across all GDI nodes.
- **Node-specific SOP templates**: SOP Templates that can be adapted by individual nodes based on their specific needs.

An up-to-date index of all released SOPs, along with their metadata, can be found in the [index table](sops/README.md).

## Releases and Versioning

The **[``main`` branch](https://github.com/GenomicDataInfrastructure/standard-operating-procedures) of this repository always contains the latest version of released SOPs**. Furthermore, if you require access to a snapshot of previous SOP releases, you have the following at your disposal:
- **GitHub Releases**: Static versions of the SOP repository are tagged and available through [GitHub releases](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/releases).
- **Zenodo Submissions**: Each GitHub release is automatically submitted to the GDI Zenodo community, where a DOI (i.e., a permanent identifier) is assigned for the SOP bundle. You can explore the releases via [Zenodo GDI community](https://zenodo.org/communities/gdi/records).

For more information on the release process and DOI minting, please refer to the [SOP Accessioning Documentation](docs/GDI-SOP_sop-accessioning.md#sop-releases-and-doi-minting).

## How to Contribute

We welcome contributions from all GDI members and the wider community. If you want to **request changes, propose new SOPs, or directly contribute to the repository**, please check out our [**CONTRIBUTING guide**](CONTRIBUTING.md).

## Key Documents
More documentation is available within the ``docs`` directory. For detailed information about the SOP framework, processes, and roles within the GDI project, please refer to the **[Charter](docs/GDI-SOP_charter.md)**, the **[Information Security Management (ISM)](docs/GDI-SOP_information-service-management.md)** and **[Organisational Roles and Responsibilities (ORR)](docs/GDI-SOP_organisational-roles-and-responsibilities.md)**.

## Reporting Issues

If you encounter any issues or have suggestions for improvements to existing SOPs, **feel free to open an issue on GitHub**. Simply go to the [Issues](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/issues) section and use the appropriate template to describe the problem.

## Diagram Overview
Below is a detailed overview of the SOP development and management process:
````mermaid
flowchart TB
    %% Colors
    classDef SOP fill:#FFD700,stroke:#000000,stroke-width:2px;
    classDef Template fill:#87CEEB,stroke:#000000,stroke-width:2px;
    classDef start fill:#e8daef,stroke:#c0392b,stroke-width:2px;

    %% Nodes

    subgraph Diagram-Legend
        subgraph Colour-coding
            l_sopTemplate[SOP Template]
            l_sopInstance[SOP Instance]
            l_start[Diagram start]
        end        
        subgraph Abbreviations
            l_oc[**OC**: Operations Committee]
            l_spdc[**SDPC**: Security and Data Protection Committee]
            l_GDI[**GDI**: European Genomic Data Infrastructure]
            l_SOP[**SOP**: Standard Operating Procedure]
        end
    end    
    B[GDI project partners]
    B -..->|Write SOP proposal| B2
    checkValid{Valid request?}
    B2 -->|Request<br>is evaluated| checkValid
    sopPreparation(Document Preparation)
    checkValid -->|Yes|sopPreparation
    checkValid -->|No|B2
    Repository-maintainers -..->|Maintains| Main-GitHub-repository
    F -..->|Is used by| sopPreparation
    sopPreparation -->|Outputs| G
    G[SOP Template]
    G -->|Is taken by| I

    %% Boxes
    subgraph European-level SOPs
        S[SOP Instance draft]
        V[Finished European-level<br>SOP Instance]
        ZA[Released European-level<br>SOP Instance]
    end

    ZA -->|Enters| review_e
    subgraph European-Review-cycle
        review_e[Periodic SOP<br> content review]
        review_e -->|Determines| revision_e
        revision_e{Is revision<br>required?}
    end
    revision_e -->|No| review_e
    revision_e -->|Yes| SOP-development-cycle

    subgraph Node-specific SOPs
        Q[SOP Template draft]
        W[Finished Node-specific<br>SOP Template]
        Z[Released Node-specific<br>SOP Template]
        nodeRep[OC/SDPC Representatives<br>from each node]
        Z -->|is used by| nodeRep
        subgraph Node's-GitHub
            nodeTem[Node-specific<br>SOP Template]
            nodeSOP[Node-specific<br>SOP Instance]
        end
        nodeRep -->|Copy SOP Template| Node's-GitHub
        subgraph Node's-Roles
            nodeRep[Node's OC/SDPC <br> representative]
            nodeRep --> |Nominate| nodeExp
            nodeExp[Nominated<br>experts]
        end
        subgraph Node's-SOP-development-process
            nodeDev(Template gets adapted<br> with the node's needs)
            nodeDev --> nodeRev
            nodeRev(Review)
            nodeRev --> nodeApp
            nodeApp(Approval)
        end
        Node's-Roles -..->|Responsible for| Node's-SOP-development-process        
        nodeTem --> nodeDev
        nodeApp --> |Produces| nodeSOP
        nodeSOP -->|Enters| review_n
        
        subgraph Node's-Review-cycle
            review_n[Periodic SOP<br> content review]
            review_n -->|Determines| revision_n
            revision_n{Is revision<br>required?}
        end
        revision_n -->|No| review_n
        revision_n -->|Yes| nodeDev
    end
    nodeRep -..->|Approves <br> changes| nodeApp

    I --> |Start development process| R
    Authors -..-> |Fill in SOP content| L
    Reviewers -..->|Review SOP| M
    Approvers -..->|Approve SOP|N
    Authorizers -..->|Authorize SOP| O
    R{Type of SOP?}
    R -->|Node-specific| Q
    R -->|European-level| S
    Q -->|Enters cycle|SOP-development-cycle
    S -->|Enters cycle|SOP-development-cycle

    subgraph SOP-development-cycle
        L(Fill in content)
        L --> M
        M(Review)
        M --> N
        N(Approval)
        N --> O
        O(Authorization)
    end
    O --> aos-accessioning
    aos-merge -->|Produces| V
    aos-merge -->|Produces| W

    subgraph Main-GitHub-repository
        B2[GitHub Issue]
        F[General GDI SOP Template]
        aos-accessioning(SOP accessioning<br> and formatting)
        aos-merge(PR against <br> &apos;dev&apos; branch)
        subgraph SOP-release-process
            git1(Pull Request<br>to &apos;main&apos; branch)
            git1 -->|Branch is<br>used for| git2
            git2(GitHub release)
            
        end
    end
    git3(Zenodo release)
    git2 -->|Automatically <br> triggers| git3
    aos-accessioning --> aos-merge

    subgraph ORR-roles
        Authors
        Reviewers
        Authorizers
        Approvers
        Trainers
        Node-maintainers
        Repository-maintainers
    end

    subgraph Authors
        I[OC/SDPC]
        I -->|Nominate|J
        J[Nominated experts]
    end

    subgraph Reviewers
        reviewers1[GDI members]
    end

    subgraph Approvers
        approvers1[OC/SDPC]
    end

    subgraph Trainers
        t_authors[SOP Authors]
        t_experts[Nominated<br>experts]
    end

    subgraph Node-maintainers
        n_maintainers[Node's OC/SDPC<br>representative]
        n_experts[Nominated<br>experts]
    end
    Node-maintainers -..->|Are| Node's-Roles

    subgraph Repository-maintainers
        ocsdpc[OC/SDPC]
    end

    subgraph Authorizers
        authorizers1[Management Board]
        authorizers2[1+MG Working Group]
    end

    V -->|Enters process| SOP-release-process
    W -->|Enters process| SOP-release-process
    SOP-release-process -->|Produces| ZA
    SOP-release-process -->|Produces| Z

    SOPtraining[SOP Training]
    nodeSOP --> SOPtraining
    ZA --> SOPtraining
    Trainers -..-> |Provides|SOPtraining
    revision[Revision is due]
    
    %% Styles
    class S,V,ZA,nodeSOP,l_sopInstance SOP
    class G,F,Q,W,Z,nodeTem,l_sopTemplate Template
    class B2,l_start start
````
