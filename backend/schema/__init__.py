# -*- coding: utf-8 -*-
from mtpylon import Schema


from .constructors import (
    Bool,
    User,
    TodoList,
    TodoListsResult,
    Task,
    TaskList
)
from .functions import (
    register,
    login,
    get_me,
    create_todo_list,
    get_todo_lists,
    get_single_todo_list,
    remove_todo_list,
    create_task,
    get_task_list,
    edit_task_title,
    set_as_completed,
    set_as_uncompleted,
    remove_task,
)

mtpylon_schema = Schema(
    constructors=[
        Bool,
        User,
        TodoList,
        TodoListsResult,
        Task,
        TaskList
    ],
    functions=[
        register,
        login,
        get_me,
        create_todo_list,
        get_todo_lists,
        get_single_todo_list,
        remove_todo_list,
        create_task,
        get_task_list,
        edit_task_title,
        set_as_completed,
        set_as_uncompleted,
        remove_task,
    ]
)

__all__ = [
    'mtpylon_schema'
]
