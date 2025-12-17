from fastapi import FastAPI
from app.routes import router as all_routes

app = FastAPI(
    title="Expense Stats API",
    version="1.0.0",
)

app.include_router(all_routes)

# @app.get("/health")
# def health():
#     return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)