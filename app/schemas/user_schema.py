from pydantic import BaseModel

class AuthRegister(BaseModel):
    username: str
    display_name: str
    password: str