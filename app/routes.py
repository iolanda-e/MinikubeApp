from fastapi import APIRouter
from app.controllers import category_stats_controller, stats_controller

router = APIRouter()

router.include_router(stats_controller.router, prefix="/stats")
router.include_router(category_stats_controller.router, prefix="/stats")