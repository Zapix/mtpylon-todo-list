# -*- coding: utf-8 -*-
import pytest
from unittest.mock import patch
from users.utils import encode_password, register_user, login_user


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


@pytest.mark.asyncio
async def test_login_user_no_user(async_session):
    with patch('users.utils.async_session', async_session):
        with pytest.raises(ValueError):
            await login_user('unknown_user', 'random_password')


@pytest.mark.asyncio
async def test_login_user_wrong_password(async_session, user):
    with patch('users.utils.async_session', async_session):
        with pytest.raises(ValueError):
            await login_user(user.nickname, 'random_password')


@pytest.mark.asyncio
async def test_login_user_success(async_session, user):
    with patch('users.utils.async_session', async_session):
        logged_in_user = await login_user(user.nickname, 'hello_world')

    assert logged_in_user.id == user.id
