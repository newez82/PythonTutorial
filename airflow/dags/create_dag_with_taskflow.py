"""
    TaskFlow API takes care of moving inputs and output between tasks
    and automatically calculate dependency.

    high recommend to use TaskFlow API only when only consist of plain python functions
"""

from datetime import datetime, timedelta

from airflow.decorators import dag, task

default_args = {"owner": "chin", "retries": 5, "retry_delay": timedelta(minutes=5)}


@dag(
    dag_id="dag_with_taskflow_api_v02",
    default_args=default_args,
    start_date=datetime(2024, 9, 22),
    schedule_interval="@daily",
)
def hello_world_etl():
    """
    taskflow API will automatically calculate the dependency, it also takes care of the
    XCOM values push and pull operation.
    """

    @task(multiple_outputs=True)
    def get_name():
        return {"first_name": "Jerry", "last_name": "Fridman"}

    @task()
    def get_age():
        return 19

    @task()
    def greet(first_name, last_name, age):
        print(
            f"Hello World! My name is {first_name} {last_name} and I am {age} years old!"
        )

    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict["first_name"], last_name=name_dict["last_name"], age=age)


greet_dag = hello_world_etl()
