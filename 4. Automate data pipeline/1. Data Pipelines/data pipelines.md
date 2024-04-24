
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

### DAG Example
```
import logging
import pendulum
from airflow.decorators import dag, task

# @dag decorates the greet_task to denote it's the main function. In this case @dag decorator takes one argument
@dag(
    start_date=pendulum.now()
)
def greet_flow_dag():    
    # @task decorates the re-usable hello_world_task - it can be called as often as needed in the DAG. The function decorated with task will
    # be executed when DAG run. A DAG may have more than one task. task decorator helps you to create your own operator. What operator does is
    # when you call your operator it will return a task, that task can be executed inside of our Airflow DAG. 
    @task
    def hello_world_task():
        logging.info("Hello World!")

    # hello_world represents a discrete invocation of the hello_world_task
    hello_world=hello_world_task()

# greet_dag represents the invocation of the greet_flow_dag. If we dont invoke the DAG function and assign that to a variable. And if we dont
# do that its not considered as valid DAG and it will execute inside of Airflow.
greet_dag=greet_flow_dag()
```

## Airflow Components
![image](https://github.com/codeslash21/data_engineering/assets/32652085/1bb35dcf-4d1f-448d-8478-d1b98cbcafe4)

- **Scheduler** orchestrates the execution of jobs on a trigger or schedule. The Scheduler chooses how to prioritize the running and execution of tasks within the system.
- **Work Queue** is used by the scheduler in most Airflow installations to deliver tasks that need to be run to the Workers.
- **Worker** processes execute the operations defined in each DAG. In most Airflow installations, workers pull from the work queue when it is ready to process a task. When the worker completes the execution of the task, it will attempt to process more work from the work queue until there is no further work remaining. When work in the queue arrives, the worker will begin to process it.
- **Metastore Database** saves credentials, connections, history, and configuration. The database, often referred to as the metadata database, also stores the state of all tasks in the system. Airflow components interact with the database with the Python ORM, SQLAlchemy.
- **Web Interface** provides a control dashboard for users and maintainers. Throughout this course you will see how the web interface allows users to perform tasks such as stopping and starting DAGs, retrying failed tasks, configuring credentials, The web interface is built using the Flask web-development microframework.

- Airflow is not a data processing framework. In airfflow you wont pass data in memory between steps in your DAG. Instead you will use Airflow to coordinate the movement of data between other data stores and data processing tools. Airflow can be used to run transformations, however the result of those transformations must always be stored in a destination data store at the end of each step, you will not pass data from step to step in airflow. Additionally, airflow worker has less memory and processing power individually than some data frameworks offer in aggregate. Tools like Spark are able to expose the computing power of many machines all at once, whereas with airflow you will always be llimited to the processing power of a single machine. This is why airflow developers prefer to use airflow to trigger heavy processing steps in analytics warehouses like Redshift or data framework like Spark instead of within airflow itself.

## How Airflow Works
![image](https://github.com/codeslash21/data_engineering/assets/32652085/7db28b59-cb8d-4181-90e1-a77d6368e263)

![image](https://github.com/codeslash21/data_engineering/assets/32652085/0e07d202-54da-4644-a7fe-7a7d9810b214)

## Operators
Operators define the atomic steps of work that make up a DAG. Operator is an abstract building block that can be configured to perform some work. Airflow comes with many Operators that can perform common operations. Here are a handful of common ones:
- `PythonOperator`
- `PostgresOperator`
- `RedshiftToS3Operator`
- `S3ToRedshiftOperator`
- `BashOperator`
- `SimpleHttpOperator`
- `Sensor`

### Creating a DAG
#### Using Decorator
A DAG Decorator is an annotation used to mark a function as the definition of a DAG. You can set attributes about the DAG, like: name, description, start date, and interval. The function itself marks the beginning of the definition of the DAG.
```
import pendulum
import logging
from airflow.decorators import dag

@dag(description='Analyzes Divvy Bikeshare Data',
    start_date=pendulum.now(),
    schedule_interval='@daily')
def divvy_dag():
```

#### Using Operator
Operators define the atomic steps of work that make up a DAG. Instantiated operators are referred to as Tasks.
```
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def hello_world():
    print(“Hello World”)

divvy_dag = DAG(...)
task = PythonOperator(
    task_id=’hello_world’,
    python_callable=hello_world,
    dag=divvy_dag)
```

#### Schedules
Schedules are optional, and may be defined with cron strings or Airflow Presets. Airflow provides the following presets:
- `@once` - Run a DAG once and then never again
- `@hourly` - Run the DAG every hour
- `@daily` - Run the DAG every day
- `@weekly` - Run the DAG every week
- `@monthly` - Run the DAG every month
- `@yearly`- Run the DAG every year
- `None` - Only run the DAG when the user initiates it

<br/>

- **Start Date:** If your start date is in the past, Airflow will run your DAG as many times as there are schedule intervals between that start date and the current date.
- **End Date:** Unless you specify an optional end date, Airflow will continue to run your DAGs until you disable or delete the DAG.

## Task Dependencies
In Airflow DAGs:
- Nodes = Tasks
- Edges = Ordering and dependencies between tasks

Task dependencies can be described programmatically in Airflow using `>>` and `<<`
- `a >> b` means a comes before b
- `a << b` means a comes after b

```
hello_world_task = PythonOperator(task_id=’hello_world’, ...)
goodbye_world_task = PythonOperator(task_id=’goodbye_world’, ...)
# Use >> to denote that goodbye_world_task depends on hello_world_task
hello_world_task >> goodbye_world_task
```
Tasks dependencies can also be set with “set_downstream” and “set_upstream”
- `a.set_downstream(b)` means a comes before b
- `a.set_upstream(b)` means a comes after b

```
hello_world_task = PythonOperator(task_id=’hello_world’, ...)
goodbye_world_task = PythonOperator(task_id=’goodbye_world’, ...)
hello_world_task.set_downstream(goodbye_world_task)
```

## Airflow Hooks
Connections can be accessed in code via hooks. Hooks provide a reusable interface to external systems and databases. With hooks, you don’t have to worry about how and where to store these connection strings and secrets in your code. Airflow comes with many Hooks that can integrate with common systems. Here are a few common ones:
- `HttpHook`
- `PostgresHook` (works with RedShift)
- `MySqlHook`
- `SlackHook`
- `PrestoHook`

```
from airflow import DAG
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.python_operator import PythonOperator

def load():
# Create a PostgresHook option using the `demo` connection
    db_hook = PostgresHook(‘demo’)
    df = db_hook.get_pandas_df('SELECT * FROM rides')
    print(f'Successfully used PostgresHook to return {len(df)} records')

load_task = PythonOperator(task_id=’load’, python_callable=hello_world, ...)
```

## Templating
Airflow leverages templating to allow users to “fill in the blank” with important runtime variables for tasks. We use the `**kwargs` parameter to accept the runtime variables in our task.
```
from airflow.decorators import dag, task
@dag(
  schedule_interval="@daily";
)
def template_dag(**kwargs):
  @task
  def hello_date():
    print(f“Hello {kwargs['ds']}}”)
```
