# -*- coding: utf-8 -*-
import os
import logging

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

logger = logging.getLogger(__name__)

PG_URL = os.getenv('PG_URL', 'sqlite+aiosqlite://')

logger.debug(f'PG_URL: {PG_URL}')

engine = create_async_engine(PG_URL, future=True, echo=True)
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()
