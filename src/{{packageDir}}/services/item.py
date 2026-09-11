from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.item import Item
from ..schemas.item import ItemCreate


async def list_items(session: AsyncSession) -> list[Item]:
    result = await session.execute(select(Item).order_by(Item.id))
    return list(result.scalars().all())


async def create_item(session: AsyncSession, payload: ItemCreate) -> Item:
    item = Item(name=payload.name, description=payload.description)
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item


async def get_item(session: AsyncSession, item_id: int) -> Item | None:
    result = await session.execute(select(Item).where(Item.id == item_id))
    return result.scalar_one_or_none()
