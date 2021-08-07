# -*- coding: utf-8 -*-
from mtpylon import Schema


from .constructors import User, TodoList
from .functions import register, login, get_me, create_todo_list

mtpylon_schema = Schema(
    constructors=[User, TodoList],
    functions=[
        register,
        login,
        get_me,
        create_todo_list,
    ]
)

__all__ = [
    'mtpylon_schema'
]
