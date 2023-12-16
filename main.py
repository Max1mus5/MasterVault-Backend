from fastapi import FastAPI
from config.database import engine, Base
from routers.auth import  auth_router
from routers.passwords import password_router
from routers.users import users_router

app = FastAPI()

app.title = "Password Manager BACK"
app.version = "1.0"

#BD in config/database.py
Base.metadata.create_all(bind=engine)


app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(password_router, prefix="/passwords", tags=["Passwords"])
app.include_router(users_router, prefix="/users", tags=["Users"])

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000)