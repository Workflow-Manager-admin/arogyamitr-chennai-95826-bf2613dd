from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/scanner",
    tags=["Product Scanner & AI Scoring"],
)


class ScanResult(BaseModel):
    product_name: str = Field(..., description="Name of scanned product")
    ethical_score: float = Field(
        ..., description="AI-computed ethical/nutrition score [0-100]"
    )
    advisories: list = Field(..., description="Health advisories or suggestions")


# PUBLIC_INTERFACE
@router.post(
    "/barcode",
    response_model=ScanResult,
    summary="Scan product barcode for scoring"
)
async def scan_barcode(barcode: str = File(...)):
    """
    Scan product barcode to deliver AI-based ethical/nutritional rating.
    """
    # Simulate lookup
    return ScanResult(
        product_name="Packaged Fruit Juice",
        ethical_score=68.0,
        advisories=["Limit added sugar intake"]
    )


# PUBLIC_INTERFACE
@router.post(
    "/photo",
    response_model=ScanResult,
    summary="Scan product photo for scoring"
)
async def scan_photo(file: UploadFile = File(...)):
    """
    Scan product photo to deliver AI-based ethical/nutritional rating.
    """
    return ScanResult(
        product_name="Instant Noodles",
        ethical_score=45.0,
        advisories=["Ultra-processed: occasional use only"]
    )
