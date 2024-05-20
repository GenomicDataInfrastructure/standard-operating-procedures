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
    A[GDI project partners]
    A -->|Identify the need for a\n new GDI SOP| B
    B[GDI project partners]
    B -->|Write proposal of SOP.\n inc. purpose, scope, and justification of SOP| B2
    B2[GitHub Issue]
    B2 --> D
    D{1+MG Working\nGroup Approves\nproposal?}
    D -->|No| B
    D -->|Yes| E
    F[General GDI SOP Template]
    F -->|Is used by| E
    E[T4.3/WP4]
    E -->|Prepares template| G
    G[SOP Template]
    G --> H
    H[T4.3/WP4]
    H -->|Shares template| I
    

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
            nodeRep[Node's OC/SDPC representative]
            nodeRep --> |Nominate| nodeExp
            nodeExp[Node's experts]
        end
        subgraph Node's-SOP-development-process
            nodeDev(Template gets adapted\n with the node's needs)
            nodeDev --> nodeRev
            nodeRev(Review)
            nodeRev --> nodeApp
            nodeApp(Approval)
            nodeApp --> nodeAcc
            nodeAcc(Accessioning)
        end
        Node's-Roles -..->|Responsible for| Node's-SOP-development-process        
        nodeTem --> nodeDev
        nodeApp --> |Produces| nodeSOP
    end

    subgraph Authors
        I[Operations Committee - OC\nSecurity and Data Protection Committee - SDPC]
        I -->|Nominate|J
        J[Nominated experts]
    end

    I --> |Start development process| R
    Authors -..-> |Fill SOP content| L
    P -..->|Review SOP| M
    T -..->|Approve SOP|N
    U -..->|Authorize SOP| O
    R{Is SOP\na template?}
    R -->|Yes| Q
    R -->|No| S
    Q -->|Enters cycle|SOP-development-cycle
    S -->|Enters cycle|SOP-development-cycle

    subgraph SOP-development-cycle
        L(Content-filling)
        L --> M
        M(Review)
        M --> N
        N(Approval)
        N --> O
        O(Authorization)
        O --> zz(Finished Development cycle)
    end
    zz -->|Produces| V
    zz -->|Produces| W
    
    subgraph ORR-roles
        Authors
        P[Reviewers]
        T[Approvers]
        U[Authorizers\ne.g. Management Board - MB\ne.g. 1+MG Working Group]
    end

    V -->|Enters process| SOP-release-process
    W -->|Enters process| SOP-release-process
    SOP-release-process -->|Produces| ZA
    SOP-release-process -->|Produces| Z

    I -..->|Responsible for| SOP-release-process
    subgraph SOP-release-process
        Accessioning(SOP Accessioning)
        Accessioning --> GitHub-management
        GitHub-management
    end

    subgraph GitHub-management
        git1(Pull Request\nto main branch\nwith new SOP)
        git1 --> git2
        git2(PR approved)
    end

    %% Styles
    class S,V,ZA,nodeSOP SOP
    class G,F,Q,W,Z,nodeTem Template
````
