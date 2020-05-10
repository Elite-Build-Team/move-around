# -*- coding: UTF-8 -*-
import Location
from typing import List


class AccessMap(object):
    def __init__(self):
        self.__locations: List[Location] = None

    @property
    def __locations(self):
        return

    @__locations.setter
    def __locations(self, value):
        pass

    @__locations.deleter
    def __locations(self):
        pass
