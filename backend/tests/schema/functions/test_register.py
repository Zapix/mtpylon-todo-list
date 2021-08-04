# -*- coding: utf-8 -*-
import pytest
from contextlib import ExitStack
from unittest.mock import patch, MagicMock, AsyncMock

from mtpylon.contextvars import auth_key_var
from mtpylon.exceptions import RpcCallError

from schema.functions.register_func import register
from schema.constructors import RegisteredUser


@pytest.mark.asyncio
async def test_register_success(mtpylon_auth_key):
    auth_key_var.set(mtpylon_auth_key)

    request = MagicMock()

    mocked_user = MagicMock(
        id=12,
        nickname='johndoe'
    )
    register_user = AsyncMock()
    register_user.return_value = mocked_user

    remember_user = AsyncMock()

    with ExitStack() as patcher:
        patcher.enter_context(
            patch(
                'schema.functions.register_func.register_user',
                register_user
            )
        )
        patcher.enter_context(
            patch(
                'schema.functions.register_func.remember_user',
                remember_user
            )
        )

        result = await register(request, 'johndoe', '12345')

    register_user.assert_awaited()
    assert isinstance(result, RegisteredUser)

    remember_user.assert_awaited()


@pytest.mark.asyncio
async def test_register_rpc_call_error():
    request = MagicMock()

    register_user = AsyncMock()
    register_user.side_effect = ValueError('Value Error')

    with patch('schema.functions.register_func.register_user', register_user):
        with pytest.raises(RpcCallError):
            await register(request, 'johndoe', '123123')
