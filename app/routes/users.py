from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import UserCreate, UserResponse, UserLogin
from app.crud import create_user, authenticate_user
from app.auth import create_access_token

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate):
    user_id = create_user(user)
    return {"id": user_id, "username": user.username, "email": user.email}

@router.post("/login")
def login_user(user: UserLogin):
    db_user = authenticate_user(user.email, user.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}
