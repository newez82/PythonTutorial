"""
    Create airflow dag with python operator

    share information between different tasks using airflow XCOM
    push information into 1 task and pull information from another
    task. By default every functions return value will be automatically
    pushed into XCOM

    max size of COMS is only 48 kb, it never use to share large data 
    like Panda dataframe

"""

from datetime import datetime, timedelta

from airflow.operators.python import PythonOperator

from airflow import DAG

default_args = {"Owner": "Chin", "retires": 5, "retry_delay": timedelta(minutes=2)}


def greet(name, age):
    print(f"Hello World! My name is {name}, and I am {age} years old!")


def get_name(ti):
    ti.xcom_push(key="first_name", value="Jerry")
    ti.xcom_push(key="last_name", value="Fridman")


def get_age(ti):
    ti.xcom_push(key="age", value=19)


# ti stands for task instance, XCOM can only be called by ti,
# it will populate an error if using different name
def greet_xoms(ti):
    # pull the return value of task with ID and get name
    first_name = ti.xcom_pull(task_ids="get_name", key="first_name")
    last_name = ti.xcom_pull(task_ids="get_name", key="last_name")
    age = ti.xcom_pull(task_ids="get_age", key="age")
    print(
        f"Hello World! My name is {first_name} {last_name}, and I am {age} years old!"
    )


with DAG(
    dag_id="python_operator_v7",
    default_args=default_args,
    description="first dag using python operator",
    start_date=datetime(2024, 9, 20, 12),
    schedule_interval="@daily",
) as dag:
    # task1 = PythonOperator(
    #     task_id="greet",
    #     python_callable=greet,
    #     # dictionary of keyword arguments that will get unpacked in the python function
    #     op_kwargs={"name": "Tom", "age": 20},
    #     )
    task1 = PythonOperator(
        task_id="greet_xcom",
        python_callable=greet_xoms,
        # dictionary of keyword arguments that will get unpacked in the python function
        # op_kwargs={"age": 20},
    )
    task2 = PythonOperator(task_id="get_name", python_callable=get_name)
    task3 = PythonOperator(task_id="get_age", python_callable=get_age)
    [task2, task3] >> task1
