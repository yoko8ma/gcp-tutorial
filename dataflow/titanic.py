# coding:utf-8

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import GoogleCloudOptions
from apache_beam.options.pipeline_options import WorkerOptions
from apache_beam.options.pipeline_options import StandardOptions

def run():
    # Dataflow設定
    options = PipelineOptions()
    google_cloud_options = options.view_as(GoogleCloudOptions)
    google_cloud_options.project = '<YOUR_PROJECT_ID>'
    google_cloud_options.job_name = 'titanic'
    google_cloud_options.staging_location = 'gs://<YOUR_BUCKET>/titanic/binaries'
    google_cloud_options.temp_location = 'gs://<YOUR_BUCKET>/titanic/temp'
    worker_options = options.view_as(WorkerOptions)
    worker_options.disk_size_gb = 30
    worker_options.max_num_workers = 2

    # localで動かす場合
    options.view_as(StandardOptions).runner = 'DirectRunner'

    # GCPで動かす場合
    # options.view_as(StandardOptions).runner = 'DataflowRunner'

    pipeline = beam.Pipeline(options=options)

    query = "SELECT Pclass, Sex, Age, SibSp, Parch, Fare, Embarked, Survived FROM `bq_tutorial.titanic_train`;"

    # パイプライン定義
    (pipeline
     | "read" >> beam.io.Read(beam.io.BigQuerySource(project=google_cloud_options.project, query=query, use_standard_sql=True))
     | "map" >> beam.Map(lambda v: (v["Sex"], v))
     | 'window' >> beam.WindowInto(beam.window.FixedWindows(1))
     | "group by" >> beam.GroupByKey()
     | "learn" >> beam.FlatMap(train))

    pipeline.run().wait_until_finish()

# 学習
def train(key_value):
    # プロセスが分かれるためメソッド内でインポートする
    import logging
    from sklearn.svm import SVC
    from sklearn.preprocessing import LabelEncoder
    import pandas as pd
    from sklearn.model_selection import train_test_split

    logging.getLogger().setLevel(logging.INFO)

    # key_value[0]: 性別
    # key_value[1]: 性別をキーにしたデータの配列
    df = pd.DataFrame(key_value[1])

    # 数値変換
    le = LabelEncoder()
    le.fit(df["Embarked"])
    df["Embarked"] = le.transform(df["Embarked"])

    # 学習データ作成
    x = df.drop(["Sex", "Survived"], axis='columns')
    y = df["Survived"]
    X_train, X_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=0)

    # 学習
    clf = SVC()
    clf.fit(X_train, y_train)
    logging.info(clf.score(X_train, y_train))

    # テスト
    clf.predict(X_test)
    logging.info(clf.score(X_test, y_test))

if __name__ == '__main__':
    run()
