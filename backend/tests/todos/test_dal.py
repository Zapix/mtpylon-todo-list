# -*- coding: utf-8 -*-
import pytest
from sqlalchemy.orm import sessionmaker
from faker import Faker

from users.models import User
from todos.models import TodoList
from todos.dal import create_todo_list, get_todo_lists


@pytest.mark.asyncio
async def test_create_todo_list(async_session: sessionmaker, user: User):
    async with async_session() as session:
        todo_list = await create_todo_list(session, user, 'mtpylon todo list')

    assert todo_list is not None
    assert todo_list.id is not None
    assert todo_list.title == 'mtpylon todo list'
    assert todo_list.user == user


@pytest.mark.asyncio
async def test_get_todo_list(
    async_session: sessionmaker,
    fake: Faker,
    user: User
):
    async with async_session() as session:
        for _ in range(15):
            await create_todo_list(session, user, fake.name())

        todo_lists = await get_todo_lists(session, user)

    assert len(todo_lists) == 15
    assert isinstance(todo_lists[0], TodoList)
