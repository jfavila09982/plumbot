from fastapi import APIRouter
from app.controllers import user_controller ,test_controller

router = APIRouter()
router.include_router(user_controller.router)

#test controller (familiarization phase)
router.include_router(test_controller.router)
