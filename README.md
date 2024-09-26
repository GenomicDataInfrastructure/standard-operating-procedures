# standard-operating-procedures

Welcome! ☀️ This GitHub repository contains resources managing standard operating procedure (SOP) resources for the GDI project. We use this repository to manage SOP resources so that changes can be made and reviewed easily, issues and requests can be logged, and so we can ensure consistency and clarity across node operations.

## Where can I find the SOP materials?

To-do

## How do I add or change SOP materials?

To-do

## How do I report an issue with SOP materials?

To-do

## Summary diagram
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

    ZA -->|Enters periodic<br>review cycle| ZA

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
    
    %% Styles
    class S,V,ZA,nodeSOP,l_sopInstance SOP
    class G,F,Q,W,Z,nodeTem,l_sopTemplate Template
    class B2,l_start start
````
