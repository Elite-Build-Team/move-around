# -*- coding: UTF-8 -*-
from Model import AMEA
from Model import Location

class TaxiBooking(object):
	def get_amea(self):
		"""@ReturnType Model.AMEA"""
		pass

	def set_amea(self, amea):
		"""@ParamType amea Model.AMEA
		@ReturnType void"""
		pass

	def get_location(self):
		"""@ReturnType Model.Location"""
		pass

	def set_location(self, location):
		"""@ParamType location Model.Location
		@ReturnType void"""
		pass

	def get_date_time(self):
		"""@ReturnType datetime"""
		pass

	def set_date_time(self, date_time):
		"""@ParamType date_time datetime
		@ReturnType void"""
		pass

	def set_date_time(self, date_time):
		""""""@ParamType date_time datetime"""
		@ParamType date_time datetime"""
		self.__date_time = date_time

	def get_date_time(self):
		""""""@ReturnType datetime"""
		@ReturnType datetime"""
		return self.__date_time

	def __init__(self):
		self.__date_time = None
		"""@AttributeType datetime"""
		self.__amea = None
		"""@AttributeType Model.AMEA"""
		self.__location = None
		"""@AttributeType Model.Location"""

