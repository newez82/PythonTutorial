"""
    # create env
    #   python3 -m venv py_env
    # activate the python env
    #   source py_env/bin/activate
    # install airflow

    # a dac implmentation is an installoation of the class dac
    
    # create first airflow DAG
"""

# import the DAG from airflow
from datetime import datetime, timedelta

from airflow.operators.bash import BashOperator

from airflow import DAG

# initalize the operator
default_args = {
    "owner": "Chin",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),  # 2 minutes wait time for every retries
}

# create the instance of DAG using the WITH statement
with DAG(
    dag_id="first_dag_v7",
    default_args=default_args,
    description="first airflow dag",
    start_date=datetime(2024, 9, 20, 14),
    schedule_interval="@daily",
) as dag:
    task1 = BashOperator(
        task_id="first_task", bash_command="echo hello world, this is the first task!"
    )
    task2 = BashOperator(
        task_id="second_task",
        bash_command="echo hey, I am task2 and will be running after task1",
    )
    task3 = BashOperator(
        task_id="third_task",
        bash_command="echo hey, I am task3 and will be running after task1",
    )
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # Big Shift operator
    # task1 right shifts of task2 and task3 means
    # task2 and task3 are downstream tasks of task1
    # task1 >> task2
    # task1 >> task3

    # put the tasks in an array that are downstream tasks of task1
    task1 >> [task2, task3]
