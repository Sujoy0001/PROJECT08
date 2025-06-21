from fastapi import FastAPI
from routes import auth_routes

app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "Welcome to the FTech API!"}

app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])