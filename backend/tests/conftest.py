# -*- coding: utf-8 -*-
import pytest
from faker import Faker

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from db import Base
from users.models import User


@pytest.fixture
def fake():
    return Faker()


@pytest.fixture
async def db_engine():
    engine = create_async_engine('sqlite+aiosqlite://')
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    return engine


@pytest.fixture
async def async_session(db_engine) -> sessionmaker:
    return sessionmaker(db_engine, expire_on_commit=False, class_=AsyncSession)


@pytest.fixture
async def user(faker: Faker, async_session: sessionmaker) -> User:
    async with async_session() as session:
        user = User(
            nickname=faker.name(),
            password='e4ecd6fc11898565af24977e992cea0c9c7b7025'
        )
        session.add(user)
        await session.commit()
    return user
