# -*- coding: UTF-8 -*-
import LocationType
from typing import Tuple


class Location(object):
    def __init__(self):
        self.__coordinates: Tuple[int, int] = None
        self.__type: LocationType = None

    @property
    def __coordinates(self):
        return

    @__coordinates.setter
    def __coordinates(self, value):
        pass

    @__coordinates.deleter
    def __coordinates(self):
        pass

    @property
    def __type(self):
        return

    @__type.setter
    def __type(self, value):
        pass

    @__type.deleter
    def __type(self):
        pass
