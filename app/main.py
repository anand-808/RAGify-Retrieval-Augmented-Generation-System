from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.auth.firebase_auth import verify_firebase_token

app = FastAPI(
    title="RAGify API",
    description="Retrieval-Augmented Generation system using FastAPI",
    version="1.0.0"
)

# Allow CORS (for frontend or external tools later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check route
@app.get("/")
def read_root():
    return {"message": "Welcome to RAGify API"}

@app.get("/protected")
def protected_route(user_data=Depends(verify_firebase_token)):
    return {"message": f"Hello {user_data['email']}, you're authenticated!"}