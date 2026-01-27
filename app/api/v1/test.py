from fastapi import APIRouter

router = APIRouter(prefix="/test", tags=["Test"])

@router.get("/hello")
def hello_test():
    return {
        "status": "ok",
        "message": "Hello World from FastAPI 🚀"
    }