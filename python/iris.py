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
print(ac_score)
