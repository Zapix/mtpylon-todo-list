# -*- coding: utf-8 -*-
from typing import Union

from mtpylon.crypto.exceptions import AuthKeyDoesNotExist
from mtpylon.crypto import AuthKey
from mtpylon.crypto.auth_key_manager import AuthKeyManagerProtocol

from db import async_session
from converter import bytes_to_int2048
from .dal import create_key, get_key, delete_key


class AuthKeyDbManager(AuthKeyManagerProtocol):

    async def set_key(self, value: Union[AuthKey, int]):
        if isinstance(value, int):
            auth_key = AuthKey(value)
        else:
            auth_key = value

        async with async_session() as session:
            await create_key(session, auth_key)

    async def has_key(self, value: Union[AuthKey, int]) -> bool:
        key_id = value.id if isinstance(value, AuthKey) else value

        async with async_session() as session:
            result = await get_key(session, key_id)

        return result is not None

    async def get_key(self, value: int) -> AuthKey:
        async with async_session() as session:
            result = await get_key(session, value)

        if result is None:
            raise AuthKeyDoesNotExist()

        return AuthKey(value=bytes_to_int2048(result.auth_key))

    async def del_key(self, value: Union[AuthKey, int]):
        if isinstance(value, int):
            try:
                key = await self.get_key(value)
            except AuthKeyDoesNotExist:
                return
        else:
            key = value

        async with async_session() as session:
            await delete_key(session, key)
