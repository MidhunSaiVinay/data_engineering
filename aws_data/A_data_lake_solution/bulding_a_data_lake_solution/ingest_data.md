# Ingesting data into a data lake

---

## AWS DMS (Data Migration Service)

AWS DMS can ingest data into your AWS data lake from various data stores such as relational databases, NoSQL databases, and data warehouses.

It can migrate data from database to database and from databases to other storage solutions like S3.

![DMS](aws_data/A_data_lake_solution/images/dms.png)

The source database can be located on-premises or in the cloud.

A **source endpoint** provides connection, data type store, and location information about the source data store. AWS DMS uses this information to establish a connection.

A **replication instance** is a compute resource that will be used to perform replication tasks.

There are three phases in a replication task:
1.  Migrate existing data
2.  Application of cached changes
3.  Replicate data changes only (CDC - Change Data Capture)

A **target endpoint** provides connection, data type store, and location information about the target data store. DMS uses this information to establish a connection.

### Full load
This is a one-time migration of existing data. Any changes that occur during this initial migration are cached.

### Application of cached changes
After the full load, AWS DMS begins applying the changes that occurred up to that point.

After the full load task is completed, AWS DMS begins to collect changes as transactions for the ongoing replication phase. After AWS DMS applies all cached changes, tables are transactionally consistent. At this point, AWS DMS moves to the ongoing replication phase.

### Ongoing Replication
AWS DMS reads changes from the source database transaction logs, extracts these changes, converts them to the target format, and applies them to the target. This process provides near real-time replication to the target, reducing the complexity of replication monitoring.

The following are two types of CDC workloads:
* Insert-only operations
* Full CDC, which includes update and delete operations

---

## AWS DataSync
AWS DataSync is a data transfer service optimized for moving large volumes of file-based and object data to, from, and between AWS storage services.

DataSync automatically scales and handles scheduling, monitoring, encryption, and verification of your file and object transfers. With DataSync, you pay only for the amount of data copied, with no minimum commitments or upfront fees.
