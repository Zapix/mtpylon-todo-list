# -*- coding: utf-8 -*-
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
