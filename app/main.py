from fastapi import FastAPI
from .db import engine, Base
from app.controllers import user_controller

app = FastAPI(title="YT→MP3 MVP (main + DB)")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"ok": True}

app.include_router(user_controller.router)
