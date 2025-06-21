from fastapi import FastAPI
from routes import auth_routes, technician_profile_routes, show_all

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(technician_profile_routes.router, tags=["technicians"])
app.include_router(show_all.router, prefix="/show", tags=["show"])