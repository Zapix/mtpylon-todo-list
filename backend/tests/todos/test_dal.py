# -*- coding: utf-8 -*-
import pytest
from typing import cast
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
from faker import Faker

from users.models import User
from users.dal import create_user
from todos.models import TodoList, Task
from todos.dal import (
    create_todo_list,
    get_todo_lists,
    get_single_todo_list,
    delete_todo_list,
    create_task,
    get_task_list,
    get_task,
    update_task,
    delete_task
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


@pytest.mark.asyncio
async def test_create_task_dal(
    async_session: sessionmaker,
    todo_list: TodoList
):
    async with async_session() as session:
        task = await create_task(session, todo_list, 'first task')
    assert task.id is not None
    assert task.todo_list == todo_list
    assert task.title == 'first task'
    assert not task.completed


@pytest.mark.asyncio
async def test_get_task_list(
    async_session: sessionmaker,
    fake: Faker,
    todo_list: TodoList
):
    async with async_session() as session:
        for _ in range(14):
            task = Task(
                todo_list=todo_list,
                title=fake.name(),
                completed=False
            )
            session.add(task)
        await session.commit()

        task_list = await get_task_list(session, todo_list)

    assert len(task_list) == 14
    assert isinstance(task_list[0], Task)


@pytest.mark.asyncio
async def test_task_by_id(async_session: sessionmaker, task: Task):
    async with async_session() as session:
        returned_task = await get_task(session, task_id=task.id)

    assert returned_task is not None
    assert returned_task.id == task.id


@pytest.mark.asyncio
async def test_get_task_by_id_none(async_session: sessionmaker):
    async with async_session() as session:
        returned_task = await get_task(session, task_id=-1)

    assert returned_task is None


@pytest.mark.asyncio
async def test_get_task_by_todo_list(
    async_session: sessionmaker,
    todo_list: TodoList,
    task: Task,
):
    async with async_session() as session:
        returned_task = await get_task(
            session,
            todo_list=todo_list,
            task_id=task.id
        )

    assert returned_task is not None
    assert returned_task.id == task.id


@pytest.mark.asyncio
async def test_get_task_by_todo_list_none(
    async_session: sessionmaker,
    user: User,
    task: Task
):
    async with async_session() as session:
        new_todo_list = await create_todo_list(
            session,
            title='another',
            user=user,
        )

        returned_task = await get_task(
            session,
            todo_list=new_todo_list,
            task_id=task.id
        )

    assert returned_task is None


@pytest.mark.asyncio
async def test_get_task_by_user(
    async_session: sessionmaker,
    user: User,
    task: Task
):
    async with async_session() as session:
        returned_task = await get_task(session, user=user, task_id=task.id)

    assert returned_task is not None
    assert returned_task.id == task.id


@pytest.mark.asyncio
async def test_get_task_by_user_none(
    async_session: sessionmaker,
    task: Task
):
    async with async_session() as session:
        new_user = await create_user(session, 'new_user', 'pass')
        returned_task = await get_task(
            session,
            user=new_user,
            task_id=task.id
        )

    assert returned_task is None


@pytest.mark.asyncio
async def test_update_task_mark_completed(
    async_session: sessionmaker,
    task: Task
):
    async with async_session() as session:
        updated_task = await update_task(session, task, completed=True)

    async with async_session() as session:
        retrieved_task = await get_task(session, task_id=task.id)
        retrieved_task = cast(Task, retrieved_task)

    assert updated_task.completed
    assert retrieved_task.completed


@pytest.mark.asyncio
async def test_udpate_task_change_title(
    async_session: sessionmaker,
    task: Task
):
    async with async_session() as session:
        updated_task = await update_task(session, task, title='changed')

    async with async_session() as session:
        retrieved_task = await get_task(session, task_id=task.id)
        retrieved_task = cast(Task, retrieved_task)

    assert updated_task.title == 'changed'
    assert retrieved_task.title == 'changed'


@pytest.mark.asyncio
async def test_delete_task(async_session: sessionmaker, task: Task):
    task_id = task.id
    async with async_session() as session:
        await delete_task(session, task)

    async with async_session() as session:
        returned_task = await get_task(session, task_id=task_id)

    assert returned_task is None
