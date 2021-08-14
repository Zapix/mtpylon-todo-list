# -*- coding: utf-8 -*-
from .register_func import register
from .login_func import login
from .get_me_func import get_me

from .create_todo_list_func import create_todo_list
from .get_todo_lists_func import get_todo_lists
from .get_single_todo_list_func import get_single_todo_list
from .remove_todo_list_func import remove_todo_list
from .create_task_func import create_task
from .get_task_list_func import get_task_list
from .edit_task_title_func import edit_task_title
from .set_as_completed_func import set_as_completed
from .set_as_uncompleted_func import set_as_uncompleted

__all__ = [
    'register',
    'login',
    'get_me',
    'create_todo_list',
    'get_todo_lists',
    'get_single_todo_list',
    'remove_todo_list',
    'create_task',
    'get_task_list',
    'edit_task_title',
    'set_as_completed',
    'set_as_uncompleted',
]
