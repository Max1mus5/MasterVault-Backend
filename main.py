from fastapi import FastAPI
from config.database import engine, Base
from routers.auth import auth_router
from routers.passwords import password_router
from routers.users import users_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.title = "Password Manager BACK"
app.version = "1.0"

# Configuración de CORS
origins = [
    "http://localhost:3000",  
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8000/user/create_user/"
    "http://localhost:8000/user/create_user/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=["*"],
)

# Creación de la base de datos
Base.metadata.create_all(bind=engine)

# Inclusión de los routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(password_router, prefix="/passwords", tags=["Passwords"])
app.include_router(users_router, prefix="/users", tags=["Users"])

""" uvicorn main:app --reload --port=8080 """