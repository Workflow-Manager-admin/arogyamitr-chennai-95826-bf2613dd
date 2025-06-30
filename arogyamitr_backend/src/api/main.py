from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes import (
    wellness_dashboard,
    ai_recommendations,
    health_tracking,
    ayurveda,
    product_scanner,
    disease_mgmt,
    teleconsult,
    community,
    events,
    emergency,
    gamification,
    content,
)

app = FastAPI(
    title="ArogyaMitr Backend API",
    description="API for wellness, AI guidance, Ayurveda, disease management, community and more.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, set this appropriately
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["General"])
# PUBLIC_INTERFACE
def health_check():
    """
    Health check endpoint.

    Returns:
        dict: Service status.
    """
    return {"message": "Healthy"}


# Register all feature routers
app.include_router(wellness_dashboard.router)
app.include_router(ai_recommendations.router)
app.include_router(health_tracking.router)
app.include_router(ayurveda.router)
app.include_router(product_scanner.router)
app.include_router(disease_mgmt.router)
app.include_router(teleconsult.router)
app.include_router(community.router)
app.include_router(events.router)
app.include_router(emergency.router)
app.include_router(gamification.router)
app.include_router(content.router)
