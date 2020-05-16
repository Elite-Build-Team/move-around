# -*- coding: UTF-8 -*-
class Review(object):
    def __init__(self):
        self.description: str = None
        self.stars: int = None

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @description.deleter
    def description(self):
        del self.__description

    @property
    def stars(self):
        return self.__stars

    @stars.setter
    def stars(self, value):
        self.__stars = value

    @stars.deleter
    def stars(self):
        del self.__stars
