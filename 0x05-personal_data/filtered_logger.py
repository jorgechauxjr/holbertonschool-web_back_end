#!/usr/bin/env python3
from typing import List
import re
"""0. Regex-ing"""


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Returns the log message obfuscated
    Arguments:
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating all
    fields in the log line (message)

    re.sub(pattern, repl, string)
    """

    for info in fields:
        pattern = info + "=.+?(?=abc)*\\" + ";"
        message = re.sub(pattern, info + "=" + redaction + separator, message)
    return message
