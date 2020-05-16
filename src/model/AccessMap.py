# -*- coding: UTF-8 -*-
import Location

class AccessMap(object):
	def get_location(self):
		"""@ReturnType Location*"""
		pass

	def set_location(self, *aLocation):
		"""@ParamType aLocation Location*
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

	def add_location(self, aLocation):
		"""@ParamType aLocation Location
		@ReturnType void"""
		pass

	def delete_location(self, aLocation):
		"""@ParamType aLocation Location
		@ReturnType void"""
		pass

	def __init__(self):
		self.__location = None
		"""@AttributeType Location*"""

