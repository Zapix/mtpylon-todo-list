# -*- coding: utf-8 -*-
import pytest
from unittest.mock import patch, AsyncMock, MagicMock

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
async def test_login_success():
    request = MagicMock()

    login_user = AsyncMock()
    login_user.return_value = MagicMock(id=12, nickname='zapix')

    with patch('schema.functions.login_func.login_user', login_user):
        user_data = await login(request, 'zapix', 'password123')

    assert isinstance(user_data, RegisteredUser)
    assert user_data.id == 12
    assert user_data.nickname == 'zapix'
