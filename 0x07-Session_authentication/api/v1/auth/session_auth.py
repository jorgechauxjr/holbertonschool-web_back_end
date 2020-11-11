#!/usr/bin/env python3
"""first step for creating a new authentication mechanism
"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """that inherits from Auth
    """