from fastapi import HTTPException, APIRouter, Depends
from config.database import Session
from utils.encryption import user_password
from utils.validation import (is_valid_email as validate_email, 
                          is_valid_password as validate_password, is_valid_username as validate_username, is_valid_password as validate_password,
                          validate_identity)
from models.user import User
from schemas.user_schemas import userS
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from middlewares.auth_middleware import JWTBearer
from schemas.user_schemas import userS

auth_router = APIRouter()

def set_user(username: str, email: str, password: str):
  db = Session()
  try:
      if not validate_username(username):
       raise ValueError("Invalid username")
      if not validate_email(email):
          raise ValueError("Invalid email")
      if not validate_password(password):
          raise ValueError("Invalid password")

      hashed_password = user_password(password)
      new_user = User(username=username, email=email, password=hashed_password)
      db.add(new_user)
      db.commit()
      db.refresh(new_user)
      db.close()
      return new_user

  except ValueError as e:
      db.close()
      raise HTTPException(status_code=400, detail=str(e))
    
@auth_router.post("/create_user/", response_model=userS, status_code=200)
def create_user(user_data: userS):
    """ 
    print("Received data from frontend:")
    print("Username:", user_data.username)
    print("Email:", user_data.email)
    print("Password:", user_data.password) """

    user = set_user(username=user_data.username, email=user_data.email, password=user_data.password)
    try:
        return user  # Devolver el objeto 'user' que coincide con el modelo 'userS'
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


  
  
@auth_router.post("/login/", response_model=dict, status_code=200)
def login(user: userS):
    if validate_identity(user=user, password=user.password):
        token = create_token(data=user.model_dump())
        result = JSONResponse(content={"token": token},
                              status_code=200)

    else:
        result = JSONResponse(content={"message":"Invalid credentials"}, status_code=401)
    return result

