from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import List

router = APIRouter(
    prefix="/dashboard",
    tags=["Wellness Dashboard"],
)


class UserDashboardSummary(BaseModel):
    user_id: str = Field(..., description="Unique user identifier")
    energy_score: float = Field(..., description="Energy score out of 100")
    hydration: float = Field(..., description="Hydration level as percentage")
    recent_activities: List[str] = Field(
        ..., description="Recent activity summaries"
    )
    top_goals: List[str] = Field(..., description="User's top goals")


# PUBLIC_INTERFACE
@router.get(
    "/{user_id}",
    response_model=UserDashboardSummary,
    summary="Get a user's personalized wellness dashboard"
)
async def get_dashboard(user_id: str):
    """
    Returns a summary of the user's wellness dashboard.

    Parameters:
        user_id (str): Unique user identifier.

    Returns:
        UserDashboardSummary: High-level KPIs and recommendations.
    """
    # Dummy implementation
    return UserDashboardSummary(
        user_id=user_id,
        energy_score=82.5,
        hydration=90.0,
        recent_activities=[
            "Morning yoga",
            "10,000 steps walked",
            "8h sleep"
        ],
        top_goals=[
            "Drink 2L water",
            "Meditate 15 min",
            "Sleep by 10pm"
        ]
    )
