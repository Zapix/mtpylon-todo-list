# -*- coding: utf-8 -*-
import pytest

from schema.utils.converter import (
    from_bool,
    to_bool,
    from_task_model
)
from schema.constructors import BoolFalse, BoolTrue, Task
from todos.models import Task as TaskModel


def test_from_bool_true():
    assert from_bool(True) == BoolTrue()


def test_from_bool_false():
    assert from_bool(False) == BoolFalse()


def test_to_bool_true():
    assert to_bool(BoolTrue())


def test_to_bool_false():
    assert not to_bool(BoolFalse())


@pytest.mark.asyncio
async def test_from_task(task: TaskModel):
    data = from_task_model(task)

    assert isinstance(data, Task)
    assert data.id == task.id
    assert data.title == task.title
    assert data.completed == from_bool(task.completed)
