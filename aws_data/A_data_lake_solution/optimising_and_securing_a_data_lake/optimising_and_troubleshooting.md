# Consolidated Notes: Data Lakes on AWS

## I. Open Table Formats

**A. Challenges in Growing Data Lakes:**
* Efficient record-level updates and deletions.
* Managing query performance with millions of files.
* Ensuring data consistency (concurrent writers/readers).
* Preventing data corruption from write failures.
* Evolving table schemas without rewriting datasets.

**B. Role of Open Table Formats:**
* Provide database-like functionality to simplify optimization and management of transactional data lakes.
* Open-source libraries for efficient organization, storage, querying, and processing of data files in data lakes (especially on AWS).

**C. Examples:**
* Apache Iceberg
* Apache Hudi
* Delta Lake

**D. Key Features:**
* Data compaction
* Time travel (accessing historical versions of data)
* Reduction of file listing operations via metadata files

**E. Using Apache Iceberg on AWS:**
1.  **Creation & Writing**: Create Iceberg table and write data (e.g., via Athena).
2.  **Cataloging**: Table becomes available in AWS Glue Data Catalog.
3.  **Ingestion**: Batch/streaming ingestion (Amazon EMR, AWS Glue, Apache Flink). Data/metadata in Amazon S3.
4.  **Querying**: Use Athena, Redshift Spectrum, etc.

---
## II. Security Using AWS Lake Formation

**A. Core Security Aspects for Data Lakes:**
* Data network security
* Access management
* Regulatory compliance
* Sensitive data protection

**B. Key AWS Security Services:**
* **IAM (Identity and Access Management)**: For user/role management and policy configuration (e.g., S3 bucket access, Glue API permissions).
* **AWS CloudTrail**: For logging and monitoring API calls.
* **Amazon Macie**: For discovering and protecting sensitive data.
* **AWS Key Management Service (KMS)**: For managing encryption keys.

**C. Security Components & Roles:**

1.  **IAM (Identity and Access Management):**
    * Manages users, groups, roles, and access levels.
    * Configures access control policies (resource, action, condition-based).
    * Grants/denies access to AWS resources/services.

2.  **AWS Lake Formation:**
    * Integrates with AWS Glue Data Catalog for metadata management.
    * Centralized, fine-grained data access control policy store.
    * Enables analytics tools to enforce user permissions.
    * Provides audit logs for data access/changes.

3.  **AWS Glue Data Catalog:**
    * Central metadata repository (for S3 data, etc.).
    * Lake Formation sets column/row-level permissions on catalog metadata.

**D. IAM and Lake Formation Integration:**
* IAM handles authentication/authorization (including for Lake Formation).
* IAM policies define permissions for Lake Formation resources/data.
* Lake Formation adds specific data lake governance (fine-grained access, tagging).
* Permissions can be assigned to: IAM users/roles, IAM Identity Center users/groups, SAML 2.0/Quicksight users/groups, external AWS accounts/orgs/users/roles.

**E. Major Steps for Setting Up Data Lake Security:**
1.  Configure IAM.
2.  Enable Lake Formation in the AWS region.
3.  Register data sources with Lake Formation.
4.  Define data access policies in Lake Formation.
5.  Integrate Lake Formation permissions with other AWS services (Athena, EMR, etc.).
6.  Monitor and audit access and policy changes.

---
## III. Troubleshooting Data Lake Issues

**A. AWS Glue Job Failures:**
* **Logs**: Check CloudWatch logs for errors.
* **Script Logic**: Verify ETL script.
* **Resource Allocation**: Ensure sufficient memory/compute (DPUs); increase if needed.
* **Dependencies**: Confirm upstream jobs/data availability.
* **Endpoints**: Check health/accessibility of service endpoints.

**B. Data Format Incompatibilities:**
* **Input Data**: Analyze format, schema, sample records.
* **Transformation Code**: Verify handling of input format (including complex structures).
* **Target Format**: Ensure output matches target system expectations.

**C. Data Quality Issues:**
* **Checks**: Implement validation/cleansing in transformation logic.
* **Evaluate Periodically**: Use AWS Glue Data Quality for monitoring.
* **Error Handling**: Implement robust mechanisms (e.g., dead-letter queues).

**D. Insufficient Permissions:**
* **IAM Roles**: Verify necessary permissions for transformation jobs (S3 access, Glue API, KMS).
* **Resource Policies**: Check S3 bucket policies, KMS key policies for denials.
* **Lake Formation Permissions**: Confirm grants for data locations, catalogs, tables, columns if Lake Formation is used.

**E. Performance Issues:**

| Issue                          | Troubleshooting Recommendations                                                                                                                                                                                                                                                                |
| :----------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Slow Data Processing** | Analyze ingestion; optimize storage (partitioning, compaction, columnar formats like Parquet); use purpose-built stores (e.g., Kinesis for real-time); rightsize compute resources; optimize code/queries; use monitoring (e.g., Spark UI).                                                      |
| **Excessive Resource Consumption** | Optimize storage (compression, deduplication, S3 Lifecycle); rightsize compute resources (use auto-scaling); explore serverless options (Glue, EMR Serverless, Athena).                                                                                                                            |

**F. Data Governance and Access Control Issues:**
* **Cataloging**: Use Lake Formation for centralized catalog and granular access controls.
* **Data Protection**: Implement masking/tokenization for sensitive data (PII).
* **IAM Review**: Regularly update IAM roles/policies for least privilege.