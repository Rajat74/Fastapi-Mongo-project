from fastapi import FastAPI
from app.routes import users, link

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(link.router, prefix="/link", tags=["link"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI and MongoDB project"}
