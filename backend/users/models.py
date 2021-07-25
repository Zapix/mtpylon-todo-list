# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Sequence, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    nickname = Column(String, unique=True)
    password = Column(String)

    auth_keys = relationship('AuthKey', back_populates='user')

    def __repr__(self):
        return f'<User(id={self.id} nickname={self.nickname})>'


class AuthKey(Base):
    """
    Base class that associates mtpylon auth key with existing `User`
    Stores auth_key_id as unique_key
    """
    __tablename__ = 'auth_keys'

    id = Column(Integer, Sequence('auth_key_id_seq'), primary_key=True)
    auth_key_id = Column(BigInteger, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='auth_keys')

    def __repr__(self):
        return f'<AuthKey(auth_key_id={self.auth_key_id})>'
