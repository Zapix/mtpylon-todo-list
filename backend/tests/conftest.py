# -*- coding: utf-8 -*-
import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from db import Base


@pytest.fixture
async def db_engine():
    engine = create_async_engine('sqlite+aiosqlite://')
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    return engine


@pytest.fixture
async def async_session(db_engine):
    return sessionmaker(db_engine, expire_on_commit=False, class_=AsyncSession)
