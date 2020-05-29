# -*- coding: UTF-8 -*-
from model import Location
from model import Review
from typing import List


class AFP(object):
    def get_location(self) -> Location:
        return self.__location

    def set_location(self, location: Location):
        self.__location = location

    def get_reviews(self) -> List[Review]:
        return self.__reviews

    def set_reviews(self, reviews: List[Review]):
        self.__reviews = reviews

    def add_review(self, review: Review):
        self.__reviews.append(review)

    def delete_review(self, review: Review):
        self.__reviews.remove(review)

    def get_afp_details(self) -> [Location, List[Review]]:
        return self.__location, self.__reviews

    def like_afp(self):
        raise NotImplementedError

    def __init__(self):
        self.__location: Location = Location
        self.__reviews: List[Review] = []
