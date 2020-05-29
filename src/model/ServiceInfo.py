# -*- coding: UTF-8 -*-
class ServiceInfo(object):
	def get_phone(self) -> str:
		return self.__phone

	def set_phone(self, phone: str):
		if len(phone) == 10:
			self.__phone = phone
		else:
			raise Exception('Phone number must be 10 digits long')

	def get_name(self) -> str:
		return self.__name

	def set_name(self, name: str):
		self.__name = name

	def __init__(self):
		self.__phone: str = ''
		self.__name: str = ''

