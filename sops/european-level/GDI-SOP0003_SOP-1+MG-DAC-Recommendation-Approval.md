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
| ``v1``               |                  | Marcos Casado Barbero    | Transform document to markdown and complete version | ``2024.10.04`` |
| ``v0``               |                  | Dylan Spalding    | First version of SOP drafted     | ``2024.04.11`` |

### 2. Glossary
Find GDI SOPs common Glossary at the [**charter document**](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_charter.md).

| Abbreviation | Description                                                                                               |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 1+MG DAC     | 1+MG Data Access Committee (1+MG DAC) - Data Access Committee, which may include several domain-specific sub-committees, provided by 1+MG that receives and reviews access requests and moderates consensus discussions on access requests where necessary |
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
| Reviewer   | Gergő Csarnai | LU / Senior ELSI Specialist | LNDS |
| Approver   | Gabriele Rinck | Task 4.3 member | EMBL-EBI |

### 4. Purpose
The purpose of this SOP is to define the process for **requesting and granting access to controlled data within the European Genomic Data Infrastructure (GDI)**. This SOP ensures that:

- **Access to data is granted only in justified cases**, following thorough review by the 1+MG Data Access Committee (DAC) and involving all necessary stakeholders to protect the rights and freedoms of the data subjects.
- The 1+MG DAC **reviews applications** to ensure **compliance with the 1+MG Data Governance requirements**, and **makes recommendations** to National Coordination Points (NCPs), who may agree or exercise their veto rights.
- The **process is transparent**, and **disputes are resolved in a timely manner**, adhering to the allocated timeframes for each request.

### 5. Scope
This SOP covers the process **from when a data access application is received by the 1+MG DAC to when the application is approved or rejected** by the 1+MG DAC. The **input** is a completed application form, and the **output** is a notification of approval or rejection of the request for authorisation to access the controlled access data described in the application.

### 6. Introduction and Background Information
To access controlled access data within the European Genomic Data Infrastructure a user must apply for authorisation to access the data from the 1+ Million Genomes Data Access Committee (1+MG DAC). The 1+MG DAC will **review applications** to ensure they conform to the 1+MG Data Governance requirements, and **make recommendations** to the relevant National Coordination Points (NCPs) who may agree or disagree with the recommendation.

Additionally, the 1+MG DAC will follow a review process when the NCP disagrees with its recommendation (see [GDI-SOP0002_NCPs-veto-EDIC-decision.md](../node-specific/GDI-SOP0002_NCPs-veto-EDIC-decision.md)). Once an agreement is reached, or the review process completes, the data user will be informed of the decision.

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
#### 8.1. Initiate application check
| Step identifier | When                                       | Who          |
|-----------------|--------------------------------------------|--------------|
| 1               | On receipt of notification of a new data access application | 1+MG DAC     |

