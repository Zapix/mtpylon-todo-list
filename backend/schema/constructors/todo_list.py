# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class TodoList:
    id: int
    title: str

    class Meta:
        name = 'todo_list'
        order = ('id', 'title')
