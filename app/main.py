from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
