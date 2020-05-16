# -*- coding: UTF-8 -*-
from datetime import datetime
from typing import List

from model import User, ScheduledMeeting


class PublicServiceWorker(User):
    def __init__(self, ):
        self.public_service_name: str = ''
        self.meetings: List[ScheduledMeeting] = []

    @property
    def meetings(self):
        return self.__meetings__

    @meetings.setter
    def meetings(self, value):
        self.__meetings = value

    @meetings.deleter
    def meetings(self):
        del self.__meetings

    @property
    def public_service_name(self):
        return self.__public_service_name

    @public_service_name.setter
    def public_service_name(self, value):
        self.__public_service_name = value

    @public_service_name.deleter
    def public_service_name(self):
        del self.__public_service_name

    def add_scheduled_meeting(self, meeting: ScheduledMeeting):
        if self.is_meeting_datetime_free(meeting.datetime):
            self.meetings.append(meeting)

    def is_meeting_datetime_free(self, meeting_datetime: datetime) -> bool:
        if meeting_datetime in [meeting.datetime for meeting in self.meetings]:
            return False
        else:
            return True

# TODO is_service_free
# TODO is_meeting_free
