# -*- coding: utf-8 -*-
import pytest

from sqlalchemy.orm import sessionmaker
from mtpylon.crypto import AuthKey as MtpylonAuthKey

from auth_key_manager.dal import create_key


@pytest.mark.asyncio
async def test_create_key_success(
    async_session: sessionmaker,
    mtpylon_auth_key: MtpylonAuthKey,
):
    async with async_session() as session:
        auth_key_item = await create_key(session, mtpylon_auth_key)

    assert auth_key_item.id is not None
    assert auth_key_item.auth_key_id == mtpylon_auth_key.id
    assert auth_key_item.auth_key == mtpylon_auth_key.value.to_bytes(
        256,
        'big'
    )


@pytest.mark.asyncio
async def test_create_key_exists(
    async_session: sessionmaker,
    mtpylon_auth_key: MtpylonAuthKey,
):
    async with async_session() as session:
        await create_key(session, mtpylon_auth_key)

        with pytest.raises(ValueError):
            await create_key(session, mtpylon_auth_key)
