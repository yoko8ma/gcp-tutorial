import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import datetime

default_args = {
    'start_date': datetime.datetime(2018, 1, 1),
}

dag = DAG(
    dag_id='echo',
    default_args=default_args,
    schedule_interval = None)

task = BashOperator(
    task_id='echo',
    bash_command='echo Hello World!',
    dag=dag)

task
