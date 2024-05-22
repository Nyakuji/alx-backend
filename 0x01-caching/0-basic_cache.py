"""Basic dictionary"""

BaseCache = __import__('base_caching').BaseCaching


class BasicCache(BaseCache):
    """ Defines a basic cache system """

    def put(self, key, item):
        """
        Assign item value for the key in
        self.cache_data
        if neither key nor item is None
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to key in self.cache_data.
        Return None if key is None or doesn't exist
        """
        return self.cache_data.get(key, None)
