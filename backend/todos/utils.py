# -*- coding: utf-8 -*-
from db import async_session
from users.models import User
from .models import TodoList
from .dal import create_todo_list as dal_create_todo_list


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
