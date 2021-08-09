# -*- coding: utf-8 -*-
import pytest

from users.dal import (
    create_user,
    get_user,
    create_auth_key,
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


@pytest.mark.asyncio
async def test_get_user_by_auth_key(async_session, user, mtpylon_auth_key):
    async with async_session() as session:
        await create_auth_key(session, user, mtpylon_auth_key)
        returned_user = await get_user(session, auth_key=mtpylon_auth_key)

    assert returned_user is not None
    assert returned_user.id == user.id


@pytest.mark.asyncio
async def test_get_user_by_auth_key_big_id(
    async_session,
    user,
    mtpylon_auth_key_big_id
):
    async with async_session() as session:
        await create_auth_key(
            session,
            user,
            mtpylon_auth_key_big_id
        )
        returned_user = await get_user(
            session,
            auth_key=mtpylon_auth_key_big_id
        )

    assert returned_user is not None
    assert returned_user.id == user.id


@pytest.mark.asyncio
async def test_get_user_by_auth_key_none(async_session, mtpylon_auth_key):
    async with async_session() as session:
        returned_user = await get_user(session, auth_key=mtpylon_auth_key)

    assert returned_user is None


@pytest.mark.asyncio
async def test_create_auth_key(async_session, user, mtpylon_auth_key):
    async with async_session() as session:
        auth_key = await create_auth_key(session, user, mtpylon_auth_key)

    assert auth_key.id is not None
    assert auth_key.auth_key_id == mtpylon_auth_key.id


@pytest.mark.asyncio
async def test_create_auth_key_with_big_auth_id(
    async_session,
    user,
    mtpylon_auth_key_big_id
):
    negative_id = int.from_bytes(
        mtpylon_auth_key_big_id.id.to_bytes(8, 'little'),
        'little',
        signed=True
    )
    async with async_session() as session:
        auth_key = await create_auth_key(
            session,
            user,
            mtpylon_auth_key_big_id
        )

    assert auth_key.id is not None
    assert auth_key.auth_key_id < 0
    assert auth_key.auth_key_id == negative_id
