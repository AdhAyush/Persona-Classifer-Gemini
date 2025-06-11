from fastapi import FastAPI
from app.routes import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


# Allow all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use ["http://localhost:5500"] etc. in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router, prefix="/api")
