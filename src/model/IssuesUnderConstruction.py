# -*- coding: UTF-8 -*-
import ServiceInfo
import ReportIssue
from typing import List


class IssuesUnderConstruction(object):
    def __init__(self):
        self.__service_info: ServiceInfo = None
        self.__report_issues: List[ReportIssue] = None

    @property
    def __service_info(self):
        return

    @__service_info.setter
    def __service_info(self, value):
        pass

    @__service_info.deleter
    def __service_info(self):
        pass

    @property
    def __report_issues(self):
        return

    @__report_issues.setter
    def __report_issues(self, value):
        pass

    @__report_issues.deleter
    def __report_issues(self):
        pass
