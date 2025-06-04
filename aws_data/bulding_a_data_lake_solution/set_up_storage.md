# Set up storage
To set up storage in a data lake, we use AWS S3. An example architecture would look like this:

![Example Diagram](aws_data/images/s3-storage_setup.png)

S3 full form is Simple Storage Service.

## S3 standard
This is standard S3 storage.

## S3 standard infrequent access
Files that are infrequently accessed are stored here. The cost of storage is less, but the cost of retrieval is high.

## Glacier Deep Archive
Archival files are stored here. The cost of retrieval is high.

## S3 intelligent-tiering
This automatically moves data to whichever storage class is most cost-effective.

## S3 Glacier Instant Retrieval
This is low-cost storage for long-lived data that is accessed a few times each year and requires milliseconds retrieval.

## S3 Glacier Flexible Retrieval
This is low-cost storage for long-lived data used for backups and archives, with bulk data retrieval from minutes to hours.

## Key benefits of AWS S3 in data lakes

### Scalability
S3 is an exabyte-scale object store for storing any type of data, including databases, JSON, XML, images, and media files. We can start small and grow the data lake as needed.

### Durability
S3 is designed to deliver 99.999999999% (11 9's) data durability. S3 automatically creates copies and stores them in three Availability Zones. However, S3 One Zone-Infrequent Access creates copies in only one zone.

### Security
S3 is designed to provide security across all storage classes, including identity and access management, inventory scanning, and automatic encryption.

### Availability
Amazon S3 storage classes are designed to provide a range of availability between 99.5% and 99.99% in a given year. This is backed by a Service Level Agreement (SLA).

### Cost
On S3, you pay for the data storage and data processing that you actually use, as you use them.

# Data lake zones or layers

![Example Diagram](aws_data/images/data_lake_zone.png)

## Landing zone
When working with sensitive data, it is recommended to use an additional S3 bucket as a landing zone to mask the data before it is moved to the raw zone.

## Logs zone
This zone is used for logs for Amazon S3 and other services.

## Archived zone
This zone is used for infrequently accessed historic data.

## Sandbox Zone
This zone is used for exploratory analysis and experimentation.

# S3 Life Cycle Policies

Lifecycle policies can be helpful to decide when to transition to the right storage class.

Guidelines to consider:

* If your bucket is versioned, ensure that there is a rule action for both current and noncurrent objects to either transition or expire.
* If you are uploading objects using multipart upload, there might be situations when the uploads fail or do not finish. The incomplete uploads remain in your buckets and are chargeable. You can configure lifecycle rules to automatically clean up incomplete multipart uploads after a certain time period.
* To have a single lifecycle policy for all the source datasets (instead of one for each source prefix), you can keep all source data under one prefix.
* S3 Lifecycle transition costs are directly proportional to the number of objects transitioned. Reduce the number of objects by aggregating or zipping and compressing them before moving them to archive tiers.

# Additional Amazon S3 optimization techniques

Use S3 object tagging to control access, analyze usage, manage lifecycle policies, and replicate objects.