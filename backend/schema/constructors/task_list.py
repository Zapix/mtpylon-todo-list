# -*- coding: utf-8 -*-
from typing import List
from dataclasses import dataclass

from .task import Task


@dataclass
class TaskList:

    tasks: List[Task]

    class Meta:
        name = 'task_list'
        order = ('tasks',)
