# -*- coding: utf-8 -*-
from hashlib import sha1


def encode_password(password: str) -> str:
    """
    Creates sha1 hash to store password. Doesn't use salt coz it's an example
    """
    hash = sha1(password.encode('utf-8'))
    return hash.hexdigest()
