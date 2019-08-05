from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import datetime

default_args = {
    'start_date': datetime.datetime(2018, 1, 1),
}


def learn():
    import logging
    from sklearn.datasets import load_iris

    iris = load_iris()
    logging.info(type(iris))


dag = DAG(
    dag_id='learning',
    default_args=default_args,
    schedule_interval = None)

task = PythonOperator(
    task_id='learn',
    python_callable=learn,
    dag=dag)

task
