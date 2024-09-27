# European GDI - 1+MG DAC Approval Process

| Metadata               | Value                                            |
|------------------------|--------------------------------------------------|
| Template SOP number    | ``GDI-SOP0003``                                  |
| Template SOP version   | ``v1``                                           |
| Topic                  | Data & metadata management                       |
| Template SOP Type      | European-Level SOP                               |
| GDI Node               |                                                  |
| Instance version       |                                                  |

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

| Template Version | Instance version | Author(s)         | Description of changes           | Date       |
|------------------|------------------|-------------------|----------------------------------|------------|
| ``v1``               |                  | Marcos Casado Barbero    | Transform document to markdown and complete version | ``2024.09.27`` |
| ``v0``               |                  | Dylan Spalding    | First version of SOP drafted     | ``2024.04.11`` |

### 2. Glossary
Find GDI SOPs common Glossary at the [**charter document**](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_charter.md).

| Abbreviation | Description                                                                                               |
|--------------|-----------------------------------------------------------------------------------------------------------|
| DAC          | Data Access Committee, responsible for reviewing access requests and approving or denying the requests     |
| EDIC         | European Digital Infrastructure Consortium, will serve as the DAC for managing access requests to data in GDI |
| NCP          | National Coordination Point                                                                               |

| Term          | Definition                                                                                                |
|---------------|-----------------------------------------------------------------------------------------------------------|
| | |

### 3. Roles and Responsibilities
See the qualifications and responsibilities of the roles at the [**Organisational Roles and Responsibilities**](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_organisational-roles-and-responsibilities.md) document.

| Role       | Full name             | GDI/node role           | Organisation |
|------------|-----------------------|-------------------------|--------------|
| Author     | Dylan Spalding        | Finland / Pillar II co-lead | CSC          |
| Author     | Marcos Casado Barbero | Task 4.3 Lead | EMBL-EBI          |
| Reviewer   | Regina Becker | LU / Pillar I co-lead | LNDS |
| Approver   | _#! TO-DO_         |    |          |
| Authorizer | _#! TO-DO_         |    |          |

### 4. Purpose
To access controlled access data within the European Genomic Data Infrastructure a research user must apply for authorisation to access the data from the 1+ Million Genomes Data Access Committee (DAC). The 1+MG DAC (EDIC) will check and review the application, making sure it conforms to the requirements in the 1+MG Data Governance, and if so, make a recommendation to the National Coordination Point(s) (NCP) who can agree or disagree with the recommendation.

### 5. Scope
This SOP covers the point at which a data access application is received by the 1+MG DAC to the point at which the 1+MG approves or rejects the application. The input is a completed application form, and the output is a notification of approval or rejection of the request for authorisation to access the controlled access data described in the application.

### 6. Introduction and Background Information
The 1+MG DAC is tasked with recommending (to the relevant NCP) the approval or rejection of requests for the authorisation to access data held within the GDI. Additionally the 1+MG DAC will follow a review process when the NCP disagrees with the 1+MG DACs recommendation (Ref. GDI-SOP00002). Once the 1+MG DAC and relevant NCP(s) agree, or the associated review process completes, the data user will be informed of the decision to approve or reject their application for authorisation to access the data described within the application. 

### 7. Summary or Context Diagram
The whole workflow is described step-by-step in section 8.

### 8. Procedure
#### 1. Initiate application check
| Step identifier | When                                       | Who          |
|-----------------|--------------------------------------------|--------------|
| 1               | On receipt of notification of a new data access authorisation application | 1+MG DAC     |

The application will be checked, based on the requirement in the Data Governance document. The application form, which is used to help the data requester enter valid and complete information for the application, must be checked to ensure that:
- Confirm the research has institutional sign off [6],
- The data analysis plan is present and suitable for the proposed research,
- The data minimisation principle is met,
- Algorithms (such as artificial intelligence) are suitable for the proposed purpose and transparent,
- The ethical approval has been obtained for the proposed research, where applicable, and that the approval is applicable for the proposed research and conclusions of the ethics review are followed,
- The funding mechanisms for the proposed research are in place (if required),
- The project description corresponds with the data analysis plan and the ELSI that exist with respect to the requested data,
- check any peer review of the scientific validity of the proposed research exists, and if not, ensure the scientific validity of the proposed research,

