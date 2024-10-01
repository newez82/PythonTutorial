"""
    Step 1: query data from postgres db and save it into text file.
    Step 2: upload text file into S3 bucket.
    tempfile package which enables us to create files in the system
    temporary directory
"""

import csv
import logging
from datetime import datetime, timedelta
from tempfile import NamedTemporaryFile

from airflow.macros import ds_add, ds_format
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator

from airflow import DAG

default_args = {"owner": "chin", "retry": 5, "retries_delay": timedelta(minutes=2)}


def postgres_to_s3(ds_nodash, next_ds_nodash):
    """
    Step 1: query data from postgres db and save it into text file.
    Step 2: upload text file into S3 bucket.
    """
    # Step 1
    hook = PostgresHook(postgres_conn_id="postgres_local")
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "select * from orders where date >=%s and date <= %s",
        (ds_nodash, next_ds_nodash),
    )
    logging.info("query %s:", cursor.query)
    logging.info("cursor %d:", cursor.rowcount)
    with NamedTemporaryFile(mode="w", suffix=f"{ds_nodash}") as f:
        # with open(f"dags/get_orders_{ds_nodash}.txt", "w", encoding="UTF-8") as f:
        csv_writer = csv.writer(f)
        # write column name as the first row
        csv_writer.writerow([i[0] for i in cursor.description])
        logging.info(cursor)
        csv_writer.writerows(cursor)
        # file saved on disk by calling the flush
        f.flush()
        cursor.close()
        conn.close()
        logging.info(
            "Saved orders data in text file: %s", f"dags/get_orders_{ds_nodash}.txt"
        )

        # Step 2
        s3_hook = S3Hook(aws_conn_id="minio_conn")
        s3_hook.load_file(
            filename=f.name,
            key=f"orders/{ds_nodash}.txt",
            bucket_name="airflow",
            replace=True,
        )
        logging.info("Order file %s has been pushed to S3!, f.name")


with DAG(
    dag_id="dag_with_postgres_hook_s3_v06",
    default_args=default_args,
    description="hook s3 from postgres",
    start_date=datetime(2022, 4, 30),
    schedule_interval="@daily",
) as dag:
    task1 = PythonOperator(task_id="postgres_to_s3", python_callable=postgres_to_s3)
