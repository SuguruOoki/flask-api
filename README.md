# Description (説明)

This repository is a template for trying flask api with docker-compose.
このリポジトリはdocker-composeでflaskのAPI実装を試すためのテンプレート。

# Directory

```
flask-api/
├── rest_api/
│   ├── apis/
│   │   └── __init__.py
│   ├── models/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── app.py
│   └── settings.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

# Preparation (準備)

Please install the following before using this repository.
このリポジトリを使う前に下記をインストールしておいてください。

- docker
- docker-compose

# How to use (使い方)

Execute app/main.py at startup. Please change as necessary.
起動時に app/main.py を実行します。必要に応じて変更してください。

- Example of access from client side (クライアント側からのアクセス例)

get

```sh
$ curl http://localhost:50000/
route get. Hello!
```

post

```sh
$ curl http://localhost:50000/reply -X POST -H "Content-Type: application/json" -d '{"keyword": "hoge"}'
{
  "Answer": {
    "Text": "route post. keyword is hoge!"
  },
  "Content-Type": "application/json"
}
```
