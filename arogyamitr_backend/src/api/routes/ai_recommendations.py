from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional, List

router = APIRouter(
    prefix="/recommendations",
    tags=["AI Recommendations"],
)


class RecommendationRequest(BaseModel):
    user_id: str = Field(..., description="User ID")
    context: Optional[str] = Field(
        None,
        description="Context for recommendation, e.g. 'breakfast', 'midnight snack'"
    )


class Recommendation(BaseModel):
    title: str
    summary: str
    actions: List[str]


# PUBLIC_INTERFACE
@router.post(
    "/meal",
    response_model=Recommendation,
    summary="AI meal recommendations"
)
async def recommend_meal(data: RecommendationRequest):
    """
    Returns personalized meal recommendation using AI and user context.

    Parameters:
        data (RecommendationRequest): User ID and context.

    Returns:
        Recommendation: Suggested meal and guidance.
    """
    # Simulated AI response
    return Recommendation(
        title="Wholesome South Indian Breakfast",
        summary=(
            "Based on your dosha and energy level, idli with sambar and coconut chutney is ideal today."
        ),
        actions=["Have tender coconut water", "Eat before 9am", "Add a fruit bowl"]
    )


# PUBLIC_INTERFACE
@router.post(
    "/activity",
    response_model=Recommendation,
    summary="AI activity recommendations"
)
async def recommend_activity(data: RecommendationRequest):
    """
    Returns personalized fitness/movement activity recommendations.

    Returns:
        Recommendation: Workout or activity plan.
    """
    return Recommendation(
        title="Yoga Flow & Evening Walk",
        summary=(
            "A 20-minute yoga session and a 30-minute walk are "
            "recommended for holistic balance."
        ),
        actions=["Try gentle Surya Namaskar", "Prefer outdoor walk"]
    )


# PUBLIC_INTERFACE
@router.post(
    "/lifestyle",
    response_model=Recommendation,
    summary="AI lifestyle tips"
)
async def recommend_lifestyle(data: RecommendationRequest):
    """
    Returns personalized lifestyle guidance, routines and tips.

    Returns:
        Recommendation: Actionable advice.
    """
    return Recommendation(
        title="Tech Detox & Mindfulness",
        summary=(
            "Unplug post-dinner, meditate for 15 minutes, "
            "and avoid screens after 9pm."
        ),
        actions=[
            "Set an 8:45pm reminder",
            "Try guided meditation audio"
        ]
    )
