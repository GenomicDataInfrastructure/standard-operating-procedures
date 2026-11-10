# European GDI - Withdrawal of Approved SOPs

| Metadata | Value |
|---|---|
| Template SOP number | `GDI-SOPXXXX` |
| Template SOP version | `v1.0.1` |
| Topic | Data & metadata management |
| Template SOP Type | European-Level SOP |
| GDI Node | |
| Instance Version | |



## Index

1. Document History
2. Glossary
3. Roles and Responsibilities
4. Purpose
5. Scope
6. Introduction and Background Information
7. Summary or Context Diagram
8. Procedure
9. References

---

## 1. Document History

| Template Version | Instance version | Author(s) | Description of changes | Date |
|---|---|---|---|---|
|  v1.0.1 | | Silvia Bahena | Initial draft of the SOP withdrawal procedure, addressing GitHub Issue #76 | 2026.11.10 |

## 2. Glossary

Find the common GDI SOP glossary in the [Charter](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_charter.md).

| Abbreviation | Description |
|---|---|
| GDI | Genomic Data Infrastructure |
| GH | GitHub |
| MB | Management Board |
| OC | Operations Committee |
| PR | Pull Request |
| SDPC | Security and Data Protection Committee |
| SOP | Standard Operating Procedure |
| WP | Work Package |

| Term | Definition |
|---|---|
| Active SOP | An approved SOP currently applicable for operational use. |
| Withdrawal | Formal process of removing an approved SOP from operational use while retaining its historical record. |
| Withdrawn SOP | An SOP formally declared no longer applicable. It must not be used as an active operational procedure. |
| Superseded SOP | An SOP replaced by another approved SOP. Supersession is a possible reason for withdrawal. |
| SOP owner | Person or group responsible for maintaining the content of an SOP. |
| Repository maintainer | Authorised contributor responsible for maintaining the GDI SOP GitHub repository. |
| Withdrawal record | Documentation containing the justification, decision, approval and implementation details of an SOP withdrawal. |

## 3. Roles and Responsibilities

See the [Organisational Roles and Responsibilities](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_organisational-roles-and-responsibilities.md).


| Role | Full name | GDI/node role | Organisation |
|---|---|---|---|
| Author | Silvia Bahena | Task 4.3 member | EMBL-EBI |
| Reviewer | Marcos Casado | Task 4.3 member | EMBL-EBI |
| Approver | Gabriele Rinck | Task 4.3 Lead /OC / SDPC | EMBL-EBI |
| Authorizer | Management Board | Authorizer according to GDI SOP governance | GDI |


## 4. Purpose

This SOP defines a standardised process for formally withdrawing previously approved GDI Standard Operating Procedures (SOPs) that are obsolete, superseded or no longer applicable.

It ensures that withdrawal decisions are appropriately assessed, documented, approved and communicated, while preserving document history, identifiers and traceability across the GDI infrastructure.

## 5. Scope

