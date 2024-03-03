from fastapi import HTTPException, APIRouter, Depends
from config.database import Session
from utils.encryption import user_password
from utils.validation import (is_valid_email as validate_email, 
                          is_valid_password as validate_password, is_valid_username as validate_username, is_valid_password as validate_password,
                          validate_identity,get_current_user)
from models.user import User
from models.password import Password
from utils.jwt_manager import create_token
from middlewares.auth_middleware import JWTBearer
from sqlalchemy import update



users_router = APIRouter()
def hide_password(password: str) -> str:
   return '*' * len(password)



@users_router.get("/get/",tags=["Users"])
def get_all_users():
   db = Session()
   users = db.query(User).all()
   
   for user in users:
       user.password=hide_password(user.password)
       for password in user.passwords:
           password.password = hide_password(password.password)
           password.unlock = hide_password(password.unlock)
   db.close()       
   return users


@users_router.put("/update/",tags=["Users"])
def update_my_info(user_id: int, username: str, email: str, current_user: User = Depends(get_current_user),
                    new_password:str = None):
 db = Session()
 try:
    if not validate_username(username):
        raise ValueError("Invalid username")
    if not validate_email(email):
        raise ValueError("Invalid email")
    if not validate_password(new_password):
        raise ValueError("Invalid password")
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if current_user.id != user.id:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    db=Session()
    hashed_password = user_password(new_password)
    stmt = (
        update(User).where(User.id == user_id).values(username=username, email=email, password=hashed_password)
    )
    db.execute(stmt)
    db.commit()
    db.close()
    return {"message": f"User {user.username} updated successfully"}

 except ValueError as e:
    raise HTTPException(status_code=400, detail=str(e))





@users_router.delete("/delete/",tags=["Users"])
def delete_user(user_id: int):
 db = Session()
 passwords = db.query(Password).filter(Password.user_id == user_id).all()
 user = db.query(User).filter(User.id == user_id).first()
 if validate_identity(user.username, user.password):
   try:
       user = db.query(User).filter(User.id == user_id).first()
       if user is None:
           raise HTTPException(status_code=404, detail="User not found")
       for password in passwords:
           db.delete(password)
       db.delete(user)
       db.commit()
       db.close()
       return {"message": f"User {user.username} deleted successfully"}

   except HTTPException as e:
       raise HTTPException(status_code=e.status_code, detail=str(e.detail))
