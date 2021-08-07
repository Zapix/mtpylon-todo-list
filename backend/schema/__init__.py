# -*- coding: utf-8 -*-
from mtpylon import Schema


from .constructors import User, TodoList, TodoListsResult
from .functions import (
    register,
    login,
    get_me,
    create_todo_list,
    get_todo_lists,
)

mtpylon_schema = Schema(
    constructors=[User, TodoList, TodoListsResult],
    functions=[
        register,
        login,
        get_me,
        create_todo_list,
        get_todo_lists,
    ]
)

__all__ = [
    'mtpylon_schema'
]
