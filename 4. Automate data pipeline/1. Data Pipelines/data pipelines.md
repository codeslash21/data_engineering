
# Data Pipeline
A data pipeline describes, in code, a series of sequential data processing steps. Depending on the data requirements for each step, some steps may occur in parallel. Data pipelines also typically occur on a schedule. Extract, transform and load (ETL), or extract, load, and transform (ELT), are common patterns found in data pipelines, but not strictly required. Some data pipelines perform only a subset of ETL or ELT. Data Pipelines provide a set of logical guidelines and a common set of terminology. The conceptual framework of data pipelines will help you better organize and execute everyday data engineering tasks. Examples of data pipelines:
- Personalized emails that are triggered after a data pipeline executed.
- Companies commonly use data pipelines to orchestrate the analysis that determines pricing. For example, a rideshare app where you were offered real-time pricing.
- Bikeshare company, that wants to figure out where their busiest locations are. They might use this data to determine where to build additional locations, or simply to add more bikes. A data pipeline to accomplish this task would likely first load application event data from a source such as S3 or Kafka. Second, we might take that data and then load it into an analytic warehouse such as RedShift. Then third, perform data transformations that identify high-traffic bike docks.

![image](https://github.com/codeslash21/data_engineering/assets/32652085/b7fd1828-c7a5-407c-b6fb-0efe1323e0ac)

## ETL VS ELT
ETL is normally a continuous, ongoing process with a well-defined workflow. ETL first extracts data from homogeneous or heterogeneous data sources. Then, data is cleansed, enriched, transformed, and stored either back in the lake or in a data warehouse.

ELT (Extract, Load, Transform) is a variant of ETL wherein the extracted data is first loaded into the target system. Transformations are performed after the data is loaded into the data warehouse. ELT typically works well when the target system is powerful enough to handle transformations. Analytical databases like Amazon Redshift and Google BigQuery.

## Apache Kafka
Apache Kafka is an open-source stream-processing software platform developed by Linkedin and donated to the Apache Software Foundation, written in Scala and Java. The project aims to provide a unified, high-throughput, low-latency platform for handling real-time data feeds. Its storage layer is essentially a massively scalable pub/sub message queue designed as a distributed transaction log, making it highly valuable for enterprise infrastructures to process streaming data.

## Redshift
Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud. You can start with just a few hundred gigabytes of data and scale to a petabyte or more... The first step to create a data warehouse is to launch a set of nodes, called an Amazon Redshift cluster. After you provision your cluster, you can upload your data set and then perform data analysis queries. Regardless of the size of the data set, Amazon Redshift offers fast query performance using the same SQL-based tools and business intelligence applications that you use today.

## DAG And Pipeline
- **Directed Acyclic Graphs (DAGs):** DAGs are a special subset of graphs in which the edges between nodes have a specific direction, and no cycles exist. When we say “no cycles exist” what we mean is the nodes can't create a path back to themselves.
- **Nodes:** A step in the data pipeline process.
- **Edges:** The dependencies or relationships between the nodes.

It is possible to model a data pipeline that is not a DAG, meaning that it contains a cycle within the process. However, the vast majority of use cases for data pipelines can be described as a directed acyclic graph (DAG). This makes the code more understandable and maintainable.

## Data Validation
Data Validation is the process of ensuring that data is present, correct & meaningful. Ensuring the quality of your data through automated validation checks is a critical step in building data pipelines at any organization. SOme example of data validations are
- Validate the number of rows in Redshift match the number of records in S3 after loading data from S3 to Redshift.
- Validate that the number of locations in our output table match the number of tables in the input table.

## Apache Airflow
Airflow is created by AirBnb we the goal of organizing their substantial and complicated data pipeline infrustructure into one tool, so that they could run in mission-critical environment. Another goal is team can understand at a glance how their pipelines were triggered and scheduled and how all the steps in their dag fits together. What makes Airflow popular is that it makes writing and deploying data pipelines simpler than ever before. Airflow DAGs are written in Python. Additionally, Airflow comes out of the box with integrations for widely used tools like S3, Redshift, Spark etc. If an iintegration does not exist for a tool that you want to work with, Airflow has simple interface for building that integration and sharing it with other developers. Airflow makes visualizing your DAGs easier than ever before. All the developer has to do to create a visual representation of their DAG is to write the code in python and then pull up the airflow UI. The Airflow UI automatically transforms the DAG you've written in python into a DAG visualisation, complete with a schedule, execution diagram, log output, as well as a host of other great features. 

**`start-services.sh`**
```
#!/bin/bash
# Start services that airflow depend on
# Start postgres
service postgresql start
# Start cassandra
cassandra -f -R > /var/log/cassandra.log 2>&1 &
```

**`start.sh`**
```
#!/bin/bash
# Start airflow
airflow scheduler --daemon
airflow webserver --daemon -p 3000
# Wait till airflow web-server is ready
echo "Waiting for Airflow web server..."
while true; do
  _RUNNING=$(ps aux | grep airflow-webserver | grep ready | wc -l)
  if [ $_RUNNING -eq 0 ]; then
    sleep 1
  else
    echo "Airflow web server is ready"
    break;
  fi
done
```
Run the above shell scripts to start the required services such as Airflow scheduler, web server and other components. These services are essential for running and managing data pipelines using Airflow. To add Admin user to the Airflow run the following command
```
airflow users create --email student@example.com --firstname aStudent --lastname aStudent --password admin --role Admin --username admin
```
You can list all the DAGs using this command `airflow dags list`. If you see this dialog on Airflow web server UI `The scheduler does not appear to be running.`, then run the following command `airflow scheduler`.
