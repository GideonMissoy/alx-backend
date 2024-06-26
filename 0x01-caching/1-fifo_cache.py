#!/usr/bin/env python3

"""FIFO Caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    class FIFOCache that inherits from BaseCaching and a caching system
    """

    def __init__(self):
        """Inititialize method"""
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """
        assign to dict self.cache_data the item value for key.
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_discarded = self.key_indexes.pop(0)
                del self.cache_data[item_discarded]
                print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """
        return the value self.cache_data linked to key.
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
