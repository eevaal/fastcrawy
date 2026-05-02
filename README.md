<div align="center">
  <a href="https://github.com/eevaal/fastpoint">
    <img src="fastpoint.png" alt="Logo" width="128" height="128">
  </a>

  <h1 align="center">FastPoint</h1>

  <p align="center">
    <b>Библиотека, упрощающая работу с FastAPI</b>
    <br />
  </p>
  
  ![Python](https://img.shields.io/badge/python-3.13-blue?style=for-the-badge&logo=python&logoColor=white)
  ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
</div>

# FastPoint

FastPoint - это минималистичная обертка над FastAPI, предназначенная для мгновенного превращения Python-функций в HTTP-эндпоинты. Библиотека берет на себя всю рутину по настройке сервера, инициализации приложения и управлению запуском.
## Основные возможности
1. Инициализация FastAPI «из коробки» без лишнего шаблонного кода.
2. Простой декоратор для регистрации GET и POST эндпоинтов.
3. Автоматический запуск сервера uvicorn.
4. Автоматическое открытие интерактивной документации (Swagger UI) при старте.

## Установка
Для установки библиотеки используйте uv или pip:

```
uv add fastpoint
```
**ИЛИ**
```
pip install fastpoint
```

## Как пользоваться
Ниже приведен пример создания простого API-сервиса:
```python
from fastpoint import fp

@fp.endpoint("/hello")
def welcome(name: str = "User"):
    return {"message": f"Hello, {name}", "status": "success"}

@fp.endpoint("/data", method="POST")
async def handle_data(payload: dict):
    return {"received": payload}

if __name__ == "__main__":
    fp.run()

```

Pull requests и новые идеи приветствуются!
