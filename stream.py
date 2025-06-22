from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 10,00),
    
}

with DAG('user automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:
    
    streaming_task = PythonOperator(
        task_id='streaming_task',
        python_callable=lambda: print("Streaming data..."),
        dag=dag     
    
)
    