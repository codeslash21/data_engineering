import pendulum
import logging

from airflow.decorators import dag, task

@dag(
    schedule_interval='@hourly',
    start_date=pendulum.now()
)
def task_dependencies():

    @task()
    def hello_world():
        logging.info("Hello World")

    @task()
    def addition(first,second):
        logging.info(f"{first} + {second} = {first+second}")
        return first+second

    @task()
    def subtraction(first,second):
        logging.info(f"{first -second} = {first-second}")
        return first-second

    @task()
    def division(first,second):
        logging.info(f"{first} / {second} = {int(first/second)}")   
        return int(first/second)     

#  TODO: assign the result of the addition function to a variable
#  TODO: assign the result of the subtraction function to a variable
#  TODO: pass the result of the addition function, and the subtraction functions to the division function
#  TODO: Configure the task dependencies such that the graph looks like the following:
#
#                    ->  addition_task
#                   /                 \
#   hello_world_task                   -> division_task
#                   \                 /
#                    ->subtraction_task

    hello = hello_world()
    sum = addition(2,4)
    difference = subtraction(10,8)
    div = division(sum, difference)

    hello >> sum
    hello >> difference
    sum >> div
    difference >> div

task_dependencies_dag=task_dependencies()
