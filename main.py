from fastapi import FastAPI
from config.database import engine, Base
from routers.auth import auth_router
from routers.passwords import password_router
from routers.users import users_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.title = "Password Manager BACK"
app.version = "1.0"


origins = [
  "http://localhost:3000"

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