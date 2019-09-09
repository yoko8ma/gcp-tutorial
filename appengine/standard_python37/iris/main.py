import logging
import pickle
import responder
import keras

api = responder.API()


@api.route('/')
def index(req, resp):
    resp.html = api.template("index.html")


@api.route('/api/v1/predict')
def predict(req, resp):
    import numpy as np

    # 予測データ
    sepal_length = req.params.get("sepal_length")
    sepal_width = req.params.get("sepal_width")
    petal_length = req.params.get("petal_length")
    petal_width = req.params.get("petal_width")

    # TODO: validation
    data = [sepal_length, sepal_width, petal_length, petal_width]
    logging.info(data)

    # 標準化オブジェクトの読込
    with open("./static/scaler.pkl", 'rb') as f:
        scaler = pickle.load(f)

    # 標準化
    X = scaler.transform(np.array([data]))
    logging.info(X)

    # 学習済みモデルの読込
    model = keras.models.load_model("./static/model.h5", compile=False)

    # 予測
    y = model.predict(X, batch_size=1)
    logging.info(y)
    resp.headers.update({'Content-Type': 'application/json'})
    resp.media = {"label": int(y[0].argmax()), "accuracy": float(y[0].max())}


@api.route('/api/v1/learn')
def learn(req, resp):
    # scikit-learnに入っているアヤメデータを分類する
    from sklearn import datasets

    # データの読込
    iris = datasets.load_iris()

    # 学習データとテストデータへの振分
    from sklearn.model_selection import train_test_split

    X = iris.data
    y = iris.target

    # X_train: 特徴量の学習データ
    # X_test: 特徴量のテストデータ
    # y_train: ラベルの学習データ
    # y_test: ラベルのテストデータ
    # train_size=0.8: 80%を学習データ、20%をテストデータに振り分ける
    # random_state=0: いつも同じ振分結果になるように固定値をセットする
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=0)

    # 学習
    from sklearn import svm

    model = svm.SVC(gamma='scale')
    model.fit(X_train, y_train)

    # 予測
    from sklearn.metrics import accuracy_score

    pred = model.predict(X_test)
    ac_score = accuracy_score(y_test, pred)
    resp.text = str(ac_score)


if __name__ == '__main__':
    api.run(host='127.0.0.1', port=8080, debug=True)
