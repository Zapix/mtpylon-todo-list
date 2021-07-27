# -*- coding: utf-8 -*-
import pytest

from users.dal import create_user


@pytest.mark.asyncio
async def test_create_user(async_session):
    async with async_session() as session:
        user = await create_user(session, 'johndoe', 'hashed_password')
    assert user.id is not None


@pytest.mark.asyncio
async def test_create_unique_exception(async_session):
    async with async_session() as session:
        await create_user(session, 'test', 'hashed_password')

        with pytest.raises(ValueError):
            await create_user(session, 'test', 'another_hashed')
