from fastapi import APIRouter

router = APIRouter()

@router.get("/coordinator/test")
def test():
    return {"message": "Coordinatot route working!"}