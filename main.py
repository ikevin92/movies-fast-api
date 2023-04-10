
import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field

from config.database import Base, engine
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

# config para el swagger
app = FastAPI()
app.title = "My Movie App con fastAPI"
app.description = "API para la gestión de películas"
app.version = "1.0.0"

# middleware para manejo de errores
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

# motor bd importado
Base.metadata.create_all(bind=engine)


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    }
]


@app.get("/", tags=["Home"])
def message():
    return HTMLResponse('<h1>¡Hola Mundo!</h1>')


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0",
#                 port=int(os.environ.get("PORT", 8000)))
