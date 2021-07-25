# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from db import Base
from users.models import User


class TodoList(Base):
    __tablename__ = 'todo_lists'

    id = Column(Integer, Sequence('todo_list_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=False)

    user = relationship(User, back_populates='todo_lists')
    tasks = relationship('Task', back_populates='todo_list')

    def __repr__(self):
        return f'<TodoList(id={self.id} title={self.title})>'


User.todo_lists = relationship(TodoList, back_populates='user')


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, Sequence('task_id_seq'), primary_key=True)
    todo_list_id = Column(Integer, ForeignKey('todo_lists.id'), nullable=False)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False, nullable=False)

    todo_list = relationship('TodoList', back_populates='tasks')

    def __repr__(self):
        id_, title, completed = self.id, self.title, self.completed
        return f'<Task (id={id_} title={title} completed={completed})>'
