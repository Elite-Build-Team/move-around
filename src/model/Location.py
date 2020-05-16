# -*- coding: UTF-8 -*-
from typing import Tuple

from model import LocationType


class Location(object):
    def __init__(self):
        self.coordinates: Tuple[int, int] = (-1, -1)
        self.type: LocationType = None

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, value):
        self.__coordinates = value

    @coordinates.deleter
    def coordinates(self):
        del self.__coordinates

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @type.deleter
    def type(self):
        del self.__type
