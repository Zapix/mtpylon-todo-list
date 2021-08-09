# -*- coding: utf-8 -*-
from mtpylon.types import long
from converter import int64_to_long, long_to_int64


def test_int64_to_long():
    assert int64_to_long(16462053750161430071) == long(-1984690323548121545)


def test_long_to_int64():
    assert long_to_int64(long(-1984690323548121545)) == 16462053750161430071
