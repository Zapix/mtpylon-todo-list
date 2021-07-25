# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from db import Base
from users.models import User


class TodoList(Base):
    __tablename__ = 'todo_lists'

    id = Column(Integer, Sequence('todo_list_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)

    user = relationship(User, back_populates='todo_lists')
    tasks = relationship('Task', back_populates='todo_list')

    def __repr__(self):
        return f'<TodoList(id={self.id} title={self.title})>'


User.todo_lists = relationship(TodoList, back_populates='user')


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, Sequence('task_id_seq'), primary_key=True)
    todo_list_id = Column(Integer, ForeignKey('todo_lists.id'))
    title = Column(String)
    completed = Column(Boolean, default=False)

    todo_list = relationship('TodoList', back_populates='tasks')

    def __repr__(self):
        return f'<Task (id={self.id} title={self.title} completed={self.completed})>'
