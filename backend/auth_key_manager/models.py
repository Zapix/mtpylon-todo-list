# -*- coding: utf-8 -*-
from sqlalchemy import (
    Column,
    BigInteger,
    LargeBinary,
    Integer,
    Sequence
)

from db import Base


class AuthKeyItem(Base):
    """
    Declare auth key item to store auth keys for AuthKey Manager.
    """

    __tablename__ = 'auth_key_items'

    id: int = Column(
        Integer,
        Sequence('auth_key_item_id_seq'),
        primary_key=True
    )
    auth_key_id: int = Column(BigInteger, unique=True, nullable=False)
    auth_key: bytes = Column(LargeBinary(length=2048), nullable=False)

    def __repr__(self):
        return f'<AuthKeyItem(auth_key_id={self.auth_key_id}>'
