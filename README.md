# gcp-tutorial
## 構成
```
.
├── aiplatform # AI Platformサンプル
│   └── iris # アヤメデータの学習
│       ├── __init__.py
│       └── task.py
├── appengine # GAEサンプル
│   ├── helloworld
│   │   ├── README.md
│   │   ├── app.yaml
│   │   └── hello.go
│   └── standard_python37 # Pyhton3.7環境
│       ├── hello_world
│       │   ├── app.yaml
│       │   ├── gunicorn_conf.py
│       │   ├── index.yaml
│       │   ├── main.py
│       │   ├── requirements.txt
│       │   ├── static
│       │   │   └── index.html
│       │   └── templates
│       │       └── index.html
│       └── iris # アヤメデータの学習
│           ├── app.yaml
│           ├── gunicorn_conf.py
│           ├── index.yaml
│           ├── main.py
│           ├── requirements.txt
│           ├── static
│           │   ├── index.html
│           │   ├── model.h5
│           │   ├── model.pkl
│           │   └── scaler.pkl
│           └── templates
│               └── index.html
├── composer # Cloud Composer
│   └── DAG
│       ├── echo.py
│       └── learning.py
├── dataflow # Dataflow
│   └── titanic.py
└── notebook # Jupyter Notebook
    ├── BreastCancer
    │   └── BreastCancer.ipynb
    ├── Iris
    │   ├── Iris.ipynb
    │   ├── model.h5
    │   └── scaler.pkl
    ├── README.md
    └── Titanic
        ├── Titanic.ipynb
        ├── test.csv
        └── train.csv

```