#!/usr/bin/env python3
"""FIFO caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Represents a caching mechanism with FIFO evictio
    n when the limit is reached.
    """
    def __init__(self):
        """Initialize the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache. Evict the oldest
          item if the cache limit is exceeded.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieve an item by key. Return None if the
          key is not found.
        """
        return self.cache_data.get(key, None)
