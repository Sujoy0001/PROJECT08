from fastapi import FastAPI
from routes import auth_routes, technician_profile_routes, show_all

app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "Welcome to the FTech API!"}

app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(technician_profile_routes.router, tags=["technicians"])
app.include_router(show_all.router, prefix="/show", tags=["show"])