If any step in the process fails, then the application must be rejected with the reasons recorded and options to rectify these and re-submit the application, included with the reason to reject the application. The relevant NCPs must be identified and informed of the application rejection, and can exercise a veto against the rejection.

#### 2. Recommend application for approval
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 2               | Once a completed application has been reviewed by the 1+MG DAC and recommended for approval | 1+MG DAC |

The application is marked as ‘Recommended for Approval’ or the reasons for rejection recorded, including specifying the data to which the approval recommendation applies (which may be a subset of the original applied for data). The relevant NCP(s) that administer the data requested in the application are informed of the review outcome, and the application is passed to them who execute SOP [4]. The date the application recommended for approval is recorded and a reminder set of 11 working days (DATE:A) in the future to ensure the NCP has responded to the recommendation.

#### 3. Confirm approval (no NCP response)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 3               | DATE:A is reached or past, and no response from the NCP has been received | 1+MG DAC |

The 1+MG DAC will confirm approval of the request for data access authorisation, recording the decision and reasons thereof, and inform the data user that their application has been approved.

#### 4. Confirm approval (NCP agrees)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 4               | DATE:A has not been passed, and the NCP agrees with the 1+MG DAC recommendation | 1+MG DAC |

The 1+MG DAC will confirm approval of the request for data access authorisation, recording the decision and reasons thereof, and inform the data user that their application has been approved.

#### 5. Initiate NCP review process
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 5               | DATE:A has not been passed and a response from the NCP has been received which disagrees with the 1+MG DAC recommendation | 1+MG DAC |

The 1+MG DAC will initiate the NCP review process[5], which must be completed by the time limit set within  that SOP (DATE:B). 

#### 6. Confirm approval (recommendation upheld)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 6               | DATE:B has not been passed and the review process[5] has completed with the recommendation of the 1+MG DAC upheld | 1+MG DAC |

The 1+MG DAC will confirm approval of the request for data access authorisation, recording the decision and reasons thereof, and inform the data user that their application has been approved.

#### 7. Reject application (recommendation overruled)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 7               | DATE:B has not been passed and the review process[5] has completed with the recommendation of the 1+MG DAC be overruled | 1+MG DAC |

The 1+MG DAC will reject the application with the reasons recorded, including options to rectify these and re-submit the application included with the reason to reject the application.


#### 8. Inform data user (process delayed)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 8               | DATE:B has past and the review process[5] has not returned a decision within 2 months. | 1+MG DAC |

The 1+MG DAC will inform the data user the application is still under review.

### 9. References
| Reference                                                                                                  | Description                                                          |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [1](https://docs.google.com/document/d/1b887HMySeKnJt1pN1pZspGRbEnrJ6Sfk-aAwiskYJK0/edit)                  | European GDI - SOP Charter (including Glossary)                      |
| [2](https://docs.google.com/document/d/1c2jBP2XnFgMRSuQqymts2SuSZ8Aux4kD_GAGEe0mrQY/edit)                  | European GDI - Procedures for Information Service Management (ISM)   |
| [3](https://docs.google.com/document/d/1bewArzacv-M4F6NsvG6YE4T7dKNTv84f-ga1KUothh0/edit)                  | European GDI - Organisational Roles and Responsibilities             |
| [4](https://docs.google.com/document/d/11H7doKOYlnJikQinG3TTiTsqpt7edAkc7G-DBIM9Rnw/edit#heading=h.94zixl2wbth) | European GDI - NCPs veto EDIC Decision                               |
| [5](https://docs.google.com/document/d/1PzvlFPblR9Ns_1xkaVdKL0uoGEz1DursTxANCzNNzrk/edit)                  | European GDI - Resolution procedures for disagreements 1+MG DAC and NCP |
| [6](https://docs.google.com/document/d/1LJa_vWhqUtpNnw8hW7cmPoihImqELv9dgK7Bd826EHg/edit#heading=h.94zixl2wbth) | European GDI - Obtain Institutional Sign-off                         |
