from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix="/content",
    tags=["Educational Content"],
)


class ContentArticle(BaseModel):
    id: str
    title: str
    summary: str
    body: str
    language: str


# PUBLIC_INTERFACE
@router.get(
    "/",
    response_model=List[ContentArticle],
    summary="Get educational articles (multi-language)"
)
async def get_articles(language: str = Query("en")):
    """
    List health & wellness educational articles, filtered by language.
    """
    # Simulated articles
    return [
        ContentArticle(
            id="article1",
            title="Why Hydration Matters",
            summary="An intro to hydration in daily wellness.",
            body="Staying hydrated supports your digestion, focus, and overall health...",
            language=language
        ),
        ContentArticle(
            id="article2",
            title="आयुर्वेद में आहार के सिद्धांत",
            summary="भारतीय परंपरा में भोजन के बारे में जानें",
            body="आयुर्वेद आहार को शरीर और मन का पोषण मानता है...",
            language="hi"
        ),
    ]
