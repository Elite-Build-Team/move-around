# -*- coding: UTF-8 -*-
class User(object):
	def get_name(self):
		"""@ReturnType string"""
		pass

	def set_name(self, aName):
		"""@ParamType aName string
		@ReturnType void"""
		pass

	def get_surname(self):
		"""@ReturnType string"""
		pass

	def set_surname(self, aSurname):
		"""@ParamType aSurname string
		@ReturnType void"""
		pass

	def get_email(self):
		"""@ReturnType string"""
		pass

	def set_email(self, aEmail):
		"""@ParamType aEmail string
		@ReturnType void"""
		pass

	def __init__(self):
		self.__name = None
		"""@AttributeType string"""
		self.__surname = None
		"""@AttributeType string"""
		self.__email = None
		"""@AttributeType string"""

