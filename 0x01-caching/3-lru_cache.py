#!/usr/bin/env python3
"""This script implements a LRC caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """This class implements the least recently used"""

    def __init__(self):
        """Initialize this class"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item to the cache"""

        if key and item:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(
                    self.keys.index(key)))
            if len(self.keys) > self.MAX_ITEMS:
                old_key = self.keys.pop(0)
                del self.cache_data[old_key]
                print(f"DISCARD: {old_key}")

    def get(self, key):
        """Gets a key from the cache"""
        return self.cache_data.get(key, None)
