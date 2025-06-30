from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix="/community",
    tags=["Community & Forums"],
)


class ForumMessage(BaseModel):
    user_id: str
    message: str


# PUBLIC_INTERFACE
@router.get(
    "/forum/{topic}",
    response_model=List[ForumMessage],
    summary="Fetch messages for a forum topic"
)
async def fetch_messages(topic: str):
    """
    Fetch messages/posts for a given community forum topic.
    """
    return [
        ForumMessage(user_id="user123", message="Anyone tried the yoga challenge?"),
        ForumMessage(user_id="user456", message="Yes! I noticed better sleep.")
    ]


# PUBLIC_INTERFACE
@router.post(
    "/forum/{topic}",
    summary="Post a message to the forum"
)
async def post_message(topic: str, data: ForumMessage):
    """
    Post a message to a forum topic.
    """
    return {"status": "posted", "topic": topic, "message": data}
