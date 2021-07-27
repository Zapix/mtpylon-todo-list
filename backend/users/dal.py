# -*- coding: utf-8 -*-
from typing import cast, Optional

from sqlalchemy import select
from sqlalchemy.sql import Select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from .models import User


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
) -> Optional[User]:
    stmt: Select = select(User)

    if user_id is not None:
        stmt = stmt.where(User.id == user_id)

    if nickname is not None:
        stmt = stmt.where(User.nickname == nickname)

    result = await session.execute(stmt)
    row = result.one_or_none()
    user: Optional[User] = None

    if row is not None:
        user = cast(User, row[0])

    return user