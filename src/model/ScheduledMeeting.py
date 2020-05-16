# -*- coding: UTF-8 -*-
class ScheduledMeeting(object):
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

	def get_public_service_name(self):
		"""@ReturnType string"""
		pass

	def set_public_service_name(self, aPublic_service_name):
		"""@ParamType aPublic_service_name string
		@ReturnType void"""
		pass

	def add_scheduled_meeting(self, aScheduledMeeting):
		"""@ReturnType void"""
		pass

	def delete_scheduled_meeting(self, aScheduledMeeting):
		"""@ReturnType void"""
		pass

	def __init__(self):
		self.__date = None
		"""@AttributeType Date"""
		self.__time = None
		"""@AttributeType Time"""
		self.__public_service_name = None
		"""@AttributeType string"""

