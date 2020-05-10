# -*- coding: UTF-8 -*-
from typing import List

import ScheduledMeeting
import ReportIssue
import User


class PublicServiceWorker(User):
    def __init__(self):
        self.__meetings: List[ScheduledMeeting] = None
        self.__public_service_name: str = None
        self.__reported_issues: List[ReportIssue] = None

    @property
    def __meetings(self):
        return

    @__meetings.setter
    def __meetings(self, value):
        pass

    @__meetings.deleter
    def __meetings(self):
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

    @property
    def __reported_issues(self):
        return

    @__reported_issues.setter
    def __reported_issues(self, value):
        pass

    @__reported_issues.deleter
    def __reported_issues(self):
        pass
