from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_arguments = {
    'owner':"srinivas",
    'start_time': datetime(2024,10,4,10,00)
}