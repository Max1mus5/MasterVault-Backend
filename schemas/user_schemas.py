from pydantic import BaseModel

class userS(BaseModel):
  username: str
  email: str
  password:str
