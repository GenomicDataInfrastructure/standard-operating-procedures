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

    %% Nodes
    B[GDI project partners]
    B -->|Write SOP proposal| B2
    B2[GitHub Issue]
    B2 --> E
    F[General GDI SOP Template]
    F -->|Is used by| E
    E[Operations Committee - OC\nSecurity and Data Protection Committee - SDPC]
    E -->|Prepares template| G
    G[SOP Template]
    G --> I

    %% Boxes
    subgraph European-level SOPs
        S[SOP Instance]
        V[Finished European-level\nSOP Instance]
        ZA[Released European-level\nSOP Instance]
    end

    ZA -->|Enters periodic\nreview cycle| ZA

    subgraph Node-specific SOPs
        Q[SOP Template]
        W[Finished Node-specific\nSOP Template]
        Z[Released Node-specific\nSOP Template]
        nodeRep[OC/SDPC Representatives\nfrom each node]
        Z -->|is used by| nodeRep
        subgraph Node's-GitHub
            nodeTem[Node-specific\nSOP Template]
            nodeSOP[Node-specific\nSOP Instance]
        end
        nodeRep -->|Copy SOP Template| Node's-GitHub
        subgraph Node's-Roles
            nodeRep[Node's OC/SDPC \n representative]
            nodeRep --> |Nominate| nodeExp
            nodeExp[Nominated experts]
        end
        subgraph Node's-SOP-development-process
            nodeDev(Template gets adapted\n with the node's needs)
            nodeDev --> nodeRev
            nodeRev(Review)
            nodeRev --> nodeApp
            nodeApp(Approval)
        end
        Node's-Roles -..->|Responsible for| Node's-SOP-development-process        
        nodeTem --> nodeDev
        nodeApp --> |Produces| nodeSOP
    end
    rev2[OC/SDPC] -..->|Approves \n changes| nodeApp

    I --> |Start development process| R
    Authors -..-> |Fill in SOP content| L
    Reviewers -..->|Review SOP| M
    Approvers -..->|Approve SOP|N
    Authorizers -..->|Authorize SOP| O
    R{Is SOP\na template?}
    R -->|Yes| Q
    R -->|No| S
    Q -->|Enters cycle|SOP-development-cycle
    S -->|Enters cycle|SOP-development-cycle

    subgraph SOP-development-cycle
        L(Drafting)
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
        aos-accessioning(SOP accessioning\n and formatting)
        aos-merge(PR against \n `dev` branch)
        subgraph SOP-release-process
            git1(Pull Request\nto `main` branch)
            git1 -->|Automatically \n triggers| git2
            git2(Zenodo release)
        end
    end
    aos-accessioning --> aos-merge

    subgraph ORR-roles
        Authors
        Reviewers
        Authorizers
        Approvers
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

    subgraph Authorizers
        authorizers1[Management Board]
        authorizers2[1+MG Working Group]
    end

    V -->|Enters process| SOP-release-process
    W -->|Enters process| SOP-release-process
    SOP-release-process -->|Produces| ZA
    SOP-release-process -->|Produces| Z

    resp1[OC/SDPC] -..->|Responsible for| Main-GitHub-repository

    %% Styles
    class S,V,ZA,nodeSOP SOP
    class G,F,Q,W,Z,nodeTem Template
````
