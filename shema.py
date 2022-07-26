from pydantic import BaseModel


class BaseUser(BaseModel):
    login: str
    discription: str

    class Config:
        orm_mode = True


class CreateUser(BaseUser):
    password: str



