# -*- coding: utf-8 -*-
import pytest

from todos.dal import create_todo_list


@pytest.mark.asyncio
async def test_create_todo_list(async_session, user):
    async with async_session() as session:
        todo_list = await create_todo_list(session, user, 'mtpylon todo list')

    assert todo_list is not None
    assert todo_list.id is not None
    assert todo_list.title == 'mtpylon todo list'
    assert todo_list.user == user
