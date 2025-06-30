from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix="/emergency",
    tags=["Emergency Access"],
)


class EmergencyContact(BaseModel):
    name: str
    phone: str


class Location(BaseModel):
    lat: float
    lng: float


# PUBLIC_INTERFACE
@router.get(
    "/contacts/{user_id}",
    response_model=List[EmergencyContact],
    summary="List emergency contacts for user"
)
async def get_emergency_contacts(user_id: str):
    """
    Returns pre-configured emergency contacts for a user.
    """
    return [
        EmergencyContact(name="Mother", phone="+911234567890"),
        EmergencyContact(name="Doctor", phone="+919812345678")
    ]


# PUBLIC_INTERFACE
@router.post(
    "/share-location",
    summary="Share live location for emergency"
)
async def share_location(user_id: str, location: Location):
    """
    Accepts and records user's current geolocation in case of emergency.
    """
    return {
        "status": "location_sent",
        "lat": location.lat,
        "lng": location.lng,
        "user_id": user_id
    }
