# -*- coding: utf-8 -*-
from dataclasses import dataclass

from .bool import Bool


@dataclass
class Task:
    id: int
    title: str
    completed: Bool

    class Meta:
        name = 'task'
        order = ('id', 'title', 'completed')
