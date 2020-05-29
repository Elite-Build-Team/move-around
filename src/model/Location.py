# -*- coding: UTF-8 -*-
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
		self.__coordinates: Tuple[int, int] = None
		self.__type = None

