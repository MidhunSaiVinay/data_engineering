# Quick 15-Min Data Lake Revision Notes

---

## 1. S3 for Data Lake Storage

* **S3 (Simple Storage Service)**: Foundation for data lakes; exabyte-scale object storage.
* **Key Benefits**:
    * **Scalability**: Start small, grow as needed.
    * **Durability**: 99.999999999% (11 9's).
    * **Security**: IAM, encryption, inventory scanning.
    * **Availability**: 99.5% - 99.99% (SLA backed).
    * **Cost-effective**: Pay for what you use.
* **Common S3 Storage Classes**:
    * **S3 Standard**: Frequently accessed data.
    * **S3 Standard-Infrequent Access (S3 Standard-IA)**: Less frequent access, lower storage cost, higher retrieval cost.
    * **S3 Intelligent-Tiering**: Automatically moves data to cost-effective tiers.
    * **S3 Glacier (Instant Retrieval, Flexible Retrieval, Deep Archive)**: Archival, varying retrieval times/costs.
* **Data Lake Zones/Layers (Conceptual Buckets/Prefixes)**:
    * **Landing/Raw Zone**: Initial data dump, possibly for sensitive data masking.
    * **Processed/Curated Zone**: Cleaned, transformed data.
    * **Logs Zone**: Service logs.
    * **Archived Zone**: Infrequently accessed historic data.
    * **Sandbox Zone**: Experimentation.
* **S3 Lifecycle Policies**: Automate data transition between storage classes (e.g., move old data to Glacier) or expire data.
    * Consider for versioned objects (current/noncurrent).
    * Clean up incomplete multipart uploads.
    * Aggregate small objects before archiving to save on transition costs.
* **Optimization**: Use S3 object tagging for access control, cost tracking, lifecycle management.

---

## 2. Ingesting Data

* **AWS DMS (Data Migration Service)**:
    * Migrates data from various sources (relational DBs, NoSQL, data warehouses) to S3 or other databases.
    * **Components**: Source Endpoint, Replication Instance, Target Endpoint.
    * **Phases**:
        1.  **Full Load**: Initial data migration.
        2.  **Application of Cached Changes**: Applies changes during full load.
        3.  **Ongoing Replication (CDC - Change Data Capture)**: Replicates ongoing changes near real-time.
* **AWS DataSync**:
    * Optimized for moving large volumes of file-based/object data to/from/between AWS storage services (like S3).
    * Handles scheduling, monitoring, encryption, verification.

---

## 3. Building Data Catalog (Metadata Management)

* **AWS Glue Data Catalog**:
    * Central metadata repository for data assets in the data lake.
    * Integrates with Athena, EMR, Redshift Spectrum.
    * **Key Table Info**: Name, Database, StorageDescriptor (format, location, SerDe), Schema (columns, types), PartitionKeys.
* **Populating the Catalog**:
    * **Crawlers**: Automatically scan data (S3, JDBC sources), infer schema, classify data, and populate the Data Catalog.
        * Use built-in or custom **classifiers** (e.g., for JSON, CSV, Parquet, Avro, or custom logic) to determine schema.
        * Can be scheduled or event-driven.
        * Can perform incremental crawls.
    * **Manually**: Via AWS Glue console or CLI.
    * **DDL queries**: Via Athena, Glue jobs, EMR.
* **Data Catalog Features**:
    * One catalog per AWS account per Region.
    * Schema version history.
    * Column-level statistics.
    * Integration with AWS Glue Data Quality.

---

## 4. Transforming Data (ETL/ELT)

* **Goal**: Cleanse, prepare, and transform raw data into usable formats.
* **AWS Glue (ETL Service)**:
    * **Serverless** data integration service.
    * Develop ETL jobs using visual tools, notebooks, or scripts (Python/Scala) running on Apache Spark.
    * **Connectors**: Facilitate communication with data stores (S3, Redshift, JDBC, Kafka, etc.).
    * Uses Glue Data Catalog for source/target metadata.
* **Other Transformation Options**:
    * **Amazon EMR**: Managed Hadoop framework (Spark, Hive, Presto) for big data processing on EC2 clusters, Serverless, or EKS.
    * **Amazon Athena**: Can be used for some SQL-based transformations, especially for creating new tables from query results (CTAS).
* **Orchestration**:
    * AWS Step Functions, Amazon Managed Workflows for Apache Airflow (MWAA).

---

## 5. Serving Data for Consumption

* **Amazon Athena**:
    * **Serverless interactive query service** to analyze data directly in S3 using standard SQL.
    * Pay-per-query (based on data scanned).
    * Uses AWS Glue Data Catalog for schema.
    * **Schema-on-read**: Defines schema at query time.
    * Ideal for ad-hoc analysis, BI, log analysis.
    * Optimize with columnar formats (Parquet, ORC), partitioning, compression.
* **Amazon QuickSight**:
    * **Serverless BI service** for creating interactive dashboards and visualizations.
    * Connects to Athena, S3, Redshift, RDS, and other sources.
    * **SPICE**: In-memory calculation engine for fast query performance.
    * ML-powered insights (anomaly detection, forecasting).
    * Pay-per-session or capacity-based pricing.
* **Amazon Redshift**:
    * **Cloud data warehouse** for complex analytical queries.
    * **Redshift Spectrum**: Allows querying data directly in S3 from Redshift (similar to Athena but within Redshift).
* **Amazon SageMaker**: For ML, can access data from S3 or via Athena to build, train, deploy models.
* **AWS Lake Formation**: Simplifies building, securing, and managing data lakes; provides fine-grained access control for consumption tools.