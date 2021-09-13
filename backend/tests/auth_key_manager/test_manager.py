# -*- coding: utf-8 -*-
import pytest
from unittest.mock import patch

from sqlalchemy.orm import sessionmaker
from mtpylon.crypto import AuthKey
from mtpylon.crypto.exceptions import AuthKeyDoesNotExist

from auth_key_manager.manager import AuthKeyDbManager
from auth_key_manager.dal import (
    get_key,
    create_key
)


@pytest.mark.asyncio
async def test_set_key_from_int(
    async_session: sessionmaker,
    mtpylon_auth_key: AuthKey
):
    manager = AuthKeyDbManager()

    with patch('auth_key_manager.manager.async_session', async_session):
        await manager.set_key(mtpylon_auth_key.value)

    async with async_session() as session:
        key = await get_key(session, mtpylon_auth_key.id)

        assert key is not None


@pytest.mark.asyncio
async def test_set_key_from_auth_key(
    async_session: sessionmaker,
    mtpylon_auth_key: AuthKey
):
    manager = AuthKeyDbManager()

    with patch('auth_key_manager.manager.async_session', async_session):
        await manager.set_key(mtpylon_auth_key)

    async with async_session() as session:
        key = await get_key(session, mtpylon_auth_key.id)

        assert key is not None


@pytest.mark.asyncio
async def test_has_key_by_id(
    async_session: sessionmaker,
    mtpylon_auth_key: AuthKey
):
    manager = AuthKeyDbManager()

    async with async_session() as session:
        await create_key(session, mtpylon_auth_key)

    with patch('auth_key_manager.manager.async_session', async_session):
        assert await manager.has_key(mtpylon_auth_key.id)


@pytest.mark.asyncio
async def test_has_key_by_auth_key(
    async_session: sessionmaker,
    mtpylon_auth_key: AuthKey,
):
    manager = AuthKeyDbManager()

    async with async_session() as session:
        await create_key(session, mtpylon_auth_key)

    with patch('auth_key_manager.manager.async_session', async_session):
        assert await manager.has_key(mtpylon_auth_key)


@pytest.mark.asyncio
async def test_has_key_by_id_false(
    async_session: sessionmaker,
    mtpylon_auth_key: AuthKey
):
    manager = AuthKeyDbManager()

    with patch('auth_key_manager.manager.async_session', async_session):
        assert not await manager.has_key(mtpylon_auth_key.id)


@pytest.mark.asyncio
async def test_has_key_by_auth_key_false(
    async_session: sessionmaker,
    mtpylon_auth_key: AuthKey,
):
    manager = AuthKeyDbManager()

    with patch('auth_key_manager.manager.async_session', async_session):
        assert not await manager.has_key(mtpylon_auth_key)


@pytest.mark.asyncio
async def test_get_key_by_id(
    async_session: sessionmaker,
    mtpylon_auth_key: AuthKey,
):
    manager = AuthKeyDbManager()

    async with async_session() as session:
        await create_key(session, mtpylon_auth_key)

    with patch('auth_key_manager.manager.async_session', async_session):
        result = await manager.get_key(mtpylon_auth_key.id)

    assert isinstance(result, AuthKey)
    assert result == mtpylon_auth_key


@pytest.mark.asyncio
async def test_get_key_by_id_not_found(
    async_session: sessionmaker,
    mtpylon_auth_key: AuthKey,
):
    manager = AuthKeyDbManager()

    with pytest.raises(AuthKeyDoesNotExist):
        with patch('auth_key_manager.manager.async_session', async_session):
            await manager.get_key(mtpylon_auth_key.id)


@pytest.mark.asyncio
async def test_delete_key_by_id(
    async_session: sessionmaker,
    mtpylon_auth_key: AuthKey,
):
    manager = AuthKeyDbManager()
    async with async_session() as session:
        await create_key(session, mtpylon_auth_key)

    with patch('auth_key_manager.manager.async_session', async_session):
        await manager.del_key(mtpylon_auth_key.id)

        assert not await manager.has_key(mtpylon_auth_key.id)


@pytest.mark.asyncio
async def test_delete_key_by_auth_key(
        async_session: sessionmaker,
        mtpylon_auth_key: AuthKey,
):
    manager = AuthKeyDbManager()
    async with async_session() as session:
        await create_key(session, mtpylon_auth_key)

    with patch('auth_key_manager.manager.async_session', async_session):
        await manager.del_key(mtpylon_auth_key)

        assert not await manager.has_key(mtpylon_auth_key.id)
