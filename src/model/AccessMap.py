# -*- coding: UTF-8 -*-
from typing import List

from model import Location


class AccessMap(object):
    def __init__(self):
        self.locations: List[Location] = []

    @property
    def locations(self):
        return self.__locations

    @locations.setter
    def locations(self, value):
        self.__locations = value

    @locations.deleter
    def locations(self):
        del self.__locations

    def add_location(self, location):
        self.locations.append(location)

    def delete_location(self, location):
        self.locations.delete(location)

    # TODO Replace these three methods with get_location_by_type()
    def get_obstacles(self):
        return [location for location in self.locations if location.type == LocationType.Obstacle]

    def get_parkings(self):
        return [location for location in self.locations if location.type == LocationType.Parking]

    def get_toilets(self):
        return [location for location in self.locations if location.type == LocationType.Toilet]
