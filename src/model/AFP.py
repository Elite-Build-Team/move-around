# -*- coding: UTF-8 -*-
import Location
import Review

from typing import List


class AFP(object):
    def __init__(self):
        self.__location: Location = None
        self.__reviews: List[Review] = None

    @property
    def __location(self):
        return

    @__location.setter
    def __location(self, value):
        pass

    @__location.deleter
    def __location(self):
        pass

    @property
    def __reviews(self):
        return

    @__reviews.setter
    def __reviews(self, value):
        pass

    @__reviews.deleter
    def __reviews(self):
        pass
