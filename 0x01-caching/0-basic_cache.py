#!/usr/bin/env python3
"""This script implements a caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Implements a caching system to add and get item
       from a caching system
    """
    def put(self, key, item):
        """Add an item to the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item from the cache"""
        if key:
            return self.cache_data.get(key, None)
