# -*- coding: utf-8 -*-
from users.utils import encode_password


def test_encode_password():
    hashed_str = 'e4ecd6fc11898565af24977e992cea0c9c7b7025'
    assert encode_password('hello_world') == hashed_str
