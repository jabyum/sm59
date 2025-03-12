from fastapi import APIRouter
from pydantic import BaseModel, constr
import re
from database.userservice import *
user_router = APIRouter(tags=["Пользовательская часть"],
                        prefix="/user")
regex_mail = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
regex_phone = re.compile(r"^(?:\+998|998)[\d]{9}$")
class User(BaseModel):
    username: str
    phone_number: str
    email: str
    password: constr(min_length=5, max_length=10)
    birthday: str | None = None
    city: str | None = None
def mail_checker(email):
    if re.match(regex_mail, email):
        return True
    return False
@user_router.post("/register")
async def registration(user_model: User):
    data = dict(user_model)
    mail_validator = mail_checker(data.get("email"))
    if not mail_validator:
        return {"status":0, "message": "неправильный формат почты"}
    result = add_user_db(**data)
    return {"status": 1, "message": result}

