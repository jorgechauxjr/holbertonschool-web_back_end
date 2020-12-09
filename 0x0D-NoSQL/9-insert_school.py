#!/usr/bin/env python3
"""9. Insert a document in Python
"""


def insert_school(mongo_collection, **kwargs):
    """
    function that inserts a new document in a collection based on kwargs
    """

    document_id = mongo_collection.insert(kwargs)
    return document_id