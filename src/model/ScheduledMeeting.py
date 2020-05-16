# -*- coding: UTF-8 -*-
import datetime

from model import ScheduledMeetingStatus


class ScheduledMeeting(object):
    def __init__(self):
        self.datetime: datetime = None
        self.public_service_name: str = ''
        self.status: ScheduledMeetingStatus = None

    @property
    def datetime(self):
        return self.__datetime

    @datetime.setter
    def datetime(self, value):
        self.__datetime = value

    @datetime.deleter
    def datetime(self):
        del self.__datetime

    @property
    def public_service_name(self):
        return self.__public_service_name

    @public_service_name.setter
    def public_service_name(self, value):
        self.__public_service_name = value

    @public_service_name.deleter
    def public_service_name(self):
        del self.__public_service_name
