# -*- coding: utf-8 -*-
import pytest
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
from faker import Faker

from users.models import User
from users.dal import create_user
from todos.models import TodoList
from todos.dal import (
    create_todo_list,
    get_todo_lists,
    get_single_todo_list,
    delete_todo_list,
)


@pytest.mark.asyncio
async def test_create_todo_list(async_session: sessionmaker, user: User):
    async with async_session() as session:
        todo_list = await create_todo_list(session, user, 'mtpylon todo list')

    assert todo_list is not None
    assert todo_list.id is not None
    assert todo_list.title == 'mtpylon todo list'
    assert todo_list.user == user


@pytest.mark.asyncio
async def test_get_todo_lists(
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


@pytest.mark.asyncio
async def test_get_todo_list_by_id(
    async_session: sessionmaker,
    fake: Faker,
    user: User,
):
    async with async_session() as session:
        todo_list = await create_todo_list(session, user, fake.name())

        returned_todo_list = await get_single_todo_list(
            session,
            todo_list_id=todo_list.id
        )

        assert returned_todo_list == todo_list


@pytest.mark.asyncio
async def test_get_todo_list_by_id_and_user(
    async_session: sessionmaker,
    fake: Faker,
    user: User,
):
    async with async_session() as session:
        todo_list = await create_todo_list(session, user, fake.name())

        returned_todo_list = await get_single_todo_list(
            session,
            todo_list_id=todo_list.id,
            user=user
        )

        assert returned_todo_list == todo_list


@pytest.mark.asyncio
async def test_get_todo_list_by_other_user(
    async_session: sessionmaker,
    fake: Faker,
    user: User
):
    async with async_session() as session:
        other_user = await create_user(session, fake.name(), fake.password())
        todo_list = await create_todo_list(session, other_user, fake.name())

        returned_todo_list = await get_single_todo_list(
            session,
            todo_list_id=todo_list.id,
            user=user
        )

        assert returned_todo_list is None


@pytest.mark.asyncio
async def test_delete_todo_list(
        async_session: sessionmaker,
        fake: Faker,
        user: User
):
    async with async_session() as session:
        todo_list = await create_todo_list(session, user, fake.name())
        assert todo_list.id is not None

        await delete_todo_list(session, todo_list)

        stmt = select(TodoList).where(TodoList.id == todo_list.id)
        result = await session.execute(stmt)
        deleted_todo_list = result.scalar_one_or_none()
        assert deleted_todo_list is None
