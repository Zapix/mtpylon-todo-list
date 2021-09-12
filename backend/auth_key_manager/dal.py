# -*- coding: utf-8 -*-
from typing import Optional

from sqlalchemy import select
from sqlalchemy.sql import Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from mtpylon.crypto import AuthKey as MtpylonAuthKey

from converter import int64_to_long, int2048_to_bytes
from .models import AuthKeyItem


async def create_key(
    session: AsyncSession,
    auth_key: MtpylonAuthKey,
) -> AuthKeyItem:
    try:
        auth_key_item = AuthKeyItem(
            auth_key_id=int64_to_long(auth_key.id),
            auth_key=int2048_to_bytes(auth_key.value)
        )
        session.add(auth_key_item)
        await session.commit()
    except IntegrityError as e:
        raise ValueError(str(e))

    return auth_key_item


async def get_key(
    session: AsyncSession,
    auth_key_id: int
) -> Optional[AuthKeyItem]:
    """
    Checks has we got auth key or not
    """
    stmt: Select = select(AuthKeyItem)
    stmt = stmt.where(AuthKeyItem.auth_key_id == auth_key_id)

    result = await session.execute(stmt)
    return result.scalar_one_or_none()
