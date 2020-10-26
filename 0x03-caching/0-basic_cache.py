#!/usr/bin/python3

"""
Module for BasicCache class
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
     inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
