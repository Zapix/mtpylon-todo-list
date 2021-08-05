# -*- coding: utf-8 -*-
from hashlib import sha1
from typing import Optional

from mtpylon.crypto import AuthKey as MtpylonAuthKey

from db import async_session
from .models import User
from .dal import get_user, create_user, create_auth_key

AUTH_ERROR_MESSAGE = 'Authentication has been failed'


def encode_password(password: str) -> str:
    """
    Creates sha1 hash to store password. Doesn't use salt coz it's an example
    """
    hash = sha1(password.encode('utf-8'))
    return hash.hexdigest()


async def register_user(nickname: str, password: str) -> User:
    """
    Validates nickname, password, checks that user with
    this login does not exist yet

    Raises:
        ValueError - with wrong nickname, password  or user with nickname
                    exists
    Returns:
        User - user object
    """
    if len(nickname) < 5:
        raise ValueError('Nickname is too short. Should be more then 5 chars')

    if len(password) < 5:
        raise ValueError("Password is to short. Should be more then 5 chars")

    async with async_session() as session:
        existing_user = await get_user(session, nickname=nickname)

        if existing_user is not None:
            raise ValueError(f"User with nickname {nickname} exists")

        new_user = await create_user(
            session,
            nickname,
            encode_password(password)
        )

    return new_user


async def login_user(nickname: str, password: str) -> User:
    """
    Checks user with current credentials
    Raises:
        ValueError - if something goes wrong
    """
    async with async_session() as session:
        user = await get_user(session, nickname=nickname)

    if user is None:
        raise ValueError(AUTH_ERROR_MESSAGE)

    hashed_password = encode_password(password)

    if hashed_password != user.password:
        raise ValueError(AUTH_ERROR_MESSAGE)

    return user


async def remember_user(user: User, auth_key: MtpylonAuthKey):
    """
    Creates auth key for user
    """
    async with async_session() as session:
        await create_auth_key(session, user, auth_key)


async def get_user_by_auth_key(auth_key: MtpylonAuthKey) -> Optional[User]:
    """
    Get auth user by auth key
    """
    async with async_session() as session:
        user = await get_user(session, auth_key=auth_key)
    return user
