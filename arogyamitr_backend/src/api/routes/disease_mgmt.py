from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(
    prefix="/disease",
    tags=["Disease Management"],
)


class DiseaseTrend(BaseModel):
    condition: str
    trend_score: float
    recent_anomalies: Optional[str]


class MedicationReminder(BaseModel):
    medication: str
    time: str


# PUBLIC_INTERFACE
@router.get(
    "/trends/{user_id}",
    response_model=List[DiseaseTrend],
    summary="Get disease trend & anomaly info"
)
async def get_disease_trends(user_id: str):
    """
    Returns trending and anomalies for disease management.
    """
    return [
        DiseaseTrend(
            condition="Type 2 Diabetes",
            trend_score=0.82,
            recent_anomalies="Fasting sugar > 140"
        )
    ]


# PUBLIC_INTERFACE
@router.post(
    "/medication/reminder",
    summary="Set a medication reminder"
)
async def set_medication_reminder(reminder: MedicationReminder):
    """
    Set a medication reminder/alarm for a user.
    """
    return {"status": "scheduled", "reminder": reminder}


# PUBLIC_INTERFACE
@router.post(
    "/upload",
    summary="Upload medical record/file"
)
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a medical file linked to user's disease management module.
    """
    return {"filename": file.filename, "status": "received"}
