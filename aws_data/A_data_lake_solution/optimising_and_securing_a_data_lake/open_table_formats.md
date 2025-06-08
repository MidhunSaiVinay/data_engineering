# Open Table Formats

As data lakes grow, they can create special challenges such as:

* Performing efficient record-level updates and deletions.
* Managing query performance as tables grow to millions of files.
* Ensuring data consistency across multiple concurrent writers and readers.
* Preventing data corruption when write operations fail.
* Evolving table schemas over time without rewriting datasets.

To help overcome these challenges, open table formats provide additional database-like functionality. This simplifies optimization and management overhead of transactional data lakes.

Open table formats are open-source libraries designed to efficiently organize data files into tables within data lake solutions. They provide efficient storage, querying, and processing capabilities for data lakes running on AWS services.

Some open-source table formats are:

* Apache Iceberg
* Apache Hudi
* Delta Lake

The following are additional features of open table formats:

* Data compaction
* Time travel
* Reduction of file listing operations through metadata files

---
## Using Apache Iceberg on AWS

Iceberg is widely used in AWS for its performance and scalability.

To use Apache Iceberg, follow these steps:
1.  Create an Iceberg table and write data into it using Athena or compatible tools.
2.  After the table is created, it becomes available in the AWS Glue Data Catalog.
3.  Perform batch or streaming ingestion with Amazon EMR, AWS Glue, or Apache Flink (AWS managed). Data and metadata files are stored in Amazon S3.
4.  Query the tables using Athena, Redshift Spectrum, or other compatible services.

![iceberg](aws_data/A_data_lake_solution/images/iceberg.png)