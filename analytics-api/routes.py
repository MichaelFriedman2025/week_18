from fastapi import APIRouter


router = APIRouter()


@router.get("/analytics/alerts-by-border-and-priority")
def get_alerts_by_border_and_priority():
    pass