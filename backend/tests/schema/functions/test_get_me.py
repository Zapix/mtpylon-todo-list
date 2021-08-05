# -*- coding: utf-8 -*-
import pytest
from unittest.mock import patch, AsyncMock, MagicMock

from mtpylon.contextvars import auth_key_var

from schema.constructors import AnonymousUser, RegisteredUser
from schema.functions.get_me_func import get_me


@pytest.mark.asyncio
async def test_get_anonymous_user(mtpylon_auth_key):
    request = MagicMock()
    auth_key_var.set(mtpylon_auth_key)
    get_user_auth_key = AsyncMock(return_value=None)

    with patch(
        'schema.functions.get_me_func.get_user_by_auth_key',
        get_user_auth_key
    ):
        returned_user = await get_me(request)

    assert isinstance(returned_user, AnonymousUser)
    get_user_auth_key.assert_awaited()


@pytest.mark.asyncio
async def test_get_registered_user(user, mtpylon_auth_key):
    request = MagicMock()
    auth_key_var.set(mtpylon_auth_key)
    get_user_auth_key = AsyncMock(return_value=user)

    with patch(
        'schema.functions.get_me_func.get_user_by_auth_key',
        get_user_auth_key
    ):
        returned_user = await get_me(request)

    assert isinstance(returned_user, RegisteredUser)
    assert returned_user.id == user.id
    assert returned_user.nickname == user.nickname

    get_user_auth_key.assert_awaited()
