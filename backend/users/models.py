# -*- coding: utf-8 -*-
from typing import List

from sqlalchemy import (
    Column,
    Integer,
    Sequence,
    String,
    BigInteger,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from db import Base


class User(Base):
    __tablename__ = 'users'

    id: int = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    nickname: str = Column(String, unique=True, nullable=False)
    password: str = Column(String, nullable=False)

    auth_keys: List['AuthKey'] = relationship(
        'AuthKey',
        back_populates='user'
    )

    def __repr__(self):
        return f'<User(id={self.id} nickname={self.nickname})>'


class AuthKey(Base):
    """
    Base class that associates mtpylon auth key with existing `User`
    Stores auth_key_id as unique_key
    """
    __tablename__ = 'auth_keys'

    id: int = Column(Integer, Sequence('auth_key_id_seq'), primary_key=True)
    auth_key_id: int = Column(BigInteger, unique=True, nullable=False)
    user_id: int = Column(Integer, ForeignKey('users.id'), nullable=False)

    user: User = relationship('User', back_populates='auth_keys')

    def __repr__(self):
        return f'<AuthKey(auth_key_id={self.auth_key_id})>'
