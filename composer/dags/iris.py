import datetime
from airflow import DAG
from airflow.contrib.operators.mlengine_operator import MLEngineTrainingOperator

default_args = {
    'start_date': datetime.datetime(2018, 1, 1),
}

with DAG(
        "iris",
        schedule_interval=None,
        default_args=default_args) as dag:

    task = MLEngineTrainingOperator(
        project_id=<プロジェクトID>,
        job_id="iris_" + datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
        package_uris="gs://<ストレージのパス>/iris-0.1.tar.gz",
        training_args="",
        region="asia-east1",
        training_python_module="trainer.task",
        task_id="iris",
        python_version=2.7
    )

    task
