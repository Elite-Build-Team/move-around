# -*- coding: UTF-8 -*-
import AMEA
import Location

class TaxiBooking(object):
	def get_date(self):
		"""@ReturnType Date"""
		pass

	def set_date(self, aDate):
		"""@ParamType aDate Date
		@ReturnType void"""
		pass

	def get_time(self):
		"""@ReturnType Time"""
		pass

	def set_time(self, aTime):
		"""@ParamType aTime Time
		@ReturnType void"""
		pass

	def get_amea(self):
		"""@ReturnType AMEA"""
		pass

	def set_amea(self, aAmea):
		"""@ParamType aAmea AMEA
		@ReturnType void"""
		pass

	def get_location(self):
		"""@ReturnType Location"""
		pass

	def set_location(self, aLocation):
		"""@ParamType aLocation Location
		@ReturnType void"""
		pass

	def __init__(self):
		self.__date = None
		"""@AttributeType Date"""
		self.__time = None
		"""@AttributeType Time"""
		self.__amea = None
		"""@AttributeType AMEA"""
		self.__location = None
		"""@AttributeType Location"""

