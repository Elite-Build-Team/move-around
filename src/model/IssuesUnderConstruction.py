# -*- coding: UTF-8 -*-
from typing import List

from model import ServiceInfo, ReportIssue


class IssuesUnderConstruction(object):
    def __init__(self):
        self.service_info: ServiceInfo = None
        self.report_issues: List[ReportIssue] = []

    @property
    def service_info(self):
        return self.__service_info

    @service_info.setter
    def service_info(self, value):
        self.__service_info = value

    @service_info.deleter
    def service_info(self):
        del self.__service_info

    @property
    def report_issues(self):
        return self.report_issues

    @report_issues.setter
    def report_issues(self, value):
        self.__report_issues = value

    @report_issues.deleter
    def report_issues(self):
        del self.__report_issues
