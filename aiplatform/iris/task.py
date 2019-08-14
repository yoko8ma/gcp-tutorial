from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# データの読込
iris = load_iris()

# X_train: 特徴量の学習データ
# X_test: 特徴量のテストデータ
# y_train: ラベルの学習データ
# y_test: ラベルのテストデータ
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, train_size=0.8, random_state=0)

# 学習
model = SVC()
model.fit(X_train, y_train)

# テスト
print("accuracy:{}".format(model.score(X_test, y_test)))
