# -*- coding: utf-8 -*-
import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from mtpylon.crypto import AuthKey
from mtpylon.exceptions import RpcCallError
from mtpylon.contextvars import auth_key_var

from schema.utils.decorators import login_required
from users.models import User


@pytest.mark.asyncio
async def test_login_required_rpc_error(
    mtpylon_auth_key: AuthKey
):
    handler = AsyncMock()
    wrapped_handler = login_required(handler)

    request = MagicMock()

    get_user_by_auth_key = AsyncMock(return_value=None)

    auth_key_var.set(mtpylon_auth_key)

    with patch(
        'schema.utils.decorators.get_user_by_auth_key',
        get_user_by_auth_key
    ):
        with pytest.raises(RpcCallError):
            await wrapped_handler(request)

    handler.assert_not_awaited()


@pytest.mark.asyncio
async def test_login_required_success(
    user: User,
    mtpylon_auth_key: AuthKey
):
    handler = AsyncMock()
    wrapped_handler = login_required(handler)

    request = MagicMock()

    get_user_by_auth_key = AsyncMock(return_value=User)

    auth_key_var.set(mtpylon_auth_key)

    with patch(
        'schema.utils.decorators.get_user_by_auth_key',
        get_user_by_auth_key
    ):
        await wrapped_handler(request)

    handler.assert_awaited()
