from fastapi import APIRouter
from app.utils.response_helper import reusable_response

router = APIRouter()

@router.get("/test/users")
def get_users():
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
    roles = {
        1: "admin",
        2: "user"
    }
    for user in users:
        user["role"] = roles.get(user["id"],"guest")
    
    return reusable_response(users, message="This is test response")



    
    



