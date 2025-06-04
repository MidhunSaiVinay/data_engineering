# Build Data Catalog

---

## Data Catalog
The AWS Glue Data Catalog is a central metadata repository for all data assets stored in data lake locations.

The Data Catalog integrates seamlessly with other AWS analytics services such as the following:

* **Amazon Athena** relies on the Data Catalog to store and retrieve metadata about the data sources (tables, columns, data types, and so on) that you want to query.
* **Amazon EMR** can directly access the metadata stored in the Data Catalog so it can understand the structure and location of the data it needs to process.

We can use metadata in the catalog to query and transform data in a consistent manner across a wide variety of applications.

An example of a Data Catalog table entry includes:

| Field             | Description                                                                                                                              |
| :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| Name              | This is the name of the table.                                                                                                           |
| DatabaseName      | This is the database the table belongs to.                                                                                                 |
| StorageDescriptor | This defines the physical storage properties of the data, such as:<br>- Data format (for example, .csv, Parquet)<br>- Location of the data in Amazon S3<br>- Serialization and deserialization libraries |
| Schema            | This includes the schema (column names and data types), such as:<br>- `name: string`<br>- `year: integer`<br>- `price: double`                   |
| PartitionKeys     | These are the columns used to partition the data, which can improve query performance.                                                     |

The following is an example of data partitioned by day, with ingested data for 2 days:
* Partition1: `[year=2024/month=3/day=13]` => Location = `s3://doc-example-bucket/data/mytable/year=2024/month=3/day=13`
* Partition2: `[year=2024/month=3/day=14/]` => Location = `s3://doc-example-bucket/data/mytable/year=2024/month=3/day=14/`

| Field       | Description                                                                                                         |
| :---------- | :------------------------------------------------------------------------------------------------------------------ |
| Parameters  | These are key-value pairs that store additional metadata about the table, such as the table's description, creator, and creation time. |
| Table Type  | This indicates the type of table, such as EXTERNAL_TABLE, VIRTUAL_VIEW, and so on.                                      |

---

## Populating the Catalog

Software entities called **crawlers** populate the Data Catalog. Crawlers discover the data, recognize its structure, and add metadata into the Data Catalog. Crawlers use classifiers to detect and infer schemas.

To populate the Data Catalog, we can manually add metadata or run DDL queries.

### Manually add metadata
Manually add and update table details using the AWS Glue console or by calling the API through the AWS Command Line Interface (AWS CLI).

### Run DDL queries
Run Data Definition Language (DDL) queries in Athena, AWS Glue jobs, and AWS EMR jobs.

DDL is a subset of SQL that is used to define and manage the structure of a database. It is responsible for creating, modifying, and deleting database objects, such as tables, indexes, views, stored procedures, and other database components.

---

## Crawlers

AWS Glue crawlers can scan data in all kinds of repositories, classify it, extract its schema, and store metadata automatically in the Data Catalog.

When a crawler runs:
* It uses classifiers to discover and infer the structure of the data.
* It groups data into tables or partitions.
* It populates metadata in the Data Catalog.
* It creates a single schema for each S3 path.

### Crawler Configuration

* We can configure the crawler to scan multiple data stores in a single run.
* We can schedule crawlers or invoke them based on an event to ensure metadata is up-to-date.
* It is recommended to use the default setting of always updating the Data Catalog; this way, the Data Catalog stays in sync with the data lake.
* We can also configure a crawler to scan only new subfolders and perform incremental crawls.

---

## Classifiers

When defining a crawler, we can rely on built-in classifiers or choose one or more custom classifiers to read the data and determine its structure or schema.

* **Built-in classifiers**: AWS Glue provides built-in classifiers to infer schemas from common file formats, including JSON, .csv, and Apache Avro.
* **Custom classifiers**: To configure the results of a classification, you can create a custom classifier. You provide the code for custom classifiers, and they run in the order that you specify. You define your custom classifiers in a separate operation before you define the crawlers.

---

## Data Catalog Features and Considerations
The following are some features and considerations for using the Data Catalog:

* Each AWS account has one Data Catalog in each Region.
* You can manually edit the schemas in the Data Catalog. For example, you can change column data types, add new columns, or modify table properties.
* The Data Catalog maintains a comprehensive schema version history so you can compare and review how your data has changed over time.
* You can compute column-level statistics for Data Catalog tables, such as minimum value, maximum value, total null values, and total distinct values.
* You can measure and monitor the quality of your data using the AWS Glue Data Quality service.