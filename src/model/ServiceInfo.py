# -*- coding: UTF-8 -*-
class ServiceInfo(object):
	def get_phone(self):
		"""@ReturnType string"""
		pass

	def set_phone(self, phone):
		"""@ParamType phone string
		@ReturnType void"""
		pass

	def get_name(self):
		"""@ReturnType string"""
		pass

	def set_name(self, name):
		"""@ParamType name string
		@ReturnType void"""
		pass

	def __init__(self):
		self.__phone = None
		"""@AttributeType string"""
		self.__name = None
		"""@AttributeType string"""

