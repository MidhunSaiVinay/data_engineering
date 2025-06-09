# Designing the Data Warehouse Solution

## goals of a data warehouse

oltp systems capture and maintain transaction data

business use enterprise resource planning(ERP) software or systems to plan and manage daily activities erp systems can support supply chain manufacturing  services financials abd other business processes.

customer resource management (CRM) system complies data form various communicatio channels including email live chat and marketing emails

line of business (lob) applications are large programs with integrations to databases and database management systems.

the prolifiration of seperate heterogeous databases eads to data seggregation or data silos making it difficult to obtain complete view of enterprise

the main goal of the data warehouse os to consolidate data from various sources such as transactional systems operational databases and external sources into a centralised repository.

amazon redshift is a amazons data warehousing solution is a rbdms altough it has sma e functionality of rdbms it is highlt optimised for perfomance and reporting

![data warehouse arch](aws_data/A_data_warehouse_solution/images/datawarehouse.png)

modren data architecture combines the benifits of data lake and data warehouse architerctures and provides stragetic vision combining aws data and data analytics services into multi purpouse data processing and analytics environments

## Provisions or serverless

we provisiong redshift we have two options 

provisioned and serverless

we cna distinguish them by compute resources , cost and storage options

### redshift provisioned

red shift provisioned is the traditional deployment model of amazon redshift in this we provision a cluster with specific number of nodes and each node has specific amount of compute resources such as cpu and ram and storage 

![Redshift provisioned](aws_data/A_data_warehouse_solution/images/redshift_provisioned.png)