As the 1+MG DAC, check the requester's application, based on the requirement in the Data Governance document. The application form, which is used to help the data requester enter valid and complete information for the application, must be checked to ensure that:
- Confirm the research has [institutional sign-off](https://docs.google.com/document/d/1LJa_vWhqUtpNnw8hW7cmPoihImqELv9dgK7Bd826EHg/edit#heading=h.94zixl2wbth), if applicable (i.e., if the requestor is employed by a suitable institution).
- The data analysis plan is present and suitable for the proposed research.
- The data minimisation principle is met.
- Algorithms (such as artificial intelligence) are suitable for the proposed purpose and transparent.
- The ethical approval has been obtained for the proposed research, where applicable, and that the approval is applicable for the proposed research and conclusions of the ethics review are followed.
- The funding mechanisms for the proposed research are in place (if required).
- The project description corresponds with the data analysis plan and the ELSI that exist with respect to the requested data.
- Any peer review of the scientific validity of the proposed research exists, and if not, ensure the scientific validity of the proposed research.

You must **finish this initial assessment within 5 working days**. After this period,you shall **transmit the outcome of the review and a decision recommendation** to the 1+MG NCPs who can channel it to relevant bodies on the national level.

Depending on the outcome of this initial evaluation:
- If all steps are correct, move to **[step 2](#82-recommend-application-for-approval)**.
- If **any step fails**, the **application must be rejected**:
   - Inform the relevant NCPs, who may veto the rejection (see [GDI-SOP0002_NCPs-veto-EDIC-decision.md](../node-specific/GDI-SOP0002_NCPs-veto-EDIC-decision.md)). In your communication to the NCPs, clearly state the date for which their veto expires. Also inform NCPs about the possibility, in exceptional and justified cases (as defined in the [1+MG Data Access Governance for Research](https://docs.google.com/document/d/19HVf7SP2R_fCI-KugVStZR4yEAkV6vhvSbVd6a2ZviU))
   - After 6 _calendar_ days since NCPs were notified, **send a reminder** to the NCPs.
   - After 11 working days (``DATE:A``) since NCPs were notified, if no response was given from NCPs, move to **[step 10](#810-inform-data-requestor-rejection-confirmed)**.

#### 8.2. Recommend application for approval
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 2               | Once a completed application has been reviewed by the 1+MG DAC and recommended for approval | 1+MG DAC |

Once initial evaluation of data request is positive, **mark application** as 'Recommended for Approval'.

**Inform the relevant NCP(s)** of the review outcome, and pass the application to them for further action as per [GDI-SOP0002_NCPs-veto-EDIC-decision.md](../node-specific/GDI-SOP0002_NCPs-veto-EDIC-decision.md). Record the date of recommendation and set a reminder for 11 working days (``DATE:A``).

Depending on the response from NCPs:
- If **no response** before the end of DATE:A, move to **[step 3](#83-confirm-approval-no-ncp-response)**.
- If **NCPs agree** with recommendation, move to **[step 4](#84-confirm-approval-ncp-agrees)**.
- If **NCPs disagree** with recommendation, move to **[step 5](#85-initiate-ncp-review-process)**.

#### 8.3. Confirm approval (no NCP response)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 3               | DATE:A is reached or past, and no response from the NCP has been received | 1+MG DAC |

After the end of ``DATE:A`` is reached with no response from relevant NCPs, **confirm the approval of the data access request**: move to **[step 9](#89-inform-data-user-approval-confirmed)**.

#### 8.4. Confirm approval (NCP agrees)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 4               | DATE:A has not been passed, and the NCP agrees with the 1+MG DAC recommendation | 1+MG DAC |

If the **NCP agrees** with the recommendation, then **confirm the approval of the data access request**: move to **[step 9](#89-inform-data-user-approval-confirmed)**.

#### 8.5. Initiate NCP review process
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 5               | DATE:A has not been passed, and the NCP disagrees with the 1+MG DAC recommendation | 1+MG DAC |

If the NCP disagrees with the recommendation, **initiate the review process for handling NCP disagreements** as per SOP [NCP review process of disagreement with 1+MG DAC recommendation](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/issues/33). This process must be completed by the time limit set in that SOP (``DATE:B``).

Depending on the outcome of the NCP review process:
- If **no response** before the end of ``DATE:B``, move to **[step 8](#88-inform-data-user-process-delayed)**.
- If **NCPs upholds recommendation**, move to **[step 6](#86-confirm-approval-recommendation-upheld)**.
- If **NCPs overrules recommendation**, move to **[step 5](#85-initiate-ncp-review-process)**.

#### 8.6. Confirm approval (recommendation upheld)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 6               | DATE:B has not been passed, and the NCP review process upholds the 1+MG DAC recommendation | 1+MG DAC |

If the outcome of the NCP review process is positive, then **confirm the approval of the data access request**: move to **[step 9](#89-inform-data-user-approval-confirmed)**.

#### 8.7. Reject application (recommendation overruled)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 7               | DATE:B has not been passed, and the NCP review process overrules the 1+MG DAC recommendation | 1+MG DAC |

If the NCPs overrule the initial recommendation, **reject the application**: move to **[step 10](#810-inform-data-requestor-rejection-confirmed)**.

#### 8.8. Inform data user (process delayed)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 8               | DATE:B has passed, and the review process has not returned a decision within 2 months | 1+MG DAC |

After the end of ``DATE:B``, if no decision is obtained **after 2 months**, **inform the data user that the application is still under review**.

Move back to **[step 5](#85-initiate-ncp-review-process)**.

#### 8.9. Inform data requestor (Approval confirmed)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 9               | After confirmation of approval is reached      | 1+MG DAC |

Regardless of the path of confirmation, once the approval has been confirmed:
- **Record the decision and reasons**.
- **Inform the data requestor**.

This concludes the process resulting in confirmation of the data request.

#### 8.10. Inform data requestor (Rejection confirmed)
| Step identifier | When                                           | Who      |
|-----------------|------------------------------------------------|----------|
| 10               | After rejection of request is reached          | 1+MG DAC |

Regardless of the path of rejection:
- **Record the decision and reasons** (e.g., missing documents, invalid data, non-compliance with ethical standards...). Include options to rectify these issues for the data requestor to amend and re-submit the application.
- **Inform the data requestor**.

This concludes the process resulting in rejection of the data request.

### 9. References
| Reference                                                                                                  | Description                                                          |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [1](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_charter.md) | European GDI - SOP Charter |
| [2](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_organisational-roles-and-responsibilities.md) | European GDI - Organisational Roles and Responsibilities (ORR) |
| [3](../node-specific/GDI-SOP0002_NCPs-veto-EDIC-decision.md) | European GDI SOP - NCPs veto EDIC Decision                               |
| [4](https://docs.google.com/document/d/19HVf7SP2R_fCI-KugVStZR4yEAkV6vhvSbVd6a2ZviU) | 1+MG Data Access Governance for Research |
| [5](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/issues/33)                  | European GDI - NCP review process of disagreement with 1+MG DAC recommendation |
| [6](https://docs.google.com/document/d/1LJa_vWhqUtpNnw8hW7cmPoihImqELv9dgK7Bd826EHg/edit#heading=h.94zixl2wbth) | European GDI - Obtain Institutional Sign-off                         |