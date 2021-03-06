# -*- coding: utf-8 -*-
import pytest
from faker import Faker

from mtpylon.crypto import AuthKey
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from db import Base
from users.models import User
from todos.models import TodoList, Task


@pytest.fixture
def fake():
    return Faker()


@pytest.fixture
async def db_engine():
    engine = create_async_engine('sqlite+aiosqlite://')
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    return engine


@pytest.fixture
async def async_session(db_engine) -> sessionmaker:
    return sessionmaker(db_engine, expire_on_commit=False, class_=AsyncSession)


@pytest.fixture
async def user(faker: Faker, async_session: sessionmaker) -> User:
    async with async_session() as session:
        user = User(
            nickname=faker.name(),
            password='e4ecd6fc11898565af24977e992cea0c9c7b7025'
        )
        session.add(user)
        await session.commit()
    return user


@pytest.fixture
async def todo_list(
    faker: Faker,
    async_session: sessionmaker,
    user: User
) -> TodoList:
    async with async_session() as session:
        todo_list = TodoList(title='project', user=user)
        session.add(todo_list)
        await session.commit()
    return todo_list


@pytest.fixture
async def task(async_session: sessionmaker, fake: Faker, todo_list):
    async with async_session() as session:
        task = Task(
            title=fake.name(),
            todo_list=todo_list
        )
        session.add(task)
        await session.commit()

    return task


@pytest.fixture
def mtpylon_auth_key() -> AuthKey:
    auth_key_value = 0x4fa4120d3646e1cadc7e21fcc9c46111ff8467665908a56b18bd38bee60ee1cccc2eff69dda5e638be2b06e813e6d9832142a054d22f405d9d416f79168140d373b048f55924b836ec5be2ab92e29624edf67bd5d763f8a15c3aed587e7ac70f8fe0d78de45c4b9ea5b81a1e0a098eb064dc9609fa37ca33f703b48461aed343aabc1498dd4d1cbbf3ca4c56cc8c7dc315e251e28312ed258c74326729118251f9153f7ac9d52bd47fdf7072963f6330f06bb72e2cc744af91df3302800e80c23c25a402b97bfc5292589b1c688bd1fde0e9997d9996a32ebd39ba258137b123fa762fd07548c44fd1b9321778f6ec3464ae39402c0445bd02fa8223b30cdfc8  # noqa
    return AuthKey(value=auth_key_value)


@pytest.fixture
def mtpylon_auth_key_big_id() -> AuthKey:
    auth_key_value = 256722258174281487452565621530647706696277211511691059347769905707601842490325326109830604703636805717588572291374043299291491020317149162794208987468325459307395592200545636247491930615939634497008543116418846167263393796430225698400407096676816773518530976594176580185853449907084601858481876054375166386726196881698944607357750837300270175188569421716187664624024891269034164777039068847132016086526535426937114806491117176034836717344232967535418111820726900420546248348564082345504676227587208806069165564680975772140576681586147268222484741955150890745536631713050602209849501122001211284945043774677224942445  # noqa
    return AuthKey(value=auth_key_value)
