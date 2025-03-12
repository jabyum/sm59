from fastapi import FastAPI
from api.photos.photo_api import photo_api
from api.users.users_api import user_router
from database import engine,Base
app = FastAPI(docs_url="/")
Base.metadata.create_all(bind=engine)
app.include_router(photo_api)
app.include_router(user_router)
# uvicorn main:app --reload