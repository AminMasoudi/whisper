from fastapi import APIRouter
from schemas.user_schema import AuthRegister
from db.database import SessionDep
from services.auth_service import AuthService
from utils.security import TokenDep, TokenFormLogin

router = APIRouter()


@router.post("/register")
def register(user: AuthRegister, session: SessionDep):
    user = AuthService.register(
        session, user.username, user.password, user.display_name
    )
    return {"username": user.username}


@router.post("/login")
def login(form_data: TokenFormLogin, session: SessionDep):
    return {
        "access_token": AuthService.login(
            session, form_data.username, form_data.password
        ),
        "token_type": "bearer",
    }


@router.get("/me")
def me(token: TokenDep):
    return AuthService.user_info(token)
