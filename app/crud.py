from app.database import db
from app.models import User
from bson import ObjectId
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_user(user: User):
    user.password = get_password_hash(user.password)
    result = db.users.insert_one(user.dict(by_alias=True))
    return str(result.inserted_id)

def get_user_by_email(email: str):
    user = db.users.find_one({"email": email})
    if user:
        user["_id"] = str(user["_id"])  
    return user

def authenticate_user(email: str, password: str):
    user = get_user_by_email(email)
    if user and verify_password(password, user["password"]):
        return user  
    return None

def link_external_id(user_id: str, external_id: str):
    result = db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"external_id": external_id}})
    return result.modified_count > 0

def delete_user_and_data(user_id: str):
    db.users.delete_one({"_id": ObjectId(user_id)})
    db.other_collection.delete_many({"user_id": user_id})
