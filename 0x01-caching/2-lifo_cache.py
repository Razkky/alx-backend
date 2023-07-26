#!/usr/bin/env python3
"""This scripts implements a LIFO caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Implements the lifo caching policy"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()

    def put(self, key, item):
        """Add an item to the caching list"""

        if len(self.cache_data) >= self.MAX_ITEMS \
           and key not in self.cache_data:
            old_item = self.cache_data.popitem()
            print(f"DISCARD: {old_item[0]}")

        if key and item:
            if key in self.cache_data:
                del self.cache_data[key]
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item from a caching system"""
        return self.cache_data.get(key, None)
