from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix="/events",
    tags=["Local Events & Resources"],
)


class HealthEvent(BaseModel):
    name: str
    location: str
    start_time: str
    details: str


class ResourceEntry(BaseModel):
    name: str
    type: str
    contact: str


# PUBLIC_INTERFACE
@router.get(
    "/nearby",
    response_model=List[HealthEvent],
    summary="Discover local health events"
)
async def discover_events(city: str = Query(...)):
    """
    List local health/wellness events by city.
    """
    return [
        HealthEvent(
            name="Chennai Yoga Camp",
            location="Marina Beach Park",
            start_time="2024-07-05T07:00:00",
            details="Free public yoga session"
        )
    ]


# PUBLIC_INTERFACE
@router.get(
    "/resources",
    response_model=List[ResourceEntry],
    summary="Get local health resource directory"
)
async def get_resources(resource_type: str = Query(...)):
    """
    List local health resources (clinics, ayurvedic healers, fitness centers).
    """
    return [
        ResourceEntry(
            name="Wellness Clinic Chennai",
            type="Clinic",
            contact="+914400112233"
        ),
        ResourceEntry(
            name="SS Ayurveda",
            type="Ayurvedic Healer",
            contact="+919876543210"
        ),
    ]
