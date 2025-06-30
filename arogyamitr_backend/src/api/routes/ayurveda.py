from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import List, Dict

router = APIRouter(
    prefix="/ayurveda",
    tags=["Ayurveda & Dosha"],
)


class DoshaAssessmentRequest(BaseModel):
    answers: List[int] = Field(..., description="Encoded quiz answers for dosha assessment")


class DoshaResult(BaseModel):
    dominant_dosha: str
    proportions: Dict[str, float]
    description: str
    guidance: str


# PUBLIC_INTERFACE
@router.post(
    "/assess",
    response_model=DoshaResult,
    summary="Get Ayurvedic dosha profile"
)
async def assess_dosha(data: DoshaAssessmentRequest):
    """
    Returns user's dosha profile based on their answers.

    Returns:
        DoshaResult: Dosha and advice.
    """
    # Simulated logic
    return DoshaResult(
        dominant_dosha="Pitta",
        proportions={"Vata": 0.2, "Pitta": 0.6, "Kapha": 0.2},
        description="Pitta types are energetic and ambitious but should avoid excessive heat.",
        guidance="Favor cooling foods, regular meals, and meditation."
    )
