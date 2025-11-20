from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import Post


async def orm_get_feed(session: AsyncSession):
    query = select(Post)
    result = await session.execute(query)
    return result.scalars().all()


async def orm_add_post(session: AsyncSession, caption, url):
    session.add(Post(
            caption=caption,
            url=url,
        )
    )




