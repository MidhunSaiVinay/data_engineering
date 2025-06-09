# serving data for consumption

### **Amazon Redshift Spectrum**

* **Core Function**: Query structured and semi-structured data directly in **Amazon S3** without loading it into Redshift tables. 쿼리 최적화.
* **Architecture**: Uses dedicated servers independent of your cluster, pushing down compute-intensive tasks like filtering and aggregation to this layer.
* **External Tables**: You define the structure of your S3 files and register them in an external data catalog (like **AWS Glue** or a Hive metastore).
* **Benefits**:
    * **Data Lake Integration**: Seamlessly query formats like Parquet, JSON, CSV, etc., in S3.
    * **Performance**: Achieves massive parallelism and uses partition pruning to scan less data.
    * **Cost-Effective**: Pay only for the data scanned in S3, not for data storage in Redshift.
    * **Concurrency**: Multiple clusters can query the same S3 dataset simultaneously.

---

### **Federated Queries**

* **Core Function**: Query live data across operational databases (**RDS/Aurora for PostgreSQL & MySQL**), data warehouses (Redshift), and data lakes (S3) in a single query.
* **How it Works**: Redshift pushes parts of the computation down to the remote operational database to reduce data movement over the network.
* **Use Cases**:
    * Query operational data in real-time.
    * Apply transformations and ingest data into Redshift without a complex ETL pipeline.

---

### **Amazon QuickSight**

* **Core Function**: A business intelligence (BI) service for creating visualizations and dashboards from your data.
* **Query Modes**:
    * **Direct Query**: Connects directly to the data source (like Redshift) for real-time data analysis. Best for up-to-the-minute data needs.
    * **SPICE** (Super-fast, Parallel, In-memory Calculation Engine): An in-memory data store that caches data for accelerated query performance. Ideal for fast, interactive dashboards and aggregations.

---

### **Query Editor v2**

* **Core Function**: A web-based SQL client for teams to explore, analyze, and collaborate on data.
* **Key Features**:
    * **Unified Interface**: Run queries on your Redshift data warehouse, data lake (via Spectrum), and federated databases.
    * **Generative SQL**: AI assistance to help write and optimize queries.
    * **Visualization**: Create charts directly from query results (Bar, Pie, Line, Candlestick, etc.).
    * **Collaboration**: Organize and save related queries into folders.
    * **Multi-statement Queries**: Author and run scripts with multiple SQL statements.

---

### **Materialized Views**

* **Core Function**: A database object that contains the pre-computed result set of a query.
* **Purpose**: Drastically speed up complex and frequently run queries, such as large joins and aggregations, by returning pre-computed results instead of accessing the base tables.
* **Key Features**:
    * **Automatic Rewrite**: Redshift can automatically rewrite a query to use a relevant materialized view, even if the view isn't explicitly mentioned in the query.
    * **Refreshing Data**: Use the `REFRESH MATERIALIZED VIEW` statement to update the view's data.
    * **Auto-Refresh**: Configure materialized views to refresh automatically when base tables are updated or on a schedule.

---

### **Amazon Redshift ML**

* **Core Function**: Create, train, and deploy machine learning models directly within Amazon Redshift using **SQL commands**.
* **Process**:
    1.  **Prepare Data**: Use SQL to prep data.
    2.  **Create Model**: Use `CREATE MODEL` SQL statement, specifying the algorithm (e.g., XGBoost) and features.
    3.  **Train & Deploy**: Redshift ML handles the training process and deploys the model within the cluster.
    4.  **Predict**: Use the deployed model to generate predictions on new data directly in Redshift.
* **Main Benefit**: Eliminates the need to move data out of the data warehouse to a separate ML environment, simplifying the ML workflow for data analysts.

---

### **Datashares**

* **Core Function**: Securely share live, read-only data between different Amazon Redshift clusters (**producers** and **consumers**) without copying or moving the data.
* **How it Works**: A **producer** cluster creates a **datashare** (the unit of sharing) containing specific objects (schemas, tables, views, UDFs). A **consumer** cluster can then access this datashare to create a local database that references the shared data.
* **Key Features**:
    * **Live Data**: Consumers always see the most up-to-date data from the producer.
    * **Secure**: Uses AWS IAM for access control.
    * **Flexible**: Share data across different AWS accounts and regions.
    * **Types**: Includes Standard, AWS Data Exchange, and AWS Lake Formation-managed datashares.