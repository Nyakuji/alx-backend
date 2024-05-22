#!/usr/bin/env python3
"""LIFO Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Defines a LIFO cache system """

    def __init__(self):
        """ Initializes the cache """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Assign item value for the key in
        self.cache_data
        if neither key nor item is None
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last = self.keys.pop()
                print("DISCARD: {}".format(last))
                del self.cache_data[last]
            self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to key in self.cache_data.
        Return None if key is None or doesn't exist
        """
        return self.cache_data.get(key, None)
