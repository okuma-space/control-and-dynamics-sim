# control-and-dynamics-sim
A learning project for control engineering and dynamics simulation

本リポジトリは制御工学とダイナミクス学習用途を目的としており，READMEおよびコードコメントは日本語で記述している．

計算部分もC++エンジン化せず，まずはモデル検証と可視化を優先してPythonで試作している.

作業ログのためにPRは作っているが,コードレビューは主にローカル環境で自主的に実施している．

# 結果サマリ




# シミュレーション実行手順

# 学習文献
- はじめての制御工学 改訂第二版

# issues
現時点での改善アイディアなどはissuesに記載.


# ci/workflow
以下の4ステージで構成.

PRがmergeされる際にdeployステージが実行され、docs/report.mdをhtmlとしてリリースする.
- build-and-push
- lint
- test
- deploy

# Directory Structure
## docs
シミュレーション結果およびレポート

## src
コア実装コード

## scripts
シミュレーション実行・解析スクリプト

## tests
テストコード

## tools
ビルド・Docker・CI・補助スクリプト

# Commands
## dockerコマンド
```bash
docker build -t control-and-dynamics-sim -f .\tools\Dockerfile .

docker run -it --rm -v ${PWD}:/control-and-dynamics-sim control-and-dynamics-sim bash
```

## python format & style check(ruff)
```bash
ruff format src
ruff check src --fix
```

スタイルチェックが厳格すぎるため導入を検討中であるが以下でpylintの実行も可能
```bash
pylint src scripts tests
```

## test
test
```bash
pytest tests
```

coverage report
```bash
pytest tests --cov=src --cov-report=term --cov-report=xml
```