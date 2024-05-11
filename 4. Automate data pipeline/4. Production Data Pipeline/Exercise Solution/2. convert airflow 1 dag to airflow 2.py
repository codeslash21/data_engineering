Airflow 1 DAG
================================
import pendulum
import logging
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def hello_world():
    logging.info("Hello World!")

dag = DAG(
        'greet_flow_dag_legacy',
        start_date=pendulum.now())

greet_task = PythonOperator(
    task_id="hello_world_task",
    python_callable=hello_world,
    dag=dag
)

Airflow 2 DAG
===============================
import logging
import pendulum
from airflow.decorators import dag, task

# @dag decorates the greet_task to denote it's the main function
@dag(
    start_date=pendulum.now()
)
def greet_flow_dag():
    
    # @task decorates the re-usable hello_world_task - it can be called as often as needed in the DAG
    @task
    def hello_world_task():
        logging.info("Hello World!")

    # hello_world represents a discrete invocation of the hello_world_task
    hello_world=hello_world_task()

# greet_dag represents the invocation of the greet_flow_dag
greet_dag=greet_flow_dag()

