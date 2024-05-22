#!/usr/bin/env python3
""" Basic dictionary """
Basecache = __import__('base_caching').BaseCaching


class BasicCache(Basecache):
    """ BasicCache class """

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

    def print_cache(self):
        """ Print the cache data """
        for key, value in self.cache_data.items():
            print(f"{key}: {value}")
