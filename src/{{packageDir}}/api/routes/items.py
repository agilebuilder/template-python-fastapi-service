from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ...db.session import get_session
from ...models.item import Item
from ...schemas.item import ItemCreate, ItemRead
from ...services import item as item_service

router = APIRouter(prefix="/items", tags=["items"])


@router.get("", response_model=list[ItemRead])
async def list_items(session: AsyncSession = Depends(get_session)) -> list[Item]:
    return await item_service.list_items(session)


@router.post("", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
async def create_item(payload: ItemCreate, session: AsyncSession = Depends(get_session)) -> Item:
    return await item_service.create_item(session, payload)


@router.get("/{item_id}", response_model=ItemRead)
async def get_item(item_id: int, session: AsyncSession = Depends(get_session)) -> Item:
    item = await item_service.get_item(session, item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item
