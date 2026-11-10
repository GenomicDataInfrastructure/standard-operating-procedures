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

This SOP defines a standardised process for formally withdrawing previously approved GDI Standard Operating Procedures that are obsolete, superseded or no longer applicable.

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

**Input:** A withdrawal request identifying an approved SOP that may no longer be applicable.

**Output:** An authorised withdrawal recorded in the repository, with the SOP clearly marked as withdrawn, its historical record preserved and affected stakeholders notified.

## 6. Introduction and Background Information

The GDI SOP framework provides a standardised approach for developing, reviewing, approving and maintaining operational procedures across participating nodes.

As GDI evolves, previously approved SOPs may become obsolete due to technical developments, organisational changes, updated governance requirements or the introduction of replacement procedures.

Although the existing SOP framework defines the creation and maintenance of SOPs, a dedicated process is required to manage their formal withdrawal.

Without a standardised withdrawal procedure, obsolete SOPs may remain accessible without clear indication that they are no longer applicable, potentially leading to inconsistent practices across GDI nodes.

The withdrawal process must therefore distinguish between removing an SOP from active operational use and permanently deleting its historical record.

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

1. Navigate to the repository's [GitHub Issues](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/issues).
2. Create a new issue requesting withdrawal of the relevant SOP.
3. Provide the following information:
   - SOP identifier and title.
   - Current SOP version.
   - Reason for withdrawal.
   - Description of the operational or technical changes motivating the request.
   - Replacement SOP, if applicable.
   - Known dependencies or affected GDI nodes.
   - Supporting references or documentation.
4. Submit the issue for evaluation by the OC.

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

Proceed to step 2.

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

Acceptance of the request does not constitute approval to withdraw the SOP.

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
| `4` | After the impact assessment has been completed | OC / SDPC and designated authorising body **[TO CONFIRM]** |

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

**[TO CONFIRM — GOVERNANCE]**

The existing SOP creation procedure includes OC/SDPC approval and Management Board authorisation. The equivalent authority and approval requirements for withdrawal must be agreed before this SOP is finalised.

**Decision:**

- **Approved:** Proceed to step 5.
- **Changes requested:** Return to the impact assessment or revise the withdrawal recommendation.
- **Rejected:** Document the decision and close the withdrawal request.

**Required evidence:** Traceable approval record, including decision, date and approving authority.

### 8.5. Prepare withdrawal metadata

| Step identifier | When | Who |
|---|---|---|
| `5` | After formal withdrawal approval has been recorded | Repository maintainer |

The repository maintainer prepares the changes required to identify the SOP as withdrawn.

**Procedure:**

1. Locate the approved SOP in the repository.
2. Confirm that the SOP identifier and current version match the approved withdrawal record.
3. Update the document's metadata to include the withdrawal information.
4. Add a prominent withdrawal notice at the beginning of the document.
5. Update the document history to record the withdrawal.
6. Preserve the original SOP content for historical reference.

**Proposed metadata fields:**

| Metadata | Value |
|---|---|
| Status | Withdrawn |
| Withdrawal date | YYYY.MM.DD |
| Withdrawal reason | Brief explanation |
| Superseded by | Replacement SOP identifier or N/A |
| Withdrawal reference | GitHub issue URL |
| Approval reference | Link to recorded decision |

**Example withdrawal notice:**

> **WITHDRAWN — NOT FOR OPERATIONAL USE**
>
> This SOP was formally withdrawn on YYYY.MM.DD and is no longer applicable for GDI operations.
>
> **Reason:** [Withdrawal justification]
>
> **Replacement:** [SOP identifier, if applicable]
>
> This document is retained for historical reference only.

The SOP identifier must remain unchanged and must not be reused.

**Required evidence:** Updated SOP Markdown file included in the withdrawal pull request.

Proceed to step 6.

### 8.6. Update repository documentation and references

| Step identifier | When | Who |
|---|---|---|
| `6` | After the withdrawal metadata has been prepared | Repository maintainer |

The repository must be updated to ensure that withdrawn SOPs are clearly distinguished from active procedures.

**Procedure:**

1. Update the SOP index to display the withdrawn status.
2. Review and update references to the withdrawn SOP in other documents.
3. Where applicable, add references to the replacement SOP.
4. Ensure the withdrawn SOP is not presented as an active procedure.
5. Preserve the document in the repository for historical reference.
6. Review any automated validation or publication processes affected by the new status.

**Repository retention:**

By default, the withdrawn SOP should remain at its existing file path to preserve links and Git history.

If a dedicated archive structure is adopted, the repository maintainers must ensure that historical references remain accessible and that affected links are updated.

**Identifier preservation:**

The base identifier and all previously issued versions must remain permanently reserved.

**Required evidence:** Pull request containing the proposed repository changes.

Proceed to step 7.

### 8.7. Review and publish repository changes

| Step identifier | When | Who |
|---|---|---|
| `7` | After the withdrawal changes have been prepared | Repository maintainer and designated reviewers |

The repository maintainer submits the withdrawal changes through the established GitHub contribution workflow.

**Procedure:**

1. Create a working branch from the repository's designated development branch.
2. Commit the withdrawal-related changes.
3. Open a pull request referencing the approved withdrawal issue.
4. Request review from the appropriate repository maintainers and OC representatives.
5. Verify that the changes are consistent with the approval record.
6. Run the applicable repository validation checks.
7. Resolve review comments and merge the pull request in accordance with repository governance.

**Example Git commands** (assuming the repository's designated development branch is `dev`; verify before use):

```bash
git fetch origin
git switch dev
git pull --ff-only origin dev

git switch -c sop-withdrawal-XXXX

# Edit the relevant SOP and repository files

git add .
git commit -m "docs: withdraw GDI-SOPXXXX"

git push -u origin sop-withdrawal-XXXX
```

The pull request must contain a link to the original withdrawal issue and the recorded approval.

**Required evidence:** Merged pull request and passing repository checks.

Proceed to step 8.

### 8.8. Communicate the withdrawal

| Step identifier | When | Who |
|---|---|---|
| `8` | After the withdrawal has been published, or earlier if required by the approved transition plan | OC, supported by repository maintainers |

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

**Important:** Changes in the central repository do not necessarily update local forks or independently imported repositories automatically. Affected nodes remain responsible for reviewing and incorporating relevant changes into their local procedures.

**Required evidence:** Communication record, including notification date and channels used.

Proceed to step 9.

### 8.9. Verify withdrawal and close request

| Step identifier | When | Who |
|---|---|---|
| `9` | After repository publication and communication have been completed | OC and repository maintainer |

The OC verifies that the withdrawal has been implemented according to the approved decision.

**Verification checklist:**

- [ ] Formal withdrawal approval is documented.
- [ ] SOP metadata indicates `Withdrawn`.
- [ ] Withdrawal date and justification are recorded.
- [ ] A visible withdrawal notice is present.
- [ ] SOP identifier remains unchanged and reserved.
- [ ] Historical content remains accessible.
- [ ] Repository index has been updated.
- [ ] Relevant references have been reviewed.
- [ ] Repository checks have passed.
- [ ] Affected GDI nodes have been notified.
- [ ] Withdrawal issue links to the merged pull request.

Once the verification is complete, the OC records the outcome in the GitHub issue and closes the request.

Any unresolved node-specific follow-up actions must remain traceable through an appropriate issue or action record.

**Output:** A formally withdrawn SOP with a complete and auditable withdrawal record.

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
