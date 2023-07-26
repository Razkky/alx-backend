#!/usr/bin/env python3
"""This script implements a caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """This class implements a caching system"""

    def __init__(self):
        """Initialize this class"""

        super().__init__()

    def put(self, key, item):
        """Add an item to the cache"""
        if len(self.cache_data) >= self.MAX_ITEMS \
           and key not in self.cache_data:
            old = next(iter(self.cache_data))
            self.cache_data.pop(old)
            print(f"DISCARD: {old}")
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item from a cache"""
        return self.cache_data.get(key, None)
