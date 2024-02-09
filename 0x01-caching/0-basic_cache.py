#!/usr/bin/python3
""" BaseCache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents a basic caching system that inherits from BaseCaching.
    """

    def put(self, key, item):
        """Add an item to the cache.

        Args:
            key: Key to identify the item.
            item: Item to be stored in the cache.

        Notes:
            If key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key from the cache.

        Args:
            key: Key to identify the item.

        Returns:
            The value associated with the given key in self.cache_data.
            If key is None or if the key doesn’t exist in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
        
