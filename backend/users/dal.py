# -*- coding: utf-8 -*-
from typing import cast, Optional

from sqlalchemy import select
from sqlalchemy.sql import Select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from mtpylon.crypto import AuthKey as MtpylonAuthKey  # type: ignore

from .models import User, AuthKey


async def create_user(
    session: AsyncSession,
    nickname: str,
    password: str
) -> User:
    """
    Creates new user or raises ValueError if couldn't create
    """
    try:
        user = User(nickname=nickname, password=password)
        session.add(user)
        await session.commit()
    except IntegrityError as e:
        raise ValueError(e)
    return user


async def get_user(
    session: AsyncSession,
    user_id: Optional[int] = None,
    nickname: Optional[str] = None,
    auth_key: Optional[MtpylonAuthKey] = None,
) -> Optional[User]:
    stmt: Select = select(User)

    if user_id is not None:
        stmt = stmt.where(User.id == user_id)

    if nickname is not None:
        stmt = stmt.where(User.nickname == nickname)

    if auth_key is not None:
        stmt = stmt.join(AuthKey).where(AuthKey.auth_key_id == auth_key.id)

    result = await session.execute(stmt)
    row = result.one_or_none()
    user: Optional[User] = None

    if row is not None:
        user = cast(User, row[0])

    return user


async def create_auth_key(
        session: AsyncSession,
        user: User,
        auth_key: MtpylonAuthKey
) -> AuthKey:
    """
    Creates auth key for user
    """
    key = AuthKey(
        auth_key_id=auth_key.id,
        user_id=user.id
    )
    session.add(key)
    await session.commit()

    return key
