from django.apps import apps
from django.conf import settings
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.get("/liveness")
async def liveness_check():
    return {"status": "live"}


@router.get("/readiness")
async def readiness_check():
    return {"status": "ready"}


@router.get("/django-check")
async def django_check():
    return {
        "debug": settings.DEBUG,
        "installed_apps": settings.INSTALLED_APPS[:3],
        "apps_ready": apps.ready,
        "total_models": len(apps.get_models()),
    }
