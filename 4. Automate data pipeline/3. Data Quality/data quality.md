# Data Quality

## Data Lineage
The data lineage of a dataset describes the discrete steps involved in the creation, movement, and calculation of that dataset.

### Why is Data Lineage important?
- **Instilling Confidence:** Being able to describe the data lineage of a particular dataset or analysis will build confidence in data consumers (engineers, analysts, data scientists, etc.) that our data pipeline is creating meaningful results using the correct datasets. If the data lineage is unclear, its less likely that the data consumers will trust or use the data.
- **Defining Metrics:** Another major benefit of surfacing data lineage is that it allows everyone in the organization to agree on the definition of how a particular metric is calculated.
- **Debugging:** Data lineage helps data engineers track down the root of errors when they occur. If each step of the data movement and transformation process is well described, it's easy to find problems when they occur.

## Scheduling in Airflow
Airflow will catchup by creating a DAG run for every period defined by the schedule_interval between the start_date and now. Airflow uses the schedule interval to create historical DAG runs and catchup data. Whenever the start date of a DAG is in the past, and the time difference between the start date and now includes more than one schedule intervals, Airflow will automatically schedule and execute a DAG run to satisfy each one of those intervals. Catchup is enabled by default. Airflow will begin running pipelines on the date in the start_date parameter . This is the date when a scheduled DAG will start executing on its own. In the sample code below, the DAG will be scheduled to run daily beginning immediately. To disable `catchup` we have to set `False` to the parameter
```
@dag(
    # schedule to run daily
    # once it is enabled in Airflow
    schedule_interval='@daily',
    start_date=pendulum.now(),
    catchup=False
)
```

Airflow pipelines can optionally have end dates. You can use an end_date parameter to let Airflow know the date it should stop running a scheduled pipeline. End_dates can also be useful when you want to perform an overhaul or redesign of an existing pipeline. Update the old pipeline with an end_date and then have the new pipeline start on the end date of the old pipeline. Schedules are not explicitly required in Airflow. By default, Airflow defaults DAGs to running once a day.
```
@dag(
    start_date=pendulum.datetime(2022, 8, 1, 0, 0, 0, 0),
    end_date=pendulum.datetime(2022, 9, 1, 0, 0, 0, 0),
    schedule_interval='@daily',
    max_active_runs=1    
)
```

## Data Partitioning
Pipelines designed to work with partitioned data fail more gracefully. Smaller datasets, smaller time periods, and related concepts are easier to debug than big datasets, large time periods, and unrelated concepts. Partitioning makes debugging and rerunning failed tasks much simpler. It also enables easier redos of work, reducing cost and time. Another great thing about Airflow is that if your data is partitioned appropriately, your tasks will naturally have fewer dependencies on each other. Because of this, Airflow will be able to parallelize execution of your DAGs to produce your results even faster. There are four  common ways to partition data 
- Logical Partitioning is the process of breaking conceptually related data into discrete group of data (like based on month, date, year)
- Time Partitioning is the process of processing data based on a schedule or when it was created.
- Size partitioning separates data for processing based on storage limits
- Location partition, this would be considered a type of logical partitioning

## Data Quality
Before we can measure data quality, we need to have a set of standards to measure against. Adherence to a set of requirements is a good starting point for measuring data quality. Requirements should be defined by you and your data consumers before you start creating your data pipelines. 

#### Examples of Data Quality Requirements
- Data must be a certain size
- Data must be accurate to some margin of error
- Data must arrive within a given timeframe from the start of execution. Service Level Agreements, or SLAs, tell Airflow when a DAG must be completed by.
- Pipelines must run on a particular schedule
- Data must not contain any sensitive information

