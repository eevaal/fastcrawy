import uvicorn
from fastapi import FastAPI

class FastCrawyEngine:
    def __init__(self):
        self.app = FastAPI()

    def endpoint(self, path: str, method: str = "GET", **kwargs):
        def decorator(func):
            self.app.add_api_route(
                path,
                endpoint=func,
                methods=[method],
                **kwargs
            )
            return func
        return decorator

    def run(self, host: str = "127.0.0.1", port: int = 8000, **kwargs):
        print(f"Запуск FastCrawy на http://{host}:{port}")
        uvicorn.run(self.app, host=host, port=port, **kwargs)