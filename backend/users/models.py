# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    nickname = Column(String, unique=True)
    password = Column(String)

    def __repr__(self):
        return f'<User(id={self.id} nickname={self.nickname})>'
