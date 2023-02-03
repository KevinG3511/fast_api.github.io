"""Router"""

from fastapi import APIRouter
from .routes import servicio_1
router = APIRouter()

router.include_router(servicio_1.service1,prefix="/app1")



