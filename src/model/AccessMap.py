# -*- coding: UTF-8 -*-
from Model import Location

class AccessMap(object):
	def get_location(self):
		"""@ReturnType Model.Location*"""
		pass

	def set_location(self, *location):
		"""@ParamType location Model.Location*
		@ReturnType void"""
		pass

	def get_obstacles(self):
		"""@ReturnType Obstacle*"""
		pass

	def get_toilets(self):
		"""@ReturnType Toilets*"""
		pass

	def get_parkings(self):
		"""@ReturnType Parking*"""
		pass

	def add_location(self, location):
		"""@ParamType location Model.Location
		@ReturnType void"""
		pass

	def delete_location(self, location):
		"""@ParamType location Model.Location
		@ReturnType void"""
		pass

	def get_access_map(self):
		"""@ReturnType Model.Location*"""
		pass

	def __init__(self):
		self.__location = None
		"""@AttributeType Model.Location*"""

