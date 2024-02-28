from fastapi import APIRouter, Depends, HTTPException
from services.passwords_service import PasswordService
from models.user import User
from utils.validation import validate_identity
from middlewares.auth_middleware import JWTBearer
from schemas.password_schemas import CreatePasswordRequest, UpdatePasswordRequest
from utils.validation import (
                            is_valid_password , 
                            is_valid_username , 
                            get_current_user)

password_router = APIRouter()

@password_router.post("/create", tags=["Passwords"])
async def create_password(
   password_data: CreatePasswordRequest,
   current_user: User = Depends(get_current_user),
   password_service: PasswordService = Depends(),
):
   try:
       if not is_valid_password(current_user.password):
           raise HTTPException(status_code=400, detail="Invalid password")

       if not is_valid_username(current_user.username):
           raise HTTPException(status_code=400, detail="Invalid username")

       if not validate_identity(current_user.username, current_user.password):
           raise HTTPException(status_code=401, detail="Invalid credentials")

       password_response = password_service.create_password(
           user_id=current_user.id,
           username=current_user.username, 
           title=password_data.title,
           URL=password_data.url,
           length=password_data.length,
           min_uppercase=password_data.min_uppercase,
           min_lowercase=password_data.min_lowercase,
           min_numbers=password_data.min_numbers,
           min_special_chars=password_data.min_special_chars,
       )

       return password_response
       
   except HTTPException as e:
       raise HTTPException(status_code=e.status_code, detail=str(e.detail))

@password_router.get("/get", tags=["Passwords"])
async def get_passwords(
    current_user: User = Depends(get_current_user),  
    password_service: PasswordService = Depends() 
):
    try:
        """         print("**************************************************************current_user", current_user.username)
        """        
        password_response = password_service.get_passwords(user_id=current_user.id)
        print
        return password_response
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@password_router.put("/update", tags=["Passwords"])
async def update_password(
    password_data: UpdatePasswordRequest,
    current_user: User = Depends(get_current_user),
    password_service: PasswordService = Depends(),
):
    try:
        if not validate_identity(current_user.username, current_user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        password_response = password_service.update_password(
           password_id=password_data.password_id,
           user_id=current_user.id,
           title=password_data.title,
           url=password_data.url,
           length=password_data.length,
           min_uppercase=password_data.min_uppercase,
           min_lowercase=password_data.min_lowercase,
           min_numbers=password_data.min_numbers,
           min_special_chars=password_data.min_special_chars,
        )

        return password_response
        
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e.detail))
    
@password_router.delete("/delete", tags=["Passwords"])
async def delete_password(
    password_id: int,
    current_user: User = Depends(get_current_user),
    password_service: PasswordService = Depends(),
):
    try:
        if not validate_identity(current_user.username, current_user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        password_response = password_service.delete_password(
           password_id=password_id,
           user_id=current_user.id,
        )

        return password_response
        
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e.detail))
    




   

