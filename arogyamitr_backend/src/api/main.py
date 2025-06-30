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
from src.api.db import init_db, User, SessionLocal
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

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


# Ensure DB and example table are created at app startup
@app.on_event("startup")
def on_startup():
    """Initialize database and tables at application startup."""
    init_db()


@app.get("/", tags=["General"])
# PUBLIC_INTERFACE
def health_check():
    """
    Health check endpoint.

    Returns:
        dict: Service status.
    """
    return {"message": "Healthy"}


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# PUBLIC_INTERFACE
class UserCreate(BaseModel):
    """Pydantic model for creating a new user."""
    name: str
    email: str


# PUBLIC_INTERFACE
@app.post("/test/user", tags=["DB Gateway"], summary="Create example user in DB")
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    """
    Create a sample user in the SQLite DB for backend/frontend integration testing.

    Parameters:
        data (UserCreate): name and email
    Returns:
        dict: user ID and email, or error if already exists.
    """
    db_user = db.query(User).filter((User.email == data.email) | (User.name == data.name)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists with this name or email")
    user = User(name=data.name, email=data.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": user.id, "name": user.name, "email": user.email}


# PUBLIC_INTERFACE
@app.get("/test/users", tags=["DB Gateway"], summary="List all users")
def get_users(db: Session = Depends(get_db)):
    """
    List all users in the SQLite DB as a connectivity test.

    Returns:
        list: User records
    """
    return [
        {"id": user.id, "name": user.name, "email": user.email}
        for user in db.query(User).all()
    ]


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
