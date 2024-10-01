"""
    Airflow connection connect to Postgres
"""

from datetime import datetime, timedelta

from airflow.providers.postgres.operators.postgres import PostgresOperator

from airflow import DAG

default_args = {"owner": "chin", "reties": 5, "retry_delay": timedelta(minutes=2)}

with DAG(
    dag_id="dag_with_postgres_operator_v04",
    default_args=default_args,
    description="connect dag to postgre db",
    start_date=datetime(2024, 9, 23),
    schedule_interval="@daily",
) as dag:
    task1 = PostgresOperator(
        task_id="create_postgres_table",
        postgres_conn_id="postgres_local",
        sql="""
                create table if not exists dag_runs(
                    dt date,
                    dag_id character varying,
                    primary key(dt, dag_id)
                )
            """,
    )

    task2 = PostgresOperator(
        task_id="delete_data_from_table",
        postgres_conn_id="postgres_local",
        # ds is dag execution date
        # dag_id is dag id that are set by default by airflow engine,
        # it can be accessed by putting the variable name into 2 curly
        # brackets.
        # variable can be find in
        sql="""
            delete from dag_runs where dt = '{{ds}}' and dag_id = '{{dag.dag_id}}'
        """,
    )

    task3 = PostgresOperator(
        task_id="insert_into_table",
        postgres_conn_id="postgres_local",
        # ds is dag execution date
        # dag_id is dag id that are set by default by airflow engine,
        # it can be accessed by putting the variable name into 2 curly
        # brackets.
        # variable can be find in
        sql="""
            insert into dag_runs (dt, dag_id) values ('{{ds}}','{{dag.dag_id}}')
        """,
    )

    task1 >> task2 >> task3
