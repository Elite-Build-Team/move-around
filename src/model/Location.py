# -*- coding: UTF-8 -*-
from typing import Tuple
from enum import Enum


class LocationType(Enum):
	Obstacle = 1,
	Toilet = 2,
	Parking = 3


class Location(object):
	def get_coordinates(self) -> Tuple[int, int]:
		return self.__coordinates

	def set_coordinates(self, coordinates: Tuple[int, int]):
		self.__coordinates = coordinates

	def get_type(self):
		return self.__type

	def set_type(self, type):
		self.__type = type

	def __init__(self):
		self.__coordinates: Tuple[int, int] = ()
		self.__type = None


