# -*- coding: UTF-8 -*-
import datetime


class ScheduledMeeting(object):
    def __init__(self):
        self.__date: datetime = None
        # self.__time = None
        self.__public_service_name: str = None

    @property
    def __date(self):
        return

    @__date.setter
    def __date(self, value):
        pass

    @__date.deleter
    def __date(self):
        pass

    @property
    def __public_service_name(self):
        return

    @__public_service_name.setter
    def __public_service_name(self, value):
        pass

    @__public_service_name.deleter
    def __public_service_name(self):
        pass
