from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlalchemy

# Database setup
database_url = "sqlite:///./test.db"  # Example using SQLite
database_engine = sqlalchemy.create_engine(database_url)

# Create FastAPI app
app = FastAPI()

# CORS configuration
origins = ["http://localhost:3000", "https://yourproductionurl.com"]  # Allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Basic route
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Global Business Search API!"}

# Additional routes can go here...
