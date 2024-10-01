"""
    Schedule dag at any time using Cron expression

    cron expression is a string comprising 5 fields separated by white space that 
    represents a set of times, normally as a schedule to execute some routine
        minute | hour | day of the month | month | day of the week

    preset     meaning                                                           cron
    None     - Don't Schedule, use for exclusively "externally triggered" DAGs  
    @one     - Schedule once and only once
    @hourly  - Run once an hour at the beginning of the hour                     (0 * * * *)
    @daily   - Run once a day at midnight                                        (0 0 * * *)
    @weekly  - Run once a week at midnight on Sunday monring                     (0 0 * * 0)
    @monthly - Run once a month at midnight of the first day of the month        (0 0 1 * *)
    @yearly  - Run once a year at midnight of January 1                          (0 0 1 1 *)
"""

from datetime import datetime, timedelta

from airflow.operators.bash import BashOperator

from airflow import DAG

default_args = {"owner": "chin", "retries": 5, "retry_delay": timedelta(minutes=2)}

with DAG(
    dag_id="schedule_with_cron_expression_v03",
    default_args=default_args,
    description="schedule with cron expression",
    start_date=datetime(2024, 9, 12),
    schedule_interval="0 3 * * Tue-Fri",
) as dag:
    task1 = BashOperator(task_id="task1", bash_command="dag with cron expression")
