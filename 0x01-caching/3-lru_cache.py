#!/usr/bin/env python3

"""LRU Caching"""

from lib2to3.pgen2.token import BACKQUOTE
from typing import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    class LRUCache inherits from BaseCaching and a caching system
    """

    def __init__(self):
        """Initialize method"""
        super().__init__()
        self.lru_order = OrderedDict()

    def put(self, key, item):
        """
        assign to dict self.cache_data the item value for key.
        """
        if key and item:
            self.lru_order[key] = item
            self.lru_order.move_to_end(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discarded = next(iter(self.lru_order))
            del self.cache_data[item_discarded]
            print("DISCARD:", item_discarded)

        if len(self.lru_order) > BaseCaching.MAX_ITEMS:
            self.lru_order.popitem(last=False)

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        """
        if key in self.cache_data:
            self.lru_order.move_to_end(key)
            return self.cache_data[key]
        return None
