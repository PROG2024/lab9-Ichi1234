"""A singleton counter.

   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value

   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""
import logging


class Counter:
    __instance = None
    __share_count = 0

    def __init__(self):
        self.__count = Counter.__share_count

    def __str__(self):
        return f"{self.__count}"

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            logging.info(f"allocate a new Counter")
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @property
    def count(self):
        return self.__count

    def increment(self):
        """add 1 and return the new count"""
        Counter.__share_count += 1
        self.__count += 1
        return Counter.__share_count
