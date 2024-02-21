# Streamlit と (FastAPI または plumber) を組み合わせて作成した何か

## 想定している OS の環境

#### Windows11

## 元から必要な package

### python

- poetry

### R

- renv

## 最初に一度だけすること

```batch
poetry install --no-root
```

## Streamlit の実行

```batch
poetry shell
start-streamlit.cmd
```

#### Streamlit を用いて作成した Web App を起動した際にアクセスする URL

```
http://127.0.0.1:9000/
```

## FastAPI の実行

```batch
poetry shell
cd fastapi
start-fastapi.cmd
```

#### FastAPI を用いて作成した Web API を起動した際にアクセスする URL (API ドキュメントにアクセスするときの URL)

```
http://127.0.0.1:7000/docs
```

## plumber の実行

```batch
cd plumber
start-plumber.cmd
```

#### FastAPI を用いて作成した Web API を起動した際にアクセスする URL (API ドキュメントにアクセスするときの URL)

```
http://127.0.0.1:8000/__docs__/
```
