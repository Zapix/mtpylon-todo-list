# -*- coding: utf-8 -*-
import pytest
from unittest.mock import patch, MagicMock, AsyncMock

from mtpylon.exceptions import RpcCallError  # type: ignore

from schema.functions.register_func import register
from schema.constructors import RegisteredUser


@pytest.mark.asyncio
async def test_register_success():
    request = MagicMock()

    mocked_user = MagicMock(
        id=12,
        nickname='johndoe'
    )
    register_user = AsyncMock()
    register_user.return_value = mocked_user

    with patch('schema.functions.register_func.register_user', register_user):
        result = await register(request, 'johndoe', '12345')

    register_user.assert_awaited()
    assert isinstance(result, RegisteredUser)


@pytest.mark.asyncio
async def test_register_rpc_call_error():
    request = MagicMock()

    register_user = AsyncMock()
    register_user.side_effect = ValueError('Value Error')

    with patch('schema.functions.register_func.register_user', register_user):
        with pytest.raises(RpcCallError):
            await register(request, 'johndoe', '123123')
