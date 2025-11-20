from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import *
from app.database.engine import create_db, get_async_session
from app.database.queries import orm_add_post, orm_get_feed


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get('/feed')
async def get_feed(
        session: AsyncSession = Depends(get_async_session)
):
    data = await orm_get_feed(session)

    result = []
    for i in data:
        result.append({
            'caption': i.caption,
            'url': i.url,
            'file_name': i.file_name,
            'file_type': i.file_type
        })

    return result


@app.post('/upload')
async def upload_post(
    caption: str,
    url: str,
    session: AsyncSession = Depends(get_async_session)
):
    await orm_add_post(session, caption, url)

