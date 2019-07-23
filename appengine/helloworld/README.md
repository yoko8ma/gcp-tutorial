# Hello World
## 認証
```
gcloud auth login
```
## ローカルサーバーの起動
```
dev_appserver.py app.yaml
```
http://localhost:8080/
の表示をブラウザで確認
## GAEへのデプロイ
```
gcloud config set project <PROJECT_ID>
gcloud app deploy
gcloud app browse
```