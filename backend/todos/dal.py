# -*- coding: utf-8 -*-
from typing import List

from sqlalchemy.sql import select
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


async def get_todo_lists(session: AsyncSession, user: User) -> List[TodoList]:
    stmt = select(TodoList).where(TodoList.user == user).order_by(-TodoList.id)
    result = await session.execute(stmt)
    return result.scalars().all()


async def delete_todo_list(
    session: AsyncSession,
    todo_list: TodoList
):
    await session.delete(todo_list)
