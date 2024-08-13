from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from twitter_etl import run_twitter_etl

#Defaults arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['nikhilbevara26@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

#creation of Dag object
dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='My first DAG!',
    schedule_interval=timedelta(days=1),
)

#calling the ETL function using Python operators in airflow
run_etl = PythonOperator(
    task_id='twitter_etl',
    python_callable=run_twitter_etl,
    dag=dag,
)

run_etl
