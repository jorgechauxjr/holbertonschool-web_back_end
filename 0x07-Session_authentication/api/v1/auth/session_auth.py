#!/usr/bin/env python3
"""first step for creating a new authentication mechanism
"""
import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """that inherits from Auth
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a Session ID for a user_id
        """
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id
