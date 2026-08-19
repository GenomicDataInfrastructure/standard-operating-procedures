# European GDI - Node Helpdesk Ticket Classification

| Metadata | Value |
|---|---|
| Template SOP number | ``GDI-SOP0008`` |
| Template SOP version |  ``v1.0.0``  |
| Topic                | Helpdesk & operations |
| Template SOP Type | Node-specific SOP |
| GDI Node |  |
| Instance version |  |

## Index

1. [Document History](#1-document-history)

2. [Glossary](#2-glossary)

3. [Roles and Responsibilities](#3-roles-and-responsibilities)

4. [Purpose](#4-purpose)

5. [Scope](#5-scope)

6. [Introduction and Background Information](#6-introduction-and-background-information)

7. [Summary or Context Diagram](#7-summary-or-context-diagram)

8. [Procedure](#8-procedure)

9. [References](#9-references)

### 1. Document History

| Template Version | Instance version | Author(s) | Description of changes | Date |
|---|---|---|---|---|
| ``v1.0.1``  |  | Marcos Casado Barbero | Added dataset withdrawal tags from SOP0009 (see [PR](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/pull/62#discussion_r2891451676)) | 2026.03.10 |
|  ``v1.0.0``  |  | Elisavet Torstensson,  Silvia Bahena| Updated text formatting and clarified key points based on reviews (see [PR](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/pull/49)) | 2025.04.14 |
|  ``v0.0.0``  |  | Elisavet Torstensson, Mattias Strömberg, Silvia Bahena| Created the first version of the SOP | 2025.02.04 |

### 2. Glossary

Find GDI SOPs common Glossary at the [charter document](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_charter.md).

| Abbreviation |  Description |
|---|---|
| AF | Application Form|
| API | Application Programming Interface |
| DAA | Data Access Agreement|
| DAC | Data Access Committee|
| EBI | European Bioinformatics Institute |
| EGA | European Genome-phenome Archive |
| EMBL | European Molecular Biology Laboratory |
| FTP | File Transfer Protocol |
| GDI | Genomic Data Infrastructure |
| HD | Helpdesk |
| ID | Identity Document |
| ISM | Information Service Management |
| JSON | JavaScript Object Notation |
| NBIS | National Bioinformatics Infrastructure Sweden |
| NHD | Node Helpdesk |
| OK | All correct |
| ORR | Organisational Roles and Responsibilities |
| PR | Pull Request |
| RI | Research Infrastructure |
| SOP | Standard Operating Procedure |
| SP | Submitter Portal |
| UU | University of Uppsala |
| UX | User experience |
| VHD | Virtual Helpdesk  |
| XML | Extensible Markup Language  |

| Term | Definition |
|---|---|
| API | Application Programming Interface is a connection between computers or between computer programs. It is a type of software interface, offering a service to other pieces of software. |
| JIRA | is a software product developed by Atlassian that allows bug tracking, issue tracking and agile project management. |
| JSON | JavaScript Object Notation is an open standard file format and data interchange format that uses human-readable text to store and transmit data objects consisting of name–value pairs and arrays (or other serializable values).|
| Node Helpdesk | The support team responsible for handling tickets related to data management issues associated with the node in the GDI Project. |
| Ticket | A ticket is a record in a ticket management system that tracks an issue, request, or task from creation to resolution. It helps streamline communication and workflows within teams or organizations.|
| Ticket Classification | Process of categorizing tickets based on their type, urgency, or topic to ensure efficient handling and appropriate routing.  |
| Virtual Helpdesk  | Centralized, digital support service that coordinates and responds to incoming requests across the network. In GDI, it complements Node helpdesks by offering cross-node guidance, escalation, and harmonization of support efforts. |
| XML  | Extensible Markup Language is a markup language and file format for storing, transmitting, and reconstructing data. |

### 3. Roles and Responsibilities

See the qualifications and responsibilities of the roles in the [Organisational Roles and Responsibilities](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_organisational-roles-and-responsibilities.md) document.

| Role | Full name | GDI/node role | Organisation |
|---|---|---|---|
| Author | Elisavet Torstensson | Task 4.3 member  | UU-NBIS |
| Author | Mattias Strömberg | Task 4.3 member  | UU-NBIS |
| Author | Silvia Bahena | Task 4.3 member  | EMBL-EBI |
| Reviewer | Marcos Casado Barbero  | Task 4.3 Lead | EMBL-EBI  |
| Reviewer | Bianca Hendriksze  | Task 4.3 member | Health-RI  |
| Approver | Marcos Casado Barbero  |  Task 4.3 Lead  | EMBL-EBI  |
| Authorizer |  |  |  |

### 4. Purpose

Each GDI Node Helpdesk (NHD) provides support to its users by using a dedicated system (ticket management system) to respond to users with various issues or requests.

The purpose of this Standard Operating Procedure (SOP) is to provide clear guidelines for classifying tickets in a consistent and efficient manner in the node’s dedicated system. Proper ticket classification ensures that requests are routed to the appropriate teams, and prioritised accurately. This SOP aims to optimize resource allocation, improve response time and enhance overall customer satisfaction.

### 5. Scope

This SOP outlines the process for classifying tickets, at the **node level**, that were received from the Virtual Helpdesk (VHD). The approach is to use a classification model and register the tickets in the node's internal ticket management system. This SOP covers the steps between the initial reference of the ticket from the VHD, to its categorisation as a corresponding issue in the dedicated system.

### 6. Introduction and Background Information

This SOP applies to all tickets forwarded by the VHD that involve data management issues specific to the node. The NHD serves as the primary point of contact for addressing inquiries and requests received from the VHD concerning data management within the node. The NHD is responsible for collaborating with the VHD to ensure proper ticket classification, effective coordination, and timely resolution of these issues.

Below is defined the importance of creating custom tags for the ticket management system:

- **Classification and Prioritisation:** Tags help sort and prioritise tickets based on specific attributes or statuses.

- **Targeted Searches and Reports:** Tags enable precise filtering and custom reporting, focusing on relevant ticket aspects.

- **Enhanced Communication and Coordination:** Tags clarify ticket statuses and denote special handling requirements, improving team communication.

- **Streamlined Workflows:** Tags support automated workflows and ensure consistent ticket management practices.

- **Tracking and Reporting**: Tags aid in tracking performance metrics and analysing ticket trends for process improvements.	

- **Increased Efficiency:** Tags facilitate quick access to tickets and enable focused resolution of critical issues.

### 7. Summary or Context Diagram

This is a proposed workflow for how the ticket will be classified at the Node level.

````mermaid
flowchart TD
    subgraph Virtual_Helpdesk
        A[Ticket]
    end
    subgraph Node_Helpdesk
        A -->|Receive Ticket from VHD| B{Evaluate
                                        Ticket Scope}
        subgraph Ticket Management System
            C[Create Issue in Node Ticket Management System]
            F[Create 'Documentation' Issue in Node Ticket Management System]
        end                                        
        B -->|Positive Evaluation| C
        C --> D[Assign Tags: Type, Priority, Assignee, Status]
        D --> E[Follow NHD SOP for Ticket Handling]
        B -->|Negative Evaluation| F
        F --> D
    end
    E -->|Notify VHD of ticket resolution; for negative evaluations, inform them it’s out-of-scope.| Virtual_Helpdesk
   
````


### 8. Procedure

#### 8.1. Evaluating a Ticket from the VHD

| Step identifier | When | Who |
|:---|:---|:---|
| ``1`` | After receiving a ticket from the VHD and **within 7 working days** | Helpdesk officer  |

The NHD receives a ticket from the VHD requiring action by the specific node. Evaluate the ticket **within 7 working days** to determine whether it is **within the node's scope** (positive evaluation) **or not** (negative evaluation) based on your node's evaluation criteria.

- A ticket is considered **positively evaluated** if all the following criteria are met: 
   - ``< node's scope criteria 1>``
   - ``< node's scope criteria 2>``
   - ``< node's scope criteria 3>``
   - etc

   - If positively evaluated, proceed to **[step 2](#82--positive-evaluation---create-issue-in-node-ticket-management-system)**
  
- A ticket is considered **negatively evaluated** if any of the following criteria apply:
   - ``< node's scope criteria 1>``
   - ``< node's scope criteria 2>``
   - ``< node's scope criteria 3>``
   - etc

   - If negatively evaluated, proceed to **[step 3](#83--negative-evaluation---create-documentation-issue-in-node-ticket-management-system)**

#### 8.2.  Positive Evaluation - Create issue in Node Ticket Management System

| Step identifier | When | Who |
|:---|:---|:---|
|  ``2`` | After step 1, if the evaluation is positive, and **within 7 working days**| Helpdesk officer |

If the ticket is within the scope of the NHD (positive evaluation), follow your node's established procedure to create  **new issue** in the designated system, recording the ticket's arrival and documenting the positive evaluation. 

Proceed to [step 4](#84-assign-tags)

#### 8.3.  Negative Evaluation - Create Documentation issue in Node Ticket Management System 

| Step identifier | When | Who |
|:---|:---|:---|
| ``3`` | After step 1, if the evaluation is negative, and **within 7 working days** | Helpdesk officer |

If the ticket is out of the scope of the NHD (negative evaluation), follow your node's established procedure to create **new documentation issue** in the dedicated system, recording the ticket's arrival and documenting the negative evaluation.

Proceed to [step 4](#84-assign-tags)

#### 8.4. Assign Tags

| Step identifier | When | Who |
|:---|:---|:---|
| ``4`` | After creating a new issue in the Node Ticket Management System and **within 7 working days** | Helpdesk officer |

Once you create the issue in the Node Ticket Management System, the next step is to **assign tags**. 

If the evaluation of the ticket at [step 1](#81-evaluating-a-ticket-from-the-vhd) was **positive** then: 
- Proceed to [step 4.1](#841-choose-tags-for-positive-evaluation).

If the evaluation of the ticket at [step 1](#81-evaluating-a-ticket-from-the-vhd) was **negative** then: 
- Proceed to [step 4.2](#842-choose-tags-for-negative-evaluation).

##### 8.4.1 Choose tags for positive evaluation
| Step identifier | When | Who |
|:---|:---|:---|
| ``4.1`` | Following the creation of the issue after a positive ticket evaluation | Helpdesk officer |

Classify the ticket with **four tags** as described below: 

- [**Type of ticket**](#8411-type-of-ticket): Specifies the type of ticket.

- [**Ticket priority**](#8412-ticket-priority): Specifies the ticket's priority level.

- [**Ticket assignee**](#8413-ticket-assignee): Specifies who is responsible for resolving the ticket.

- [**Ticket status**](#8414-ticket-status): Specifies the ticket's status (initially set to "New").


###### 8.4.1.1 Type of ticket
| Step identifier | When | Who |
|:---|:---|:---|
| ``4.1.1`` | As part of step ``4.1`` | Helpdesk officer |

Below is a list of tags proposed for use by GDI NHDs to classify tickets by type. This list is derived from EGA’s internal Helpdesk system and is intended as a set of examples to provide guidance and inspiration.
	
Each node is encouraged to define and adapt its own set of tags based on the specific needs of its system or service. Nodes may select multiple tags if required for different scenarios.

### Archiving
| Tag | Definition |
|-----|------------|
| Archiving status | File is still processing in the archive |
| Data deposition - Archiving issue | Issue with archiving during deposition |
| Failed status | File has failed to archive |
### DAC
| Tag | Definition |
|-----|------------|
| DAC curation | We do DAC curation or update DAC members |
| DAC referred | User pointed back to DAC for access or clarification |
| DAC request  | DAC request |
| Update DAC | Contact and detail changes in DAC |
### Distribution
| Tag | Definition |
|-----|------------|
| File issues | Truncated or missing files from a dataset |
| Metadata issues | User asking for more info on metadata or its structure |
| Metadata query | User asking how to download or understand metadata |
### Download Issues
| Tag | Definition |
|-----|------------|
| API Download | Issue related to API-based download |
| Alternative Download | User cannot download using any of our tools |
| Dataset/file requesting issues | Problems requesting specific datasets/files |
| Datasets/files request not in client | Files not available with the download tool |
| Decryption/unzipping problems | Issues with decrypting or unzipping files |
| Download client issues | General issues with the download client |
| Firewall issues | Download issues caused by firewalls |
| Key request | Request for decryption keys |
| Log in problems | Problems logging into download client or portal |
| Null/Sleeping timeout errors | Timeout-related errors during download |
| User error | Errors due to user actions |
| Version issue | Problems due to client version |
### External Communications
| Tag | Definition |
|-----|------------|
| Journal communications | Communications with journals |
### Issue Tracking
| Tag | Definition |
|-----|------------|
| JIRA | To be used when you need to create a JIRA ticket for an issue that Helpdesk cannot resolve and requires dev involvement |
### Other
| Tag | Definition |
|-----|------------|
| Consortium | Tags related to different consortiums |
| Non - issue | User submitted a ticket but later said the issue was resolved |
### Scope & Feedback
| Tag | Definition |
|-----|------------|
| Documentation improvement | To be used when a user highlights our documentation is wrong/out of date/not clear |
| Interface issue | To be used when there is an issue with web pages |
| Out-of-scope | Issues that are out-of-scope of the nodes' helpdesk and are redirected to VHD if required|
| UX | Development feedback - to be used when a user provides feedback about service tools |
### Security
| Tag | Definition |
|-----|------------|
| GDI security issues | Security-related issues in GDI |
### Submission
| Tag | Definition |
|-----|------------|
| API - Submission | To be used when a submitter is using the submission API |
| Data deposition | User submitting data |
| Data deposition intention | To be used when initial submission request comes in |
| Data deposition policy documents | To be used when users query if their DAA is OK or ask questions about DAA |
| Data deposition problem | User having problems with data deposition |
| Data deposition question | General question about submission (not a problem) |
| Encryption Issue | User needs advice on file encryption |
| JSON submission issue | Issue related to JSON submission |
| Large submission | To be used if submission is over 10TB |
| Missing study/dataset on live | To be used when user highlights study/dataset is published but not released |
| Phenotype data | To be used for phenotype data submission |
| Post release change | To be used when user wants to update submission objects |
| Priority submission | Use in conjunction with consortium tags |
| Programmatic Submission problem | Programmatic submitters having issues with their XML |
| Publication ID query | When people are asking how to generate accession IDs for journal |
| Study/dataset release | Releasing a study/dataset to live site |
| Submitter portal issue | There is an issue with the Submitter Portal |
| Uploader issue | User is having issue with Aspera or FTP upload |
### Data withdrawal
| Tag | Definition |
|-----|------------|
| dataset-withdrawal-request | To be used when a user requests to withdraw a dataset from GDI |
| dataset-withdrawal | To be used for tickets related to dataset withdrawal |
### User Support
| Tag | Definition |
|-----|------------|
| Data query | User has a specific question about the data |
| General question | General questions about GDI |
| Non - user data request | User does not have access to a dataset and needs guidance |
| Password issue | User is having an issue with their password |
| User account-related issues | Issues related to user accounts |
 
###### 8.4.1.2 Ticket priority
| Step identifier | When | Who |
|:---|:---|:---|
| ``4.1.2`` | As part of step ``4.1`` | Helpdesk officer |

Use three priority levels as listed below. However, you may choose to implement other levels based on your node's preferences.

- **Low** - suitable for tickets that are not expected to be resolved quickly and which are of routine character

- **Medium** - suitable for tickets that are more complicated and might take longer time to resolve

- **High** - suitable for tickets that need to be handled immediately, e.g. security breaches

###### 8.4.1.3 Ticket assignee
| Step identifier | When | Who |
|:---|:---|:---|
| ``4.1.3`` | As part of step ``4.1`` | Helpdesk officer |

- Name of node helpdesk officer assigned to the ticket.
- Email address of the assigned person
- Additional helpdesk officers assigned to the issue

###### 8.4.1.4 Ticket status
| Step identifier | When | Who |
|:---|:---|:---|
| ``4.1.4`` | As part of step ``4.1`` | Helpdesk officer |

Use the model listed below. However, you may choose to implement a different model based on your node's preferences.

- **New** - ticket that has not yet been started to be resolved

- **In progress** (or opened) - ticket in the stage of being resolved

- **Resolved** - ticket that has been resolved and returned to the VHD

- **Blocked** - ticket that is unable to proceed with at the moment due to e.g. external dependencies

- **Deleted** - ticket that is archived e.g. since it is out of scope of the node HD
  

##### 8.4.2 Choose tags for negative evaluation
| Step identifier | When | Who |
|:---|:---|:---|
| ``4.2`` | Following the creation of the documentation issue after a negative ticket evaluation | Helpdesk officer |

When the ticket was evaluated negatively then, as the NHD, choose the following tags: 
-  **Type of ticket**: out-of-scope
-  **Ticket priority**: Select the appropriate priority level from the list
-  **Ticket assignee**: Select the assigned helpdesk member(s) and their email address from the list
-  **Ticket Status**: Deleted 

#### 8.5. Follow NHD SOP for Ticket Handling 
| Step identifier | When | Who |
|:---|:---|:---|
| ``5`` | After assigning tags | Helpdesk officer |

Once you have assigned the appropriate tags then proceed with the designated **SOP for Ticket handling** 
- If the ticket receives a **positive evaluation**, proceed to ``<your corresponding NHD SOP>``.
- If the ticket receives a **negative evaluation**, proceed to ``<your corresponding NHD SOP>``.

#### 8.6. Inform the VHD of Ticket Resolution 

| Step identifier | When | Who |
|:---|:---|:---|
| ``6`` | After the ticket handling  | Helpdesk officer |

Once the ticket has been handled and resolved according to the corresponding SOP, inform the VHD about the ticket resolution. 

When you resolve the issue (that had a **positive ticket evaluation**), send a brief notification to the VHD. Use the following template to draft your email (sent via the Node GDI email address) or to communicate through the node's designated system. Adjust the template content as needed for your specific case.

````
Subject: Notification of Ticket Resolution: <VHD's ticket ID>
````
````
Dear <VHD Officer>,

I am pleased to inform you that the referenced ticket <VHD's ticket ID> has been successfully resolved. It was reviewed and handled by <assigned helpdesk member(s)> with a priority status of <priority status> and classified as <type of ticket>.

As a result, the ticket will be considered resolved and closed. However, if additional details or feedback are provided, it can be reopened for further review.

Please do not hesitate to contact me with any questions or concerns. 

Thank you for your cooperation and support.

Best regards,  
<Name of NHD Officer>  
<GDI Node>
````

If the documentation issue is **out of NHD's scope**, send a brief explanation of this decision to the VHD. Use the following template to draft your email (sent via the Node GDI email address) or to communicate through the node's designated system. Adjust the template content as needed for your specific case.
````
Subject: Notification of Ticket Status: <VHD's ticket ID> - Out of Scope for <GDI Node Helpdesk>
````
````
Dear <VHD officer>,

Following a careful evaluation and in accordance with our established procedures, we have determined that the referenced ticket <VHD's ticket ID>, handled by the <assigned helpdesk member(s)>, with a <priority status> falls outside of the scope of our node helpdesk. This conclusion has been reached for the following reason(s).

<Reason(s)>

As a result, we will consider the ticket resolved and closed unless further input or objections are raised. Should additional details or feedback be provided, the ticket can be reopened for further review. 

Please do not hesitate to contact me with any questions or concerns. 

Best regards,
<Name of NHD officer>
<GDI node>

````


### 9. References

| Reference | Description |
|---|---|
|  [1](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_charter.md) | European GDI - SOP Charter (including Glossary) |
| [2](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_information-service-management.md) | European GDI - Procedures for Information Service Management (ISM) for SOPs |
| [3](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_organisational-roles-and-responsibilities.md) | European GDI - Organisational Roles and Responsibilities (ORR) |
