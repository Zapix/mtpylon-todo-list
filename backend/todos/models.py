# -*- coding: utf-8 -*-
from typing import List
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from db import Base
from users.models import User


class TodoList(Base):
    __tablename__ = 'todo_lists'

    id: int = Column(Integer, Sequence('todo_list_id_seq'), primary_key=True)
    user_id: int = Column(Integer, ForeignKey('users.id'), nullable=False)
    title: str = Column(String, nullable=False)

    user: User = relationship(User, back_populates='todo_lists')
    tasks: List['Task'] = relationship('Task', back_populates='todo_list')

    def __repr__(self):
        return f'<TodoList(id={self.id} title={self.title})>'


User.todo_lists = relationship(TodoList, back_populates='user')


class Task(Base):
    __tablename__ = 'tasks'

    id: int = Column(Integer, Sequence('task_id_seq'), primary_key=True)
    todo_list_id: int = Column(
        Integer,
        ForeignKey('todo_lists.id'),
        nullable=False
    )
    title: str = Column(String, nullable=False)
    completed: bool = Column(Boolean, default=False, nullable=False)

    todo_list: TodoList = relationship('TodoList', back_populates='tasks')

    def __repr__(self):
        id_, title, completed = self.id, self.title, self.completed
        return f'<Task (id={id_} title={title} completed={completed})>'
