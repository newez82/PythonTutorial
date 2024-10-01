"""
    Sensor is a special type of operator which waits for something to occur,
    espeically when we don't know exact time when the file exists

    Minio is an api comatiable with aws s3 cloud storage service

    Create a dag to connect to Minio S3 Bucket and sense the file's existence.

    podman run -p 9000:9000 -p 9001:9001 -e "MINIO_ROOT_USER=ROOTNAME" -e "MINIO_ROOT_PASSWORD=CHANGEME123" quay.io/minio/minio server /data --console-address ":9001"
"""

from datetime import datetime, timedelta

from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

from airflow import DAG

default_args = {"owner": "chin", "retries": 5, "retry_delay": timedelta(minutes=2)}

with DAG(
    dag_id="dag_with_minio_s3_sensor_v02",
    default_args=default_args,
    description="connect dag to minio s3",
    start_date=datetime(2024, 9, 24),
    schedule_interval="@daily",
) as dag:
    task1 = S3KeySensor(
        task_id="sensor_minio_s3",
        bucket_name="airflow",
        bucket_key="data.csv",
        aws_conn_id="minio_conn",
        mode="poke",  # poke to check the file exists
        poke_interval=5,
        timeout=30,
    )
