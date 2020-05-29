# -*- coding: UTF-8 -*-
class User(object):
	def get_name(self) -> str:
		return self.__name

	def set_name(self, name: str):
		self.__name = name

	def get_surname(self) -> str:
		return self.__surname

	def set_surname(self, surname: str):
		self.__surname = surname

	def get_email(self) -> str:
		return self.__email

	def set_email(self, email: str):
		self.__email = email

	def __init__(self):
		self.__name: str = ''
		self.__surname: str = ''
		self.__email: str = ''

