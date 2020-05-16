# -*- coding: UTF-8 -*-
class ServiceInfo(object):
    def __init__(self):
        self.phone: str = ''
        self.name: str = ''

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @phone.deleter
    def phone(self):
        del self.__phone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name
