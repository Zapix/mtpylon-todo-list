# -*- coding: utf-8 -*-
from mtpylon import Schema


from .constructors import Bool, User, TodoList, TodoListsResult
from .functions import (
    register,
    login,
    get_me,
    create_todo_list,
    get_todo_lists,
    get_single_todo_list,
    remove_todo_list,
)

mtpylon_schema = Schema(
    constructors=[
        Bool,
        User,
        TodoList,
        TodoListsResult
    ],
    functions=[
        register,
        login,
        get_me,
        create_todo_list,
        get_todo_lists,
        get_single_todo_list,
        remove_todo_list,
    ]
)

__all__ = [
    'mtpylon_schema'
]
