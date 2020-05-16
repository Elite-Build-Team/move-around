# -*- coding: UTF-8 -*-
from datetime import datetime

from model import AMEA, Location


class TaxiBooking(object):
    def __init__(self):
        self.date: datetime = None
        self.amea: AMEA = None
        self.location: Location = None

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    @date.deleter
    def date(self):
        del self.__date

    @property
    def amea(self):
        return self.__amea

    @amea.setter
    def amea(self, value):
        self.__amea = value

    @amea.deleter
    def amea(self):
        del self.__amea

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        self.__location = value

    @location.deleter
    def location(self):
        del self.__location
