# -*- coding: utf-8 -*-
from typing import List, Optional

from db import async_session
from users.models import User
from .models import TodoList, Task
from .dal import (
    create_todo_list as dal_create_todo_list,
    get_todo_lists as dal_get_todo_lists,
    get_single_todo_list as dal_get_single_todo_list,
    delete_todo_list as dal_delete_todo_list,
    create_task as dal_create_task,
    get_task_list as dal_get_task_list
)


async def create_todo_list(user: User, title: str) -> TodoList:
    """
    Checks that title isn't empty, and creates todo list

    Raises:
        ValueError - if title is empty
    """
    if len(title) == 0:
        raise ValueError("Title couldn't be empty string")

    async with async_session() as session:
        todo_list = await dal_create_todo_list(session, user, title)

    return todo_list


async def get_todo_lists(user: User) -> List[TodoList]:
    """
    Returns list
    :param user:
    :return:
    """
    async with async_session() as session:
        todo_lists = await dal_get_todo_lists(session, user)

    return todo_lists


async def get_todo_list_for_user(
    user: User,
    todo_list_id: int
) -> Optional[TodoList]:
    """
    Returns
    """
    async with async_session() as session:
        todo_list = await dal_get_single_todo_list(
            session,
            todo_list_id=todo_list_id,
            user=user
        )
    return todo_list


async def delete_todo_list(todo_list: TodoList):
    async with async_session() as session:
        await dal_delete_todo_list(session, todo_list)


async def create_task(todo_list: TodoList, title: str) -> Task:
    async with async_session() as session:
        task = await dal_create_task(session, todo_list, title)
    return task


async def get_tasks_for_todo_list(todo_list: TodoList) -> List[Task]:
    async with async_session() as session:
        task_list = await dal_get_task_list(session, todo_list=todo_list)
    return task_list
