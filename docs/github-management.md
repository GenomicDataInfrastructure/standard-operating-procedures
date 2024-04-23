# Copying GDI SOP repository
The GDI SOP repository ([**GenomicDataInfrastructure/standard-operating-procedures**](https://github.com/GenomicDataInfrastructure/standard-operating-procedures)) contains both European-level SOP _instances_ and Node-specific SOP _templates_. In order to adapt the Node-specific SOP templates, GDI nodes are expected to make a copy of this GitHub repository and modify them to suit them to their needs.

Given that the base repository is public, forks of this repository cannot be private. Therefore, making a node's copy of the repository can be done in different ways, explained in this document, depending on the level of privacy that each node may require:
- **Public node's repository**. If the node does not require for a private repository, copying the source repository is straightforward. See section _[1. Public repository](./github-management.md#1-public-repository)_.
- **Private node's repository**. On the contrary, if nodes need their SOP instances to be private (e.g. for security reasons), an alternative route is taken. See section _[2. Private repository](./github-management.md#2-private-repository)_.

````mermaid
flowchart TD
    A[Source Repository] 
    dec{Node's repo\nprivacy}
    A --> dec
    dec -->|Public| B(Fork public repository)
    dec -->|Private| C(Import)    
    H[Work with node's\n repository]
    F --> H
    B --> H[Work with node's\n repository]
    subgraph Public Path
        B
    end
    subgraph Private Path
        C(Import) --> E(Add Upstream Remote)
        E --> G(Disable Push to Upstream)
        E --> F(Sync with Upstream)
    end
````

## 1. Public repository
Here, we provide step-by-step instructions for **forking** a GitHub repository using GitHub's user interface.

### 1.1 Creating a fork repository

1. Open [GitHub](https://github.com/) and log in to your account.
1. Go to [GDI SOP repository](https://github.com/GenomicDataInfrastructure/standard-operating-procedures) page.
1. Click the "Fork" button in the upper-right corner of the repository page.
1. Provide the details of your forked repository: 
    - Choose as owner your GitHub account or organization to create the fork. This repository will be your node's instance of the ``standard-operating-procedures``. Therefore, we recommend you to use your organization's namespace (similar to [GenomicDataInfrastructure](https://github.com/GenomicDataInfrastructure) but for your specific organization), as the repository ``Owner``, instead of your own username. 
    - Provide the name and description that you see fit. We recommend to use the default ones.
1. Click on "Create fork" and wait a few moments.

### 1.2 Work with Your Fork
1. Navigate to your forked repository. It will have your username or organization name at the beginning of the URL (``https://github.com/<your-username>/standard-operating-procedures``).
1. Clone the fork to your local machine:
    ````bash
    git clone https://github.com/<your-username>/standard-operating-procedures.git
    cd standard-operating-procedures
    ````
    Remember to replace ``<your-username>`` with the correct name.
1. Start making changes to the existing SOP Templates, the [node-specific](../sops/node-specific/), creating your node's instance of the SOPs to make them useful for your node.

## 2. Private repository

This rubric guides project partners through the steps to create a private repository from a public GitHub repository and maintain synchronization with the original source.

### 2.1 Create a Private Repository

1. Open [GitHub](https://github.com/) and log in to your account.
1. Click on "[New Repository](https://github.com/new)".
1. Click on "[Import a repository](https://github.com/new/import)".
1. Follow the instructions to import a repository:
    1. Enter the URL of the **source repository**:
        ```markdown
        https://github.com/GenomicDataInfrastructure/standard-operating-procedures
        ```
    1. Enter the details of the **new repository**. 
        - This repository will be your node's instance of the ``standard-operating-procedures``. Therefore, we recommend you to use your organization's namespace (similar to [GenomicDataInfrastructure](https://github.com/GenomicDataInfrastructure) but for your specific organization), as the repository ``Owner``, instead of your own username. 
        - You can choose any name for the new repository (recommended: ``standard-operating-procedures``)
        - Choose "Private" as your new repository's privacy level. Otherwise, we advise you to follow section _[1. Public repository](./github-management.md#1-public-repository)_.
    
        Since the source repository is public, no credentials are needed to copy it.
1. Click "Begin Import". Wait for a few moments while GitHub imports the repository.

### 2.3 Add Upstream Remote and Disable Pushing
Once your repository has been imported, we are ready to set the source repository as the upstream remote. This is for your repository (called ``origin``) to track changes in the source repository (called ``upstream``):
1. **Clone your new private repository** to your local machine:
    ````bash
    git clone https://github.com/<your-username>/standard-operating-procedures.git
    cd standard-operating-procedures
    ````
    Remember to replace ``<your-username>`` with either your organization's namespace or your GitHub username, whichever you used as "Owner" when importing.
1. Add the public repository as an upstream remote:
    ````bash
    git remote add upstream https://github.com/GenomicDataInfrastructure/standard-operating-procedures.git
    ````
1. Disable pushing to the upstream repository to avoid accidental changes to the public repository:
    ````bash
    git remote set-url --push upstream no_push
    ````

### 2.4 Sync with Upstream
Whenever there are changes in the source repository, you can sync your node's repository:
1. Fetch updates from the public repository (upstream):
    ````bash
    git fetch upstream
    ````
1. Merge or rebase the changes from the upstream repository. If there are conflicts, we advise you to resolve them them manually.
    1. Merge:
        ````bash
        git merge upstream/main --no-edit
        ````
    1. Rebase:
        ````bash
        git rebase upstream/main
        ````
### 2.5 Work with your private copy
You are ready to make any changes the existing SOP Templates, the [node-specific](../sops/node-specific/), creating your node's instance of the SOPs to make them useful for your node.