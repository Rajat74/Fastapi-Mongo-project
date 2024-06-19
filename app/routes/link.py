from fastapi import APIRouter, Depends, HTTPException
from app.schemas import LinkID
from app.models import User
from app.crud import link_external_id
from app.auth import get_current_user

router = APIRouter()

@router.post("/")
def link_id(link_data: LinkID, current_user: User = Depends(get_current_user)):
    if not link_external_id(link_data.user_id, link_data.external_id):
        raise HTTPException(status_code=400, detail="Failed to link ID")
    return {"message": "ID linked successfully"}
