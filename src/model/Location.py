# -*- coding: UTF-8 -*-
class Location(object):
	def get_coordinates(self):
		"""@ReturnType (long,lat)"""
		pass

	def set_coordinates(self, aCoordinates):
		"""@ParamType aCoordinates (long,lat)
		@ReturnType void"""
		pass

	def get_type(self):
		"""@ReturnType enum(Toilet,Obstacle, Parking, AFP, Public Service)"""
		pass

	def set_type(self, aType):
		"""@ParamType aType enum(Toilet,Obstacle, Parking, AFP, Public Service)
		@ReturnType void"""
		pass

	def __init__(self):
		self.__coordinates = None
		"""@AttributeType (long,lat)"""
		self.__type = None
		"""@AttributeType enum(Toilet,Obstacle, Parking, AFP, Public Service)"""

