from fastapi import FastAPI
from app.routes import users, clothes, tryon
from app.database import Base, engine

# Initialize the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(clothes.router, prefix="/clothes", tags=["clothes"])
app.include_router(tryon.router, prefix="/tryon", tags=["tryon"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Mais Online Clothing Store"}
