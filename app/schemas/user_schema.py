from pydantic import BaseModel

class AuthRegister(BaseModel):
    username: str
    password: str