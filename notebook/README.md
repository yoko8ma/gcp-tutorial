# 環境構築
## pyenvのインストール
```
brew install pyenv
```
.bash_profile
```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```
## Anacondaのインストール
```
source ~/.bash_profile
pyenv install -l
pyenv install anaconda3-5.3.1
```
## 仮想環境のセットアップ
```
pyenv local anaconda3-5.3.1
conda create -n py37 python=3.7
source activate py37
```
source activateがコンフリクトする場合は `bash_profile` に追加し
```
alias activate="source $PYENV_ROOT/versions/anaconda3-5.3.1/bin/activate"
```
コマンドは
```
activate py37
```
## パッケージのインストール
```
pip install numpy
pip install pandas
pip install scikit-learn
pip install matplotlib
pip install xgboost
```
## Jupyter Notebookのインストールと起動
```
pip install jupyter
jupyter notebook
```
