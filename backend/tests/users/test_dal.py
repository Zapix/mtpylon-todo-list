# -*- coding: utf-8 -*-
import pytest

from mtpylon.crypto import AuthKey  # type: ignore

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
async def test_create_auth_key(async_session, user):
    auth_key_value = 0x4fa4120d3646e1cadc7e21fcc9c46111ff8467665908a56b18bd38bee60ee1cccc2eff69dda5e638be2b06e813e6d9832142a054d22f405d9d416f79168140d373b048f55924b836ec5be2ab92e29624edf67bd5d763f8a15c3aed587e7ac70f8fe0d78de45c4b9ea5b81a1e0a098eb064dc9609fa37ca33f703b48461aed343aabc1498dd4d1cbbf3ca4c56cc8c7dc315e251e28312ed258c74326729118251f9153f7ac9d52bd47fdf7072963f6330f06bb72e2cc744af91df3302800e80c23c25a402b97bfc5292589b1c688bd1fde0e9997d9996a32ebd39ba258137b123fa762fd07548c44fd1b9321778f6ec3464ae39402c0445bd02fa8223b30cdfc8  # noqa
    mtpylon_auth_key = AuthKey(value=auth_key_value)

    async with async_session() as session:
        auth_key = await create_auth_key(session, user, mtpylon_auth_key)

    assert auth_key.id is not None
    assert auth_key.auth_key_id == mtpylon_auth_key.id
