# -*- coding: utf-8 -*-

from sqlalchemy.ext.asyncio import AsyncSession

from users.models import User
from .models import TodoList


async def create_todo_list(
    session: AsyncSession,
    user: User,
    title: str
) -> TodoList:
    todo_list = TodoList(
        user=user,
        title=title
    )
    session.add(todo_list)
    await session.commit()

    return todo_list
