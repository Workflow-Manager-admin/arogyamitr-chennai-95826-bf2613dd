from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix="/gamification",
    tags=["Gamification"],
)


class LeaderboardEntry(BaseModel):
    user_id: str
    score: float


class Badge(BaseModel):
    name: str
    description: str


class Challenge(BaseModel):
    name: str
    status: str


# PUBLIC_INTERFACE
@router.get(
    "/leaderboard",
    response_model=List[LeaderboardEntry],
    summary="Get health leaderboard"
)
async def leaderboard():
    """
    Show health leaderboard.
    """
    return [
        LeaderboardEntry(user_id="user123", score=9500),
        LeaderboardEntry(user_id="user555", score=9280),
    ]


# PUBLIC_INTERFACE
@router.get(
    "/badges/{user_id}",
    response_model=List[Badge],
    summary="Get badges for a user"
)
async def user_badges(user_id: str):
    """
    List earned and available badges.
    """
    return [
        Badge(
            name="Early Riser",
            description="Logged 7am wakeup for 7 days"
        ),
        Badge(
            name="Hydration Hero",
            description="Met water goal thrice a week"
        ),
    ]


# PUBLIC_INTERFACE
@router.get(
    "/challenges",
    response_model=List[Challenge],
    summary="Active health challenges"
)
async def get_challenges():
    """
    List ongoing community health challenges.
    """
    return [
        Challenge(name="10k Steps Week", status="open"),
        Challenge(name="Sugar-Free Challenge", status="open"),
    ]
