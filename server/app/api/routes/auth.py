from fastapi import APIRouter
from schemas.user_schema import AuthRegister
from db.database import SessionDep
from services.auth_service import AuthService

router = APIRouter()


@router.post("/auth/register")
def register(user: AuthRegister, session: SessionDep):
    user = AuthService.register(session, user.username, user.password)
    return {"username": user.username}
