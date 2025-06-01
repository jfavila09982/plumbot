from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
    return users


