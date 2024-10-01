"""
    catchup or backfill let us run dag in the past

    by default catchup parameter set to True, it will automatically run
    the dag from the start_date to today date.

    if catchup set to False, we can use backfill command by logging in
    into the container (airflow_docker_airflow_scheduler_1) and run the following command:

        airflow dags backfill -s 2022-11-12 -e 2022-11-18 <dag_id>
"""

from datetime import datetime, timedelta

from airflow.operators.bash import BashOperator

from airflow import DAG

default_args = {"owner": "chin", "retries": 5, "retry_delay": timedelta(minutes=2)}

with DAG(
    dag_id="dag_with_catchup_backfill_v01.3",
    default_args=default_args,
    description="catch up and backfill dag",
    start_date=datetime(2024, 9, 12),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    task1 = BashOperator(
        task_id="task1", bash_command="echo this is a simple batch command!"
    )
