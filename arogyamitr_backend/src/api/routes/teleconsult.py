from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel

router = APIRouter(
    prefix="/teleconsult",
    tags=["Tele-Consultations"],
)


class TeleConsultSession(BaseModel):
    session_id: str
    user_id: str
    doctor_id: str
    scheduled_time: str


# PUBLIC_INTERFACE
@router.post(
    "/start",
    response_model=TeleConsultSession,
    summary="Initiate a tele-consult session"
)
async def start_teleconsult(user_id: str, doctor_id: str):
    """
    Start a new tele-consultation session.
    """
    return TeleConsultSession(
        session_id="TS123",
        user_id=user_id,
        doctor_id=doctor_id,
        scheduled_time="2024-07-01T10:00:00"
    )


# PUBLIC_INTERFACE
@router.post(
    "/share",
    summary="Securely share a medical file with the doctor"
)
async def share_file(session_id: str, file: UploadFile = File(...)):
    """
    Secure upload of file in a teleconsultation.
    """
    return {"session_id": session_id, "filename": file.filename, "status": "shared"}
