from fastapi import APIRouter

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/type_device/{id}")
async def get_type_device(type_device_id: int):
    pass


@router.get("")
async def get_type_device_list():
    pass


@router.post("")
async def add_type_device(session):
    type_device = ''
    await session.execute(type_device)
    await session.commit()
    return {"status": "success"}


