# -*- coding: UTF-8 -*-
class ScheduledMeeting(object):
	def get_public_service_name(self):
		"""@ReturnType string"""
		pass

	def set_public_service_name(self, public_service_name):
		"""@ParamType public_service_name string
		@ReturnType void"""
		pass

	def get_meeting_details(self):
		pass

	def update_meeting_details(self, string):
		pass

	def get_status(self):
		"""@ReturnType enum(Pending, Done)"""
		pass

	def set_status(self, status):
		"""@ParamType status enum(Pending, Done)
		@ReturnType void"""
		pass

	def get_date_time(self):
		"""@ReturnType datetime"""
		pass

	def set_date_time(self, date_time):
		"""@ParamType date_time datetime
		@ReturnType void"""
		pass

	def get_amea_name(self):
		"""@ReturnType string"""
		pass

	def set_amea_name(self, amea_name):
		"""@ParamType amea_name string
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

	def set_status(self, status):
		""""""@ParamType status enum(Pending, Done)"""
		@ParamType status enum(Pending, Done)"""
		self.__status = status

	def get_status(self):
		""""""@ReturnType enum(Pending, Done)"""
		@ReturnType enum(Pending, Done)"""
		return self.__status

	def set_amea_name(self, amea_name):
		""""""@ParamType amea_name string"""
		@ParamType amea_name string"""
		self.__amea_name = amea_name

	def get_amea_name(self):
		""""""@ReturnType string"""
		@ReturnType string"""
		return self.__amea_name

	def __init__(self):
		self.__date_time = None
		"""@AttributeType datetime"""
		self.__public_service_name = None
		"""@AttributeType string"""
		self.__status = None
		"""@AttributeType enum(Pending, Done)"""
		self.__amea_name = None
		"""@AttributeType string"""

