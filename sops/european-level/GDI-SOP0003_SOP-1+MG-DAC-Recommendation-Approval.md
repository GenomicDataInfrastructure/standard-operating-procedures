# European GDI - 1+MG DAC Recommendation Approval Process

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
To access controlled access data within the European Genomic Data Infrastructure a research user must apply for authorisation to access the data from the 1+ Million Genomes Data Access Committee (1+MG DAC). The 1+MG DAC (a.k.a. 1+MG EDIC) will **review applications** to ensure they conform to the 1+MG Data Governance requirements, and **make recommendations** to the relevant National Coordination Points (NCPs) who may agree or disagree with the recommendation.

### 5. Scope
This SOP covers the process **from when a data access application is received by the 1+MG DAC to when the application is approved or rejected** by the 1+MG DAC. The **input** is a completed application form, and the **output** is a notification of approval or rejection of the request for authorisation to access the controlled access data described in the application.

### 6. Introduction and Background Information
The 1+MG DAC is responsible for recommending the approval or rejection of requests for access to data held within the GDI to the relevant NCP(s). Additionally, the 1+MG DAC will follow a review process when the NCP disagrees with its recommendation (see [GDI-SOP0002_NCPs-veto-EDIC-decision.md](../node-specific/GDI-SOP0002_NCPs-veto-EDIC-decision.md)). Once an agreement is reached, or the review process completes, the data user will be informed of the decision.

### 7. Summary or Context Diagram
The following diagram summarises the step-by-step process for the recommendation by the 1+MG DAC of approval or rejection of data access applications.
````mermaid
graph TD
    A[**Start**: Data Access<br>Application Received]
    B1{**Step 1**:<br> Application Checked<br> by 1+MG DAC}
    B2[**Step 2**: Application<br>Recommended for Approval]
    B2.2{Response<br>from NCPs?}
    B3[**Step 3**: No NCP Response<br> - Approval Confirmed]
    B4[**Step 4**: NCP Agrees<br> - Approval Confirmed]
    B5[**Step 5**: NCP Disagrees<br> - NCP Review<br> Process Initiated]
    B6[**Step 6**: NCP Review<br> Upholds Recommendation<br> - Approval Confirmed]
    B7[**Step 7**: NCP Review<br> Overrules Recommendation<br> - Application Rejected]
    B8[**Step 8**: Review Delayed<br> - Inform Data User]
    B9[**Step 9**: Approval confirmed<br> - Inform Data User]
    B10[**Step 10**: Rejection confirmed<br> - Inform Data User]

    A --> B1
    B1 -->|Application<br>is approved| B2
    B2 --> B2.2
    B2.2 -->|No NCP Response| B3
    B2.2 -->|NCP Agrees| B4
    B2.2 -->|NCP Disagrees| B5
    B3 --> B9
    B4 --> B9
    B6 --> B9
    B5 -->|Recommendation Upheld| B6
    B5 -->|Recommendation Overruled| B7
    B5 -->|Review Delayed| B8
    B1 -->|Application<br>is rejected| B10
    B7 --> B10
    B8 -->|Follow up<br> review process| B5
````

### 8. Procedure
#### 1. Initiate application check
| Step identifier | When                                       | Who          |
|-----------------|--------------------------------------------|--------------|
| 1               | On receipt of notification of a new data access authorisation application | 1+MG DAC     |

