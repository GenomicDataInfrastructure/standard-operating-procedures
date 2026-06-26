# European GDI - Add datasets metadata to Node beacon

| Metadata             | Value                                                                 |
| -------------------- | --------------------------------------------------------------------- |
| Template SOP number  | `GDI-SOP0014`                                                         |
| Template SOP version | `v1`                                                                  |
| Topic                | Technical infrastructure & software development                       |
| Template SOP Type    | Node-specific SOP                                                      |
| GDI Node             |                                                                       |
| Instance version     |                                                                       |

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

| Template Version | Instance version | Author(s)                   | Description of changes                                                                                                                                               | Date         |
| ---------------- | ---------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| `v1`             |                  | Liina Nagirnaja, Oriol López-Doriga Sagalés | First version of the SOP for GitHub issue [#66](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/issues/66), after reviews completed. | `2026.06.09` |
| `v0`             |                  |  Liina Nagirnaja, Oriol López-Doriga Sagalés       | Initial version of the SOP for GitHub issue [#66](https://github.com/GenomicDataInfrastructure/standard-operating-procedures/issues/66), based on the approved draft and reviewed copy.                                                                 | `2026.04.30` |

### 2. Glossary

Find GDI SOPs common Glossary at the [**charter document**](../../docs/GDI-SOP_charter.md).

| Abbreviation  | Description                                       |
| ------------- | ------------------------------------------------- |
| AF            | Allele Frequency                                  |
| CRG           | Centre for Genomic Regulation                     |
| DKFZ           | Deutsches Krebsforschungszentrum                   |
| GDI           | European Genomic Data Infrastructure              |
| GDPR          | General Data Protection Regulation.               |
| EBI           | European Bioinformatics Institute                 |
| EMBL          | European Molecular Biology Laboratory             |
| FAIR          | Findability, Accessibility, Interoperability and Reusability             |
| HD               | Helpdesk                                                                |
| HTTPS          | Hypertext Transfer Protocol Secure                     |
| ID            | Identifier                                        |
| SOP           | Standard Operating Procedure                      |
| UM            | University of Maribor                             |
| VHD           | Virtual Helpdesk                                  |

| Term          | Definition                                                                                                |
| ------------- | ----------------------------------------------------------------------------------------------------------|
| Beacon query         | HTTPS request to an endpoint of the node’s Allele Frequency beacon.                                        |
| Dataset permissions   | All the information related to the dataset grants and its security level configuration.                   |

### 3. Roles and Responsibilities

See qualifications and responsibilities of the roles at the [**Organisational Roles and Responsibilities**](../../docs/GDI-SOP_organisational-roles-and-responsibilities.md) document.

| Role       | Full name                   | GDI/node role                                    | Organisation                          |
| ---------- | --------------------------- | ------------------------------------------------ | ------------------------------------- |
| Author     | Liina Nagirnaja             | Beacon Manager                                   | CRG                                   |
| Author     | Jordi Rambla                | Beacon Product Owner                             | CRG                                   |
| Author     | Oriol López-Doriga Sagalés  | Beacon Developer                                 | CRG                                   |
| Reviewer   | Wasiu Akanni                   | Task 4.3 member                                  | DKFZ                                   |
| Reviewer   | Aleš Čep                    | Task 4.3 member                                  | UM                                   |
| Reviewer   | Marcos Casado Barbero       | Task 4.3 member                                  | EMBL-EBI                              |
| Approver   | Gabriele Rinck              | Task 4.3 member                                  | EMBL-EBI                              |
| Authorizer | Management Board            | Authorizer according to GDI SOP governance       | GDI                                   |

### 4. Purpose

Data loaded into GDI, be it through beacon or through FAIR Data Points (FDP), need to be consistent and queryable. This SOP aims to clarify how to proceed when new dataset metadata needs to be added to a Node's beacon, covering the cases for updating or inserting datasets and full validation of the incoming metadata. 

### 5. Scope

The SOP covers node-level guidance for uploading dataset metadata to beacon  and includes:
- Dataset metadata preparation and check that the dataset ID matches FDP requirements (GH)
- Entering dataset metadata to beacon (dataset ID and name)
- Validating the dataset endpoint with Verifier

Out of scope for this SOP are:
- Full GDI HD management entry or validation
- Uploading variant records to beacon. For MAP1, the specific requirements are covered in the beacon guidelines documentation ([here](https://docs.google.com/document/d/1LLzp6zZT3fSM1XxOXHuRqwJje1v726Z2/edit?rtpof=true&tab=t.0) and [here](https://docs.google.com/document/d/1rc0591dFHNghAYqv3SE6pNkfFmGrQgWAemmR1Iek3ss/edit?tab=t.0)).
- Broader validation across services

### 6. Introduction and Background Information

Dataset metadata provides the foundation for discovering related data across the different GDI platforms and databases. When supplying the dataset metadata for a beacon, a kind of a linkage or contract between the boundaries of the beacon and the rest of the GDI components is being set. If the dataset metadata is wrong, these connections across all GDI components will fail, hence the importance of having a SOP for each component, in this case for beacon, that reduces the chances of this information to be misloaded.
For a broader context of GDI SOPs, please refer to the [Charter](../../docs/GDI-SOP_charter.md#4-introduction).

### 7. Summary or Context Diagram

```mermaid
flowchart TD;
  A["Generate metadata file with the dataset's information"] --> B{"Confirm the type of operation to perform"}
  A -- Failure --> D["Record failure details and report to VHD"]
  B -- Insert new --> C["Insert metadata for new dataset"]
  B -- Update existing --> E["Update metadata for existing dataset"]
  C -- Failure --> D["Record failure details and report to VHD"]
  E -- Failure --> D["Record failure details and report to VHD"]
  C -- Success --> F["Add permissions for your new dataset"]
  F -- Success --> I["Make additional statements for your dataset"]
  E -- Success --> G["Validate your new dataset's metadata record with verifier, log and report completion"]
  F -- Success --> G["Validate your new dataset's metadata record with verifier, log and report completion"]
  G -- Valid --> H["Record the action in the local audit or change log, including who performed the change, when it was performed, what was changed and the approved scope"]
  G -- Invalid --> D["Record failure details and report to VHD"]
  I --> G["Validate your new dataset's metadata record with verifier, log and report completion"]
```

### 8. Procedure

#### 8.1. Generate metadata file with the dataset’s information

| Step identifier | When | Who |
| :-------------- | :------------------------------------------------------------------ | :-------------------------------------- |
| `1`             | When metadata for a new beacon dataset needs to be added or existing metadata needs to be updated. | Node beacon maintainer |

After collecting all the information related to the dataset’s metadata, create a new `datasets.csv` file with this exact name inside `/ri-tools/csv` folder (or any subfolder). Copy the headers you need from the template file `/ri-tools/csv/templates/datasets.csv`. Make sure the following mandatory headers are included:
```yaml
id
name
```
Fill in the metadata in the row after the header. Ensure that the id  follows the required [Dataset SHACL](https://raw.githubusercontent.com/GenomicDataInfrastructure/gdi-metadata/refs/heads/main/Formulasation(shacl)/core/PiecesShape/Dataset.ttl), which needs to be consistent with the SHACL that the Node is currently using in their FDP and doesn't need to be the latest version from the gdi metadata repository.
Next step is to tell the ri-tools tool where the metadata file is stored. In `/ri-tools/conf/conf.py` update the value of the `csv_folder` configuration variable so that it points to the folder containing the dataset metadata file, datasets.csv. Example:
```python
csv_folder = './csv/'
```
The folder may be any folder you create for this purpose, but it must contain only the relevant datasets.csv file for the dataset being uploaded. Do not include metadata files from other datasets or templates in the same folder.
Once done, execute next the script to generate a JSON file with the metadata for your dataset from the CSV you just created:
```bash
docker exec -it ri-tools python csv_to_bff.py
```
- If the file has been successfully created, proceed to ⏩[Step 2](#82-confirm-the-type-of-operation-to-perform).
- If you encounter any issues, record the response obtained from the used commands, adding all the information about the actions performed and the intended goal of performing them and report to the GDI Virtual Helpdesk so that requester communication continues through the VHD workflow.


#### 8.2. Confirm the type of operation to perform

| Step identifier | When | Who |
| :-------------- | :------------------------------------------------------------------ | :-------------------------------------- |
| `2`             | After successfully completing ⏩[Step 1](#81-generate-metadata-file-with-the-datasets-information). | Node beacon maintainer |

As the node beacon maintainer, confirm that the incoming request package is complete before performing any modification in beacon. Double check first:
- What dataset’s metadata needs to be uploaded
- If the dataset was already uploaded in the beacon
Send an HTTPS GET request to your beacon’s datasets endpoint and locate the record corresponding to the ID of the dataset regarding the metadata to be added, use the method you prefer (e.g., curl, postman...)...",
```bash
curl 'https://<yourBeaconDomain>/api/datasets'
```
or perform the dataset ID beacon query directly,
```bash
curl 'https://<yourBeaconDomain>/api/datasets/<id>'
```
- If the dataset ID to upload metadata for was not found, you will need to perform an insert, proceed to ⏩[Step 3.1](#831-insert-metadata-for-new-dataset)
- If the dataset ID to upload metadata for was found, proceed to ⏩[Step 3.2](#832-update-metadata-for-existing-dataset)


#### 8.3. Adding dataset's metadata into beacon

| Step identifier | When | Who |
| :-------------- | :--------------------------------------- | :-------------------------------------- |
| `3`             | After confirming the type of operation to perform. | Node beacon maintainer |

##### 8.3.1. Insert metadata for new dataset

| Step identifier | When | Who |
| :-------------- | :--------------------------------------- | :-------------------------------------- |
| `3.1`             | After confirming that the type of operation to perform is to insert metadata for a new dataset. | Node beacon maintainer |

Insert the dataset’s metadata file into beacon by executing the following commands:
```bash
docker cp ri-tools/output_docs/datasets.json mongoprod:tmp/datasets.json

bash -c '
read -s -p "Mongo user: " MONGO_USER; echo
read -s -p "Mongo password: " MONGO_PASS; echo

docker exec -i mongoprod <<EOF mongoimport --jsonArray --uri "mongodb://${MONGO_USER}:${MONGO_PASS}@127.0.0.1:27017/beacon?authSource=admin" --file /tmp/datasets.json --collection datasets
EOF
'
```
You will be asked to enter the mongodb credentials on the terminal prompt.
- If the insertion was successful, proceed to ⏩[Step 4](#84-add-permissions-for-your-new-dataset).
- If the insertion was not successful, record the response obtained from the used commands, adding all the information about the actions performed and the intended goal of performing them and report to the GDI Virtual Helpdesk so that requester communication continues through the VHD workflow.

##### 8.3.2. Update metadata for existing dataset

| Step identifier | When | Who |
| :-------------- | :--------------------------------------- | :-------------------------------------- |
| `3.2`             | After confirming that the operation to perform is a dataset’s metadata update. | Node beacon maintainer |

Insert the dataset’s metadata file into beacon by executing the following commands:
```bash
docker cp ri-tools/output_docs/datasets.json mongoprod:tmp/datasets.json

bash -c '
read -s -p "Mongo user: " MONGO_USER; echo
read -s -p "Mongo password: " MONGO_PASS; echo


docker exec -i mongoprod mongosh \
"mongodb://${MONGO_USER}:${MONGO_PASS}@127.0.0.1:27017/beacon?authSource=admin" \
--eval "
const fs = require(\"fs\");
const updates = JSON.parse(fs.readFileSync(\"/tmp/datasets.json\", \"utf8\"));


updates.forEach(doc => {
  const { id, _id, ...fieldsToUpdate } = doc;


  const res = db.datasets.updateOne(
    { id },
    { \$set: fieldsToUpdate }
  );


  printjson(res);
});
"
'
```
You will be asked to enter the mongodb credentials on the terminal prompt.
- If the update was successful, proceed to ⏩[Step 5](#85-make-additional-statements-for-your-dataset).
- If the update was not successful, record the response obtained from the used commands, adding all the information about the actions performed and the intended goal of performing them and report to the GDI Virtual Helpdesk so that requester communication continues through the VHD workflow.

#### 8.4. Add permissions for your new dataset

| Step identifier | When | Who |
| :-------------- | :--------------------------------------- | :-------------------------------------- |
| `4`             | After successfully inserting new dataset metadata ⏩[Step 3.1](#831-insert-metadata-for-new-dataset). | Node beacon maintainer |

In beacon container, add the dataset ID to the file in path `/beacon/permissions/datasets/datasets_permissions.yml` and add a new item under it with the security level as the first property, and default_entry_types_granularity as the mandatory property under the security level:
```yaml
<dataset id>
   public:
      default_entry_types_granularity: record
```
This is only an example, set the security level as it is meant for the dataset and add further restrictions as needed. More information about security levels and granularity types can be found in the [beacon2 pi repository"](https://github.com/EGA-archive/beacon2-pi-api/tree/main#making-a-dataset-publicregisteredcontrolled).
Verify that your dataset appears correctly by sending an HTTPS GET request to your beacon’s datasets endpoint and locate the record corresponding to the ID of the dataset to be inserted, use the method you prefer (e.g., curl, postman...)...",
```bash
curl 'https://<yourBeaconDomain>/datasets'
```
or perform the ID beacon query directly,
```bash
curl 'https://<yourBeaconDomain>/api/datasets/<id>'
```
- If the dataset appears and you wish it to declare either if it is test mode, synthetic or deprecated, proceed to ⏩[Step 5](#85-make-additional-statements-for-your-dataset).
- If the dataset appears, and you don’t wish to make additional declarations for your dataset, proceed to ⏩[Step 6](#86-validate-your-new-datasets-metadata-record-with-verifier-log-and-report-completion).
- If the dataset is not found, record the response obtained from the used commands, adding all the information about the actions performed and the intended goal of performing them and report to the GDI Virtual Helpdesk so that requester communication continues through the VHD workflow.

#### 8.5. Make additional statements for your dataset

| Step identifier | When | Who |
| :-------------- | :--------------------------------------- | :-------------------------------------- |
| `5`             | After successfully updating new dataset metadata ⏩[Step 3.2](#832-update-metadata-for-existing-dataset), after adding permissions for the new dataset ⏩[Step 4](#84-add-permissions-for-your-new-dataset) or after making additional declarations for your dataset ⏩[Step 5](#85-make-additional-statements-for-your-dataset). | Node beacon maintainer |

In case you want your dataset to be declared as meant for test mode, specify its nature or deprecate it, you can by editing the `/beacon/conf/datasets/datasets_conf.yml` file. Add a new entry with the dataset id as the main property and add whatever three optional following items you want to declare for the dataset, setting them as `True`.
```yaml
<dataset id>
  isTest: True
  isSynthetic: True
  isDeprecated: True
```
After that, proceed to ⏩[Step 6](#86-validate-your-new-datasets-metadata-record-with-verifier-log-and-report-completion).


#### 8.6. Validate your new dataset’s metadata record with verifier, log and report completion

| Step identifier | When | Who |
| :-------------- | :--------------------------------------- | :-------------------------------------- |
| `6`             | After successfully updating new dataset metadata ⏩[Step 3.2](#832-update-metadata-for-existing-dataset), after adding permissions for the new dataset ⏩[Step 4](#84-add-permissions-for-your-new-dataset) or after making additional declarations for your dataset ⏩[Step 5](#85-make-additional-statements-for-your-dataset). | Node beacon maintainer |

As the node beacon maintainer, proceed to validate your new dataset metadata by running the [beacon verifier](https://beacon-verifier-demo.ega-archive.org/) on your beacon instance. In case the service is not operative, please, proceed to [download and run the software locally](https://github.com/EGA-archive/beacon-verifier-v2) in order to verify your beacon.
Focus on the `/datasets` endpoint.
- If the endpoint is valid, record the action in the local audit or change log, including who performed the change, when it was performed, what was changed and the approved scope.
- If the endpoint is not valid, record the response obtained from the used commands, adding all the information about the actions performed and the intended goal of performing them and report to the GDI Virtual Helpdesk so that requester communication continues through the VHD workflow.

### 9. References

| Reference | Description |
| --------- | ----------- |
| [1](../../docs/GDI-SOP_charter.md) | European GDI - SOP Charter (including Glossary) |
| [2](../../docs/GDI-SOP_information-service-management.md) | European GDI - Procedures for Information Service Management for SOPs |
| [3](../../docs/GDI-SOP_organisational-roles-and-responsibilities.md) | European GDI - Organisational Roles and Responsibilities |
| [4](https://github.com/EGA-archive/beacon2-ri-tools-v2/tree/main) | EGA - Beacon v2 RI Tools v2 |
| [5](https://github.com/EGA-archive/beacon2-pi-api/tree/main) | EGA - Beacon v2 Production Implementation |
