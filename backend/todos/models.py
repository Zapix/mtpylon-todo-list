# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship

from db import Base
from users.models import User


class TodoList(Base):
    __tablename__ = 'todo_lists'

    id = Column(Integer, Sequence('todo_list_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)

    user = relationship(User, back_populates='todo_lists')

    def __repr__(self):
        return f'<TodoList(id={self.id} title={self.title})>'


User.todo_lists = relationship(TodoList, back_populates='user')
