# -*- coding: utf-8 -*-
import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

PG_URL = os.environ.get('PG_URL')

engine = create_async_engine(PG_URL, future=True, echo=True)
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()
