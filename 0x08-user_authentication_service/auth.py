#!/usr/bin/env python3
"""
Module auth
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """takes in a password string arguments and returns a string.
    The string is a salted hash of the input password,
    hashed with bcrypt.hashpw.
    """
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """take mandatory email and password string arguments and
        return a User object
        -If a user already exist with the passed email, raise a
        ValueError with the message User <user's email> already exists.
        -If not, hash the password with _hash_password, save the user
        to the database using self._db and return the User object
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user
        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """locating the user by email. If it exists, check the password
        with bcrypt.checkpw. If it matches return True. In any other case,
        return False
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                passwhash = _hash_password(password)
                return bcrypt.checkpw(password.encode('utf-8'), passwhash)
        except NoResultFound:
            return False
