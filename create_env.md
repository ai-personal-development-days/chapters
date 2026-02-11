# 開発環境構築 & Gemini API 設定手順

このリポジトリで Gemini API を使用するための、環境構築と認証設定の全手順です。

## 1. 仮想環境の作成とライブラリ導入

まずは Python の実行環境を整えます。リポジトリのルートで実行してください。

```zsh
# Pythonのインストール
brew install python@3.13

# 仮想環境の作成
python3.13 -m venv .venv

# 仮想環境の有効化
source .venv/bin/activate

# pip自体のアップグレード
python -m pip install --upgrade pip

# 必要なライブラリのインストール
- google-genai: Gemini API を叩くための最新SDK
- python-dotenv: .env ファイルからAPIキーを読み込むためのライブラリ
pip install -U google-genai python-dotenv

# 構築完了の確認
pip list
```

## 2. Gemini API キーの取得

Google AI Studio から通信用の「鍵」を取得します。

1. [Google AI Studio](https://aistudio.google.com/) にアクセスし、Googleアカウントでログインします。
2. 左メニューの **"Get API key"** をクリックします。
3. **"Create API key"** をクリックし、生成された `AIza...` で始まる文字列をコピーします。

## 3. 環境変数 (.env) の設定

APIキーをプログラムに直接書くのは非推奨（セキュリティリスク）なため、外部ファイルに保存します。

1. リポジトリのルートディレクトリ（`chapters/` 直下）に `.env` という名前のファイルを作成します。
2. ファイル内に以下を記述します（コピーしたキーを貼り付けてください）。

```text
GEMINI_API_KEY=ここにコピーしたAPIキーを貼り付け
```

## 4. Git管理の安全設定

作成した `.env` ファイル（機密情報）や `.venv` フォルダ（実行環境）を GitHub に公開しないよう、`.gitignore` を確認します。

リポジトリ直下の **`.gitignore`** に以下の2行が含まれていることを確認してください。

```text
.venv/
.env
```
