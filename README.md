# post-line-from-sns

## 設定項目

事前に設定しておくべき項目を以下に示す。

## AWS Lambda

AWS Lambda に以下の値を設定しておくこと。

### 環境変数

- LINE_SECRET_NAME
  - 意味：LINE Notify の API キーなどを格納したシークレットの名前
  - 例：`secrets/line`
- LOG_LEVEL
  - 意味：ログレベル `CRITICAL, ERROR, WARNING, INFO, DEBUG` から選択
  - 例：`DEBUG`

### Secrets

### LINE_SECRET_NAME

- api_key
  - 意味：Basic 認証用の API key。
  - 例：`21afjlij4224`

## 使い方

### ソースコードのアップロード

まず、aws-cli を事前に設定しておくこと。

```bash
aws configure
```

次に、アップロードスクリプトを実行すること。

```bash
./upload.sh
```
