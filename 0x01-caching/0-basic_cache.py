#!/usr/bin/env python3

"""Basic ditionary
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """class that inherits from BaseCaching"""

    def put(self, key, item):
        """
        assign to dict self.cache_data the item value for key.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key."""
        return self.cache_data.get(key, None)
