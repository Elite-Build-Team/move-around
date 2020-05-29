# -*- coding: UTF-8 -*-

from enum import Enum
import datetime
from typing import Tuple


class ScheduledMeetingStatus(Enum):
    Pending = 0,
    Done = 1


class ScheduledMeeting(object):
    def get_public_service_name(self) -> str:
        return self.__public_service_name
        pass

    def set_public_service_name(self, public_service_name: str):
        self.__public_service_name = public_service_name

    def get_status(self) -> ScheduledMeetingStatus:
        return self.__status

    def set_status(self, status: ScheduledMeetingStatus):
        self.__status = status

    def get_date_time(self) -> int:
        return self.__date_time

    def set_date_time(self, date_time: datetime):
        self.__date_time = date_time

    def get_amea_name(self) -> str:
        return self.__amea_name

    def set_amea_name(self, amea_name: str):
        self.__amea_name = amea_name

    def get_meeting_details(self) -> Tuple[datetime, str, ScheduledMeetingStatus, str]:
        return self.__date_time, self.__public_service_name, self.__status, self.__amea_name

    def update_meeting_details(self, date_time: datetime, public_service_name: str, status: ScheduledMeetingStatus, amea_name: str):
        self.__date_time = date_time
        self.__public_service_name = public_service_name
        self.__status = status
        self.__amea_name = amea_name

    def __init__(self):
        self.__date_time: datetime = None
        self.__public_service_name: str = ''
        self.__status: ScheduledMeetingStatus = ScheduledMeetingStatus.Pending
        self.__amea_name: str = ''
