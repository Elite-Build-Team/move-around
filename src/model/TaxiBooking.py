# -*- coding: UTF-8 -*-
import datetime

from model import AMEA
from model import Location


class TaxiBooking(object):
	def get_amea(self):
		pass

	def set_amea(self, amea: str):
		pass

	def get_location(self):
		pass

	def set_location(self, location: Location):
		pass

	def set_date_time(self, date_time: datetime):
		self.__date_time = date_time

	def get_date_time(self) -> datetime:
		return self.__date_time

	def __init__(self):
		self.__date_time: datetime = None
		self.__amea: AMEA = None
		self.__location: Location = None

