import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


class FastPoint:
    def __init__(self):
        self.app = FastAPI()
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def endpoint(self, path: str, method: str = "GET", **kwargs):
        def decorator(func):
            route_path = path if path else f"/{func.__name__}"
            self.app.add_api_route(
                route_path,
                endpoint=func,
                methods=[method],
                **kwargs
            )
            return func
        return decorator

    def run(self, host: str = "127.0.0.1", port: int = 8000, **kwargs):
        print(f"Запуск FastPoint на http://{host}:{port}")
        print(f"Документация FastPoint доступна на http://{host}:{port}/docs")
        uvicorn.run(self.app, host=host, port=port, **kwargs)

fp = FastPoint()