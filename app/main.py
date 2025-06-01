from fastapi import FastAPI
from app.routes.api import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to your Laravel-style FastAPI app"}
