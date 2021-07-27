# -*- coding: utf-8 -*-
import pytest

from users.dal import (
    create_user,
    get_user,
)


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


@pytest.mark.asyncio
async def test_get_user_by_nickname(async_session, user):
    async with async_session() as session:
        returned_user = await get_user(session, nickname=user.nickname)

    assert returned_user is not None
    assert returned_user.id == user.id
    assert returned_user.nickname == user.nickname


@pytest.mark.asyncio
async def test_get_user_by_id(async_session, user):
    async with async_session() as session:
        returned_user = await get_user(session, user_id=user.id)

    assert returned_user is not None
    assert returned_user.id == user.id
    assert returned_user.nickname == user.nickname


@pytest.mark.asyncio
async def test_get_user_by_nickname_none(async_session):
    async with async_session() as session:
        returned_user = await get_user(session, nickname='fake_user')

    assert returned_user is None


@pytest.mark.asyncio
async def test_get_user_by_id_none(async_session):
    async with async_session() as session:
        returned_user = await get_user(session, user_id=-1)

    assert returned_user is None
