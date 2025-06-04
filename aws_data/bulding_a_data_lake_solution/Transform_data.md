# Transform data

## Processing the data 
ingested data will be in diffrent varying formats and quality it needs to be processed for later analysis stages

The terms preparation, cleansing, and transforming are often used to describe actions in the processing stage. Those actions are performed using extract, transform, and load (ETL) functions. 

Extract: Gathering data from a variety of data sources
Transform: Systematically changing raw data into useable formats
Load: Moving the transformed data into data lake storage or another location

## multiple ways to transform and clean data

### bigdata processing

Amazon emr on ec2 clusters

amazon emr sererless

amazon emr on eks clusters

### Amazon Athena
Impromptu log analysis

report generation

business intelligence

### amazon event bridge with aws step function and amazon managed workflow for apache airflow 
for scheduling and orchestration

## AWS Glue

aws glue is a serverless data integration service that makes it convinent to integrate data from multiple sources.

as it is serverless we dont need to proviosn or configure any infra

aws glue is a multi-facated service and provides a wide range of features and functions for processing data

we can develop etl jobs in aws glue with visual etl notebooks script editor with sagemakerstudio and local ides in each caser we nwwd to run code in underlyinf serverless distributed spark engine

![AWS Glue overview](aws_data/images/glue_overview.png)

## connectors

A connector is a pice of code that facilitates communication between aws glue and dta store

we can use built-i connectors or connectors offered in aws marketplace

Examples of connectors include the following:

Data warehouses: Amazon Redshift
Data lakes: Amazon S3
Relational databases: JDBC, Amazon Aurora, MariaDB, MySQL, Microsoft SQL server, Oracle Database, PostgreSQL
Non-relational databases: Amazon DocumentDB, MongoDB, Amazon OpenSearch
Streams: Apache Kafka, Amazon Kinesis
Other cloud providers

## Discovery and cataloging
Data will likely be stored in several formats with varying quality and accessibility. After being ingested into the data lake storage, it needs to be cataloged so that it is searchable. 

## Glue data catalog
