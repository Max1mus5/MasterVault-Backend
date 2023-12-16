from typing import Optional
from pydantic import BaseModel, Field


class PasswordResponse(BaseModel):
    message: str = Field(description="Message from the password service")

class CreatePasswordRequest(BaseModel):
    url: Optional[str] = Field(description="Optional new URL")
    title: str = Field(..., description="Title for the password")
    length: int = Field(..., description="Length of the password")
    min_uppercase: int = Field(..., description="Minimum number of uppercase characters")
    min_lowercase: int = Field(..., description="Minimum number of lowercase characters")
    min_numbers: int = Field(..., description="Minimum number of numeric characters")
    min_special_chars: int = Field(..., description="Minimum number of special characters")

class UpdatePasswordRequest(BaseModel):
    password_id: int = Field(description="ID of the password to update")
    url: Optional[str] = Field(description="Optional new URL")
    title: Optional[str] = Field(description="New title for the password")
    length: int = Field(..., description="Length of the password")
    min_uppercase: int = Field(..., description="Minimum number of uppercase characters")
    min_lowercase: int = Field(..., description="Minimum number of lowercase characters")
    min_numbers: int = Field(..., description="Minimum number of numeric characters")
    min_special_chars: int = Field(..., description="Minimum number of special characters")

class DeletePasswordRequest(BaseModel):
    password_id: int = Field(description="ID of the password to delete")