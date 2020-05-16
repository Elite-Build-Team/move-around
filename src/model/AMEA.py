# -*- coding: UTF-8 -*-
from typing import List

from model import User, Location, AFP


class AMEA(User):
    def __init__(self):
        self.current_location: Location = None
        self.liked_afp: List[AFP] = []
        self.taxi_bookings = None

    @property
    def current_location(self):
        return self.__current_location

    @current_location.setter
    def current_location(self, value):
        self.__current_location = value

    @current_location.deleter
    def current_location(self):
        del self.__current_location

    @property
    def liked_afp(self):
        return self.__liked_afp

    @liked_afp.setter
    def liked_afp(self, value):
        self.__liked_afp = value

    @liked_afp.deleter
    def liked_afp(self):
        del self.__liked_afp

    def add_liked_afp(self, afp):
        self.liked_afp.append(afp)
