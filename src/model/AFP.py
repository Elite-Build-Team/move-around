# -*- coding: UTF-8 -*-

from typing import List

from model import Location, Review


class AFP(object):
    def __init__(self):
        self.location: Location = None
        self.reviews: List[Review] = []

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        self.__location = value

    @location.deleter
    def location(self):
        del self.__location

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, value):
        self.__reviews = value

    @reviews.deleter
    def reviews(self):
        del self.__reviews

    def add_review(self, review):
        self.reviews.append(review)
