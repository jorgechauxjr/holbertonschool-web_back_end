#!/usr/bin/env python3
"""5. Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Expects one string argument name password
    and returns a salted, hashed password,
    which is a byte string.
    """
    encoded_psw = bytes(password, 'utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(encoded_psw, salt)
    return hashed