This SOP applies to approved European-level SOPs and node-specific SOP templates maintained in the central [GDI SOP repository](https://github.com/GenomicDataInfrastructure/standard-operating-procedures).

The procedure covers the complete withdrawal lifecycle, from the submission of a withdrawal request to the final update of the repository and communication to affected stakeholders.

The process includes:

- Identification and justification of withdrawal requests.
- Assessment of operational, technical, security and data protection implications.
- Review and approval by the relevant governance bodies.
- Updates to SOP metadata, repository indexes and references.
- Preservation of historical documentation and identifiers.
- Communication to affected GDI nodes and repository users.
- Verification and closure of the withdrawal request.

**Out of scope:** The independent withdrawal of node-specific SOP instances maintained exclusively in local node repositories. These remain subject to local governance. However, GDI nodes must be informed when a central SOP or template on which their local procedures depend is withdrawn.


## 6. Introduction and Background Information

The GDI SOP framework provides a standardised approach for developing, reviewing, approving and maintaining operational procedures across GDI and participating nodes.

As GDI evolves, previously approved SOPs may become obsolete due to technical developments, organisational changes, updated governance requirements or the introduction of replacement procedures.

Although the importance for a dedicated process to manage the SOPs formal withdrawal.

Without a standardised withdrawal procedure, obsolete SOPs may remain accessible without clear indication that they are no longer applicable, potentially leading to inconsistent practices across GDI nodes.

**The following principles apply:**

1. Approved SOPs must not be withdrawn without a documented decision.
2. Withdrawn SOPs must remain accessible for historical reference.
3. Withdrawn SOP identifiers must never be reassigned or reused.
4. The withdrawal date, justification and approval record must be traceable.
5. Withdrawn SOPs must be clearly distinguished from active SOPs.
6. Affected GDI nodes must be informed of the withdrawal.
7. Dependencies and references to withdrawn SOPs must be reviewed and updated where necessary.

## 7. Summary or Context Diagram

The withdrawal process follows the sequence below:

**Withdrawal request → Initial assessment → Impact assessment → Review and approval → Repository update → Communication → Verification and closure**

At the initial assessment stage, the request may be accepted, rejected or returned for additional information.

At the approval stage, a withdrawal may be approved, rejected or returned for further assessment. Repository changes must not be published as a formal withdrawal until the required approval has been obtained.

## 8. Procedure

### 8.1. Submit SOP withdrawal request

| Step identifier | When | Who |
|---|---|---|
| `1` | When an approved SOP is identified as potentially obsolete, superseded or no longer applicable | Any GDI member |

A withdrawal request must be created as an issue in the GDI SOP GitHub repository.

**Procedure:**

1. Navigate to the GDI SOP GitHub Issues.

1. Select New issue.

1. Choose the Request SOP Withdrawal template.

1. Complete all mandatory fields, including the SOP identifier, title, version, URL, withdrawal reason and justification.

1. Provide additional information about replacement SOPs, dependencies and potential impacts, where known.

1. Submit the request for assessment by the Operations Committee.

**Withdrawal criteria**

| Criterion | Description |
|---|---|
| Obsolete | The procedure is no longer applicable to current GDI operations. |
| Superseded | A newer approved SOP replaces the existing procedure. |
| Technical changes | The infrastructure, service or technology described is no longer supported. |
| Governance changes | Changes to organisational responsibilities or policies make the SOP inapplicable. |
| Security or compliance | The procedure is inconsistent with current security, legal or data protection requirements. |
| Process discontinuation | The activity or service described in the SOP has been discontinued. |

**Required evidence:** GitHub issue containing the withdrawal request and justification.


### 8.2. Evaluate the withdrawal request

| Step identifier | When | Who |
|---|---|---|
| `2` | After a withdrawal request has been submitted | OC |

The OC evaluates the request to determine whether the proposed withdrawal is justified and sufficiently documented.

**Procedure:**

1. Verify that the SOP identifier and version are correct.
2. Confirm that the SOP is currently approved and has not already been withdrawn.
3. Review the justification against the withdrawal criteria defined in step 1.
4. Determine whether withdrawal is appropriate or whether an update to the existing SOP would be more suitable.
5. Identify missing information and request clarification where necessary.
6. Consult the SDPC if the request involves security or data protection considerations.

**Decision:**

- **Accepted:** Record the acceptance in the GitHub issue and proceed to step 3.
- **Additional information required:** Request clarification from the submitter and repeat the evaluation.
- **Rejected:** Document the reason for rejection and close the issue.

Important: Acceptance of the request does not constitute approval to withdraw the SOP.

**Required evidence:** Documented initial assessment and decision in the GitHub issue.

### 8.3. Assess impact and dependencies

| Step identifier | When | Who |
|---|---|---|
| `3` | After the withdrawal request has been accepted | OC, SOP owner, relevant technical experts and SDPC where applicable |

Before requesting formal approval, the impact of withdrawing the SOP must be assessed.

**Procedure:**

1. Review the SOP's purpose, scope and operational relevance.
2. Identify other SOPs or supporting documents that reference the procedure.
3. Determine whether the SOP has been adopted or adapted by GDI nodes.
4. Identify any technical, operational, security or compliance risks associated with withdrawal.
5. Verify whether a replacement procedure exists and is approved.
6. Determine whether transitional actions are required before withdrawal.
7. Document the findings in the GitHub issue.

**Assessment checklist:**

- [ ] The reason for withdrawal is documented.
- [ ] Related SOPs and dependencies have been identified.
- [ ] Affected GDI nodes have been considered.
- [ ] Security and data protection implications have been assessed.
- [ ] Replacement procedures have been identified where applicable.
- [ ] Required transitional actions have been documented.

**Decision:**

If withdrawal would leave a critical operational process without an applicable procedure, the OC must determine whether withdrawal should be postponed until a replacement or mitigation is available.

**Required evidence:** Impact assessment recorded in the withdrawal issue.

Proceed to step 4.

### 8.4. Review and approve withdrawal

| Step identifier | When | Who |
|---|---|---|
| `4` | After the impact assessment has been completed | OC / SDPC / Managment Board |

The proposed withdrawal must undergo formal review before repository changes are implemented.

**Proposed procedure:**

1. The OC prepares a withdrawal recommendation containing:
   - SOP identifier, title and version.
   - Withdrawal justification.
   - Impact assessment.
   - Replacement SOP, if applicable.
   - Proposed withdrawal date.
   - Communication and transition requirements.
2. The recommendation is submitted to the appropriate reviewers.
3. The SDPC participates where security or data protection considerations apply.
4. The designated governance body reviews and records its decision.
5. The decision is linked to the GitHub withdrawal issue.

**Decision:**

- **Approved:** Proceed to step 5.
- **Changes requested:** Return to the impact assessment or revise the withdrawal recommendation.
- **Rejected:** Document the decision and close the withdrawal request.

**Required evidence:** Traceable approval record, including decision, date and approving authority.

#### 8.5. Prepare withdrawal metadata

| Step identifier | When | Who |
|---|---|---|
| `5` | After formal withdrawal approval has been recorded | Repository maintainer |

The repository maintainer must clearly identify the SOP as withdrawn and move it to the designated directory for withdrawn SOPs.

**Procedure:**

1. Locate the approved SOP in the GDI SOP repository and verify its identifier and version against the approved withdrawal record.
2. Add the following **WITHDRAWN** notice at the beginning of the SOP Markdown file, before its main content. Replace all placeholders with the approved information:

   ```markdown
   > [!WARNING]
   > **WITHDRAWN — NOT FOR OPERATIONAL USE**
   >
   > This SOP was formally withdrawn on YYYY-MM-DD and is no longer applicable for GDI operations.
   >
   > **Reason:** [Withdrawal justification]
   >
   > **Replacement SOP:** [SOP identifier and link, or N/A]
   >
   > **Withdrawal request and approval:** [GitHub issue / approval record links]
   >
   > This document is retained for historical reference only.
   ```

3. Update the document metadata to show its status as **Withdrawn**, the effective withdrawal date, withdrawal reason, replacement (if applicable), and approval reference.
4. Add an entry to the document history recording the withdrawal, without removing or rewriting previous history entries.
5. After the notice is added. Move the withdrawn sop to the folder `sops/withdrawn/`. Keep the original SOP identifier and filename unchanged.

Proceed to step 6.

#### 8.6. Update repository documentation and references

| Step identifier | When | Who |
|---|---|---|
| `6` | After the withdrawn SOP has been relocated | OC|

Update the withdrawn index records.

**Procedure:**

1. Open `sops/withdrawn/README.md` and add a row to the **Withdrawn SOP Register**, recording:
   - SOP identifier and title, linked to its new location.
   - Effective withdrawal date.
   - Withdrawal reason.
   - Replacement SOP, if applicable.
   - Link to the GitHub withdrawal issue and recorded approval.
2. Update the main SOP index and remove the record of the withdrawn SOP. 
3. Search the repository for the withdrawn SOP identifier, old file path, and related links. Review matches in other SOPs, README files, and supporting documentation.
4. Update links to the withdrawn SOP's new path (`sops/withdrawn/`). Where operational guidance should point to a replacement SOP, link to the approved replacement instead. 
6. Confirm that the withdrawn SOP remains accessible, that the register and index entries are accurate, and that links resolve correctly.


**Verification checklist:**

- [ ] A complete entry exists in `sops/withdrawn/README.md`.
- [ ] The active SOP index no longer presents the withdrawn SOP as active.
- [ ] Relevant links and references have been reviewed and updated.
- [ ] The withdrawal notice, date, reason, and approval references agree with the withdrawal record.
- [ ] The withdrawn Markdown file remains accessible in `sops/withdrawn/`.
- [ ] Relevant repository validation checks pass.


Proceed to step 7.

### 8.7. Review and publish repository changes

| Step identifier | When | Who |
|---|---|---|
| `7` | After the withdrawal changes have been prepared | OC |

The OC contact in charged of the withdrawal changes through the established GitHub contribution workflow.

**Procedure:**

1. Create a working branch from the repository's designated development branch.
2. Commit the withdrawal-related changes.
3. Open a pull request referencing the approved withdrawal issue.
4. Request review from the appropriate OC representatives.
5. Verify that the changes are consistent with the approval record.
6. Run the applicable repository validation checks.
7. Resolve review comments and merge the pull request in accordance with repository governance.

Proceed to step 8.

### 8.8. Communicate the withdrawal

| Step identifier | When | Who |
|---|---|---|
| `8` | After the withdrawal has been published | OC|

The withdrawal must be communicated to relevant stakeholders to prevent continued use of the obsolete procedure.

**Procedure:**

1. Identify the GDI nodes and stakeholders potentially affected.
2. Prepare a withdrawal notification including:
   - SOP identifier and title.
   - Effective withdrawal date.
   - Reason for withdrawal.
   - Replacement SOP, if applicable.
   - Actions required by affected nodes.
   - Link to the withdrawal record.
3. Distribute the notification through the agreed GDI communication channels.
4. Request affected nodes to review their local copies, forks or SOP instances.
5. Record the communication and any required follow-up actions in the GitHub issue.


Proceed to step 9.


### 8.9. Verify withdrawal and close request

| Step identifier | When | Who |
|---|---|---|
| `9` | After repository changes have been merged and the withdrawal has been communicated | OC |

The OC contact must verify that the withdrawal has been correctly implemented, documented, and communicated before closing the withdrawal request.

**Procedure:**

1. Verify that the withdrawal was formally approved and that the approval record is linked to the GitHub issue.
2. Confirm that the SOP Markdown file:
   - Contains a prominent **WITHDRAWN — NOT FOR OPERATIONAL USE** notice.
   - Includes the withdrawal date, reason, replacement SOP (if applicable), and approval reference.
   - Has been moved to the `sops/withdrawn/` directory.
   - Retains its original SOP identifier, version, and historical content.
3. Verify that the withdrawn SOP has been added to the withdrawal register in `sops/withdrawn/README.md`.
4. Confirm that the main SOP index and all relevant repository references have been updated to reflect the withdrawal and the new file location.
5. Check that the withdrawn SOP is no longer listed or presented as an active operational procedure.
6. Verify that the withdrawal pull request has been reviewed, approved, and merged, and that all applicable repository validation checks have passed.
7. Confirm that affected GDI nodes and stakeholders have been notified and that the communication is documented.
8. Record the final verification results in the original GitHub withdrawal issue.
9. Close the GitHub issue once all required actions have been completed.

**Final verification checklist:**

- [ ] Formal withdrawal approval is documented and linked.
- [ ] SOP contains the **WITHDRAWN** notice.
- [ ] Withdrawal date, reason, and approval reference are recorded.
- [ ] Replacement SOP is identified, where applicable.
- [ ] SOP has been moved to `sops/withdrawn/`.
- [ ] Original SOP identifier, version, and historical content are preserved.
- [ ] Withdrawal register (`sops/withdrawn/README.md`) is updated.
- [ ] Main SOP index and related references are updated.
- [ ] Withdrawn SOP is no longer presented as active.
- [ ] Pull request is approved and merged.
- [ ] Repository validation checks have passed.
- [ ] Affected GDI nodes and stakeholders have been notified.
- [ ] Withdrawal issue contains links to the approval record, merged PR, and communication evidence.

If any verification item is incomplete, the issue must remain open until the outstanding actions have been resolved or documented in a separately tracked follow-up issue approved by the OC.



**End of procedure.**


## 9. References

| Reference | Description |
|---|---|
| [GDI SOP Charter](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_charter.md) | Governance principles and terminology |
| [GDI Information Service Management](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_information-service-management.md) | SOP lifecycle and information management |
| [GDI Organisational Roles and Responsibilities](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_organisational-roles-and-responsibilities.md) | Roles and responsibilities |
| [GDI-SOP0007](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/sops/european-level/GDI-SOP0007_sop-template-creation.md) | SOP creation, review, approval and authorisation |
| [GDI SOP Template](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_sop-template.md) | Standard SOP structure |
| [GDI SOP Accessioning](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_sop-accessioning.md) | Identifier, versioning and repository conventions |
| [GDI GitHub Management](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/blob/main/docs/GDI-SOP_github-management.md) | Repository management and node forks |
| [GitHub Issue #76](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/issues/76) | Original withdrawal SOP request |
