# -*- coding: utf-8 -*-
from typing import List
from dataclasses import dataclass

from .todo_list import TodoList


@dataclass
class TodoListsResult:
    todo_lists: List[TodoList]

    class Meta:
        name = 'todo_lists_result'
        order = ('todo_lists',)
