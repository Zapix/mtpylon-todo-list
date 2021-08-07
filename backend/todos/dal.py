# -*- coding: utf-8 -*-
from typing import List, Optional

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


async def get_single_todo_list(
    session: AsyncSession,
    todo_list_id: Optional[int] = None,
    user: Optional[User] = None,
):
    stmt = select(TodoList)

    if todo_list_id is not None:
        stmt = stmt.where(TodoList.id == todo_list_id)

    if user is not None:
        stmt = stmt.where(TodoList.user == user)

    result = await session.execute(stmt)

    return result.scalar_one_or_none()


async def delete_todo_list(
    session: AsyncSession,
    todo_list: TodoList
):
    await session.delete(todo_list)