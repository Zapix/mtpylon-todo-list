# -*- coding: utf-8 -*-
from schema.utils.converter import from_bool, to_bool
from schema.constructors import BoolFalse, BoolTrue


def test_from_bool_true():
    assert from_bool(True) == BoolTrue()


def test_from_bool_false():
    assert from_bool(False) == BoolFalse()


def test_to_bool_true():
    assert to_bool(BoolTrue())


def test_to_bool_false():
    assert not to_bool(BoolFalse())
