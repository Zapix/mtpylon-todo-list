# -*- coding: utf-8 -*-
import pytest
from unittest.mock import patch
from users.utils import encode_password, register_user


def test_encode_password():
    hashed_str = 'e4ecd6fc11898565af24977e992cea0c9c7b7025'
    assert encode_password('hello_world') == hashed_str


@pytest.mark.asyncio
async def test_register_user_empty_nickname():
    with pytest.raises(ValueError):
        await register_user('', 'password')


@pytest.mark.asyncio
async def test_register_user_empty_password():
    with pytest.raises(ValueError):
        await register_user('zapix', '')


@pytest.mark.asyncio
async def test_register_user_exists(async_session, user):
    with patch('users.utils.async_session', async_session):
        with pytest.raises(ValueError):
            await register_user(user.nickname, 'password')


@pytest.mark.asyncio
async def test_register_user_success(async_session):
    with patch('users.utils.async_session', async_session):
        user = await register_user('zap.aibulatov', 'secretpassword1')

    assert user is not None
    assert user.nickname == 'zap.aibulatov'
