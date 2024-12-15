from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user(
        user_id: Annotated[int, Path(gt=0,
                                     title="User ID",
                                     description="The ID must be a positive integer")]):
    return f'Вы вошли как пользователь № {user_id}'

@app.get('/user/{username}/{age}')
async def user_info(username: str = Path(min_length=5, max_length=20, description='Enter username', examples='UrbanUser'),
                    age: int = Path(ge=18, le=120, description='Enter age', examples='24')):
    return {'message': f'Информация о пользователе. Имя: {username} Возраст: {age}'}