As the 1+MG DAC, check the requester's application, based on the requirement in the Data Governance document. The application form, which is used to help the data requester enter valid and complete information for the application, must be checked to ensure that:
- Confirm the research has [institutional sign-off](https://docs.google.com/document/d/1LJa_vWhqUtpNnw8hW7cmPoihImqELv9dgK7Bd826EHg/edit#heading=h.94zixl2wbth).
- The data analysis plan is present and suitable for the proposed research.
- The data minimisation principle is met.
- Algorithms (such as artificial intelligence) are suitable for the proposed purpose and transparent.
- The ethical approval has been obtained for the proposed research, where applicable, and that the approval is applicable for the proposed research and conclusions of the ethics review are followed.
- The funding mechanisms for the proposed research are in place (if required).
- The project description corresponds with the data analysis plan and the ELSI that exist with respect to the requested data.
- Any peer review of the scientific validity of the proposed research exists, and if not, ensure the scientific validity of the proposed research.

Depending on the outcome of this evaluation:
- If all steps are correct, move to **[step 2](#2-recommend-application-for-approval)**.
- If **any step fails**, the **application must be rejected**:
   - Inform the relevant NCPs, who may veto the rejection (see [GDI-SOP0002_NCPs-veto-EDIC-decision.md](../node-specific/GDI-SOP0002_NCPs-veto-EDIC-decision.md)).
   - After 11 working days (``DATE:A``) since NCPs were notified, move to **[step 10](#10-inform-data-requestor-rejection-confirmed)**.

#### 2. Recommend application for approval
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 2               | Once a completed application has been reviewed by the 1+MG DAC and recommended for approval | 1+MG DAC |

Once initial evaluation of data request is positive, **mark application** as 'Recommended for Approval'.

**Inform the relevant NCP(s)** of the review outcome, and pass the application to them for further action as per [GDI-SOP0002_NCPs-veto-EDIC-decision.md](../node-specific/GDI-SOP0002_NCPs-veto-EDIC-decision.md). Record the date of recommendation and set a reminder for 11 working days (``DATE:A``).

Depending on the response from NCPs:
- If **no response** before the end of DATE:A, move to **[step 3](#3-confirm-approval-no-ncp-response)**.
- If **NCPs agree** with recommendation, move to **[step 4](#4-confirm-approval-ncp-agrees)**.
- If **NCPs disagree** with recommendation, move to **[step 5](#5-initiate-ncp-review-process)**.

#### 3. Confirm approval (no NCP response)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 3               | DATE:A is reached or past, and no response from the NCP has been received | 1+MG DAC |

After the end of ``DATE:A`` is reached with no response from relevant NCPs, **confirm the approval of the data access request**: move to **[step 9](#9-inform-data-user-approval-confirmed)**.

#### 4. Confirm approval (NCP agrees)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 4               | DATE:A has not been passed, and the NCP agrees with the 1+MG DAC recommendation | 1+MG DAC |

If the **NCP agrees** with the recommendation, then **confirm the approval of the data access request**: move to **[step 9](#9-inform-data-user-approval-confirmed)**.

#### 5. Initiate NCP review process
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 5               | DATE:A has not been passed, and the NCP disagrees with the 1+MG DAC recommendation | 1+MG DAC |

If the NCP disagrees with the recommendation, **initiate the review process for handling NCP disagreements** as per SOP [NCP review process of disagreement with 1+MG DAC recommendation](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/issues/33). This process must be completed by the time limit set in that SOP (``DATE:B``).

Depending on the outcome of the NCP review SOP:
- If **no response** before the end of ``DATE:B``, move to **[step 8](#8-inform-data-user-process-delayed)**.
- If **NCPs upholds recommendation**, move to **[step 6](#6-confirm-approval-recommendation-upheld)**.
- If **NCPs overrules recommendation**, move to **[step 5](#5-initiate-ncp-review-process)**.

#### 6. Confirm approval (recommendation upheld)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 6               | DATE:B has not been passed, and the NCP review process upholds the 1+MG DAC recommendation | 1+MG DAC |

If the outcome of the NCP review process is positive, then **confirm the approval of the data access request**: move to **[step 9](#9-inform-data-user-approval-confirmed)**.

#### 7. Reject application (recommendation overruled)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 7               | DATE:B has not been passed, and the NCP review process overrules the 1+MG DAC recommendation | 1+MG DAC |

If the NCPs overrule the initial recommendation, **reject the application**: move to **[step 10](#10-inform-data-requestor-rejection-confirmed)**.

#### 8. Inform data user (process delayed)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 8               | DATE:B has passed, and the review process has not returned a decision within 2 months | 1+MG DAC |

After the end of ``DATE:B``, if no decision is obtained **after 2 months**, **inform the data user that the application is still under review**.

Move back to **[step 5](#5-initiate-ncp-review-process)**.

#### 9. Inform data requestor (Approval confirmed)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 9               | After confirmation of approval is reached      | 1+MG DAC |

Regardless of the path of confirmation, once the approval has been confirmed:
- **Record the decision and reasons**.
- **Inform the data requestor**.

This SOP is considered finished at this point.

#### 10. Inform data requestor (Rejection confirmed)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 10               | After rejection of request is reached          | 1+MG DAC |

Regardless of the path of rejection:
- **Record the decision and reasons** (e.g., missing documents, invalid data, non-compliance with ethical standards...). Include options to rectify these issues for the data requestor to amend and re-submit the application.
- **Inform the data requestor**.

This SOP is considered finished at this point.

### 9. References
| Reference                                                                                                  | Description                                                          |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [1](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_charter.md) | European GDI - SOP Charter |
| [2](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_organisational-roles-and-responsibilities.md) | European GDI - Organisational Roles and Responsibilities (ORR) |
| [3](../node-specific/GDI-SOP0002_NCPs-veto-EDIC-decision.md) | European GDI SOP - NCPs veto EDIC Decision                               |
| [4](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/issues/33)                  | European GDI - NCP review process of disagreement with 1+MG DAC recommendation |
| [5](https://docs.google.com/document/d/1LJa_vWhqUtpNnw8hW7cmPoihImqELv9dgK7Bd826EHg/edit#heading=h.94zixl2wbth) | European GDI - Obtain Institutional Sign-off                         |