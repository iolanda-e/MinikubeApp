from fastapi import APIRouter
from app.controllers import stats_controller

router = APIRouter()

router.include_router(stats_controller.router, prefix="/stats")
