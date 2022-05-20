

from datetime import datetime, timedelta

from traitlets import default
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
import pendulum

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": pendulum.today('UTC').add(days=0, hours=0),
    "email": [""],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
 }


dag = DAG(
    "spotify_dag",
    default_args=default_args,
    description="Spotify DAG",
    # schedule_interval="@once",
    schedule_interval=timedelta(minutes=5),
)

def just_a_func():
    print("Just as example")


run_etl = PythonOperator(
    task_id="whole_spotify_etl",
    python_callable=just_a_func,
    dag=dag,
)

run_etl
