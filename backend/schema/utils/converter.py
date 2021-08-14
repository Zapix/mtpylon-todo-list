# -*- coding: utf-8 -*-
from ..constructors.bool import Bool, BoolTrue, BoolFalse
from ..constructors.task import Task
from todos.models import Task as TaskModel


def from_bool(value: bool) -> Bool:
    if value:
        return BoolTrue()

    return BoolFalse()


def to_bool(value: Bool) -> bool:
    return value == BoolTrue()


def from_task_model(value: TaskModel) -> Task:
    return Task(
        id=value.id,
        title=value.title,
        completed=from_bool(value.completed)
    )
