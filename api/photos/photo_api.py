from fastapi import APIRouter, UploadFile, File
import random
photo_api = APIRouter(prefix="/photo",
                      tags=["Фотографии"])

@photo_api.post("/add-photo")
async def add_photo1(post_id: int | None=None,
                     user_id: int | None=None,
                     photo_file: UploadFile = File(...)):
    file_id = random.randint(1, 1000000000000)
    info_id = post_id if post_id else user_id
    if photo_file:
        # создаем пустой файл для сохранения кода фотографии,
        # которую получили от пользователя
        photo_in_project = open(f"database/users_photo/photo_{file_id}_{info_id}.jpg",
                                "wb")
        try:
            # читаем код файла, который отправил юзер
            photo_to_save = await photo_file.read()
            # переписываем код в наш пустой файл
            photo_in_project.write(photo_to_save)
        except:
            return {"status": 0, "message": "ошибка загрузки"}
        finally:
            photo_in_project.close()
        return {"status": 1, "message": "успешно загружено"}

@photo_api.post("/add-photo2")
async def add_photo2(post_id: int | None=None,
                     user_id: int | None=None,
                     photo_file: UploadFile = File(...)):
    file_id = random.randint(1, 1000000000000)
    info_id = post_id if post_id else user_id
    if photo_file:
        # создаем пустой файл через контекстный менеджер для сохранения кода фотографии,
        # которую получили от пользователя
        with open(f"database/users_photo/photo_{file_id}_{info_id}.jpg",
                                "wb") as photo_in_project:
            try:
                # читаем код файла, который отправил юзер
                photo_to_save = await photo_file.read()
                # переписываем код в наш пустой файл
                photo_in_project.write(photo_to_save)
            except:
                return {"status": 0, "message": "ошибка загрузки"}
            return {"status": 1, "message": "успешно загружено"}
@photo_api.post("/add-text")
async def add_text(username:str, text:str):
    with open("database/text.txt", "at") as file:
        file.write("\n"+ username + ": "+text)
        return {"status": 1, "message": "успешно"}