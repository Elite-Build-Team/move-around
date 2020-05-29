# -*- coding: UTF-8 -*-
from enum import Enum

from model import Location
from typing import List

from model.Location import LocationType


class AccessMap(object):
	def get_locations(self) -> List[Location]:
		return self.__locations

	def set_locations(self, locations : List[Location]):
		self.__locations = locations

	def get_obstacles(self) -> List[Location]:
		return [location for location in self.__locations if location.type == LocationType.Obstacle] 

	def get_toilets(self) -> List[Location]:
		return [location for location in self.__locations if location.type == LocationType.Toilet]

	def get_parkings(self) -> List[Location]:
		return [location for location in self.__locations if location.type == LocationType.Parking]

	def add_location(self, location : Location):
		self.__locations.append(location)

	def delete_location(self, location : Location):
		self.__locations.remove(location)

	def get_access_map(self) -> List[Location]:
		return self.__locations

	def __init__(self):
		self.__locations = List[Location] = []