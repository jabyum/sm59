from fastapi import FastAPI
from api.photos.photo_api import photo_api
app = FastAPI(docs_url="/")
app.include_router(photo_api)
# uvicorn main:app --reload