# -*- coding: utf-8 -*-
import pytest
from contextlib import ExitStack
from unittest.mock import patch, AsyncMock, MagicMock

from mtpylon.contextvars import auth_key_var  # type: ignore
from mtpylon.exceptions import RpcCallError  # type: ignore

from schema.functions.login_func import login
from schema.constructors import RegisteredUser


@pytest.mark.asyncio
async def test_login_failed():
    request = MagicMock()

    login_user = AsyncMock()
    login_user.side_effect = ValueError('Authentication Failed')

    with patch('schema.functions.login_func.login_user', login_user):
        with pytest.raises(RpcCallError):
            await login(request, 'zapix', 'password123')


@pytest.mark.asyncio
async def test_login_success(mtpylon_auth_key):
    auth_key_var.set(mtpylon_auth_key)

    request = MagicMock()

    login_user = AsyncMock()
    login_user.return_value = MagicMock(id=12, nickname='zapix')

    remember_user = AsyncMock()

    with ExitStack() as patcher:
        patcher.enter_context(
            patch('schema.functions.login_func.login_user', login_user)
        )
        patcher.enter_context(
            patch('schema.functions.login_func.remember_user', remember_user)
        )

        user_data = await login(request, 'zapix', 'password123')

    assert isinstance(user_data, RegisteredUser)
    assert user_data.id == 12
    assert user_data.nickname == 'zapix'

    remember_user.assert_awaited()
