from fastapi import APIRouter
from app.controllers import category_stats_controller, stats_controller, top_categories_controller, daily_expenses_controller,system_controller

router = APIRouter()

router.include_router(stats_controller.router, prefix="/stats")
router.include_router(category_stats_controller.router, prefix="/stats")
router.include_router(top_categories_controller.router, prefix="/stats")
router.include_router(daily_expenses_controller.router, prefix="/stats")
router.include_router(system_controller.router, prefix="/stats")