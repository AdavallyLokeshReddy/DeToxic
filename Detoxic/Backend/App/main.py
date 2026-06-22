"""
Main FastAPI application entry. Adds routes and a health endpoint.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import predict, auth, submissions, analytics, admin

app = FastAPI(title="Detoxic API")

# Allow frontend dev server origins during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "http://localhost:8080", "http://127.0.0.1:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict.router, prefix="/api")
app.include_router(auth.router, prefix="/api")
app.include_router(submissions.router, prefix="/api")
app.include_router(analytics.router, prefix="/api")
app.include_router(admin.router, prefix="/api")


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    # run with package path so relative imports work when started from project root
    uvicorn.run("Backend.App.main:app", host="0.0.0.0", port=5000, reload=True)
