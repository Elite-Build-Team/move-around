# -*- coding: UTF-8 -*-
from typing import List

from model import ReportIssue


class User(object):
    def __init__(self):
        self.name: str = ''
        self.surname: str = ''
        self.email: str = ''
        self.reported_issues: List[ReportIssue] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @surname.deleter
    def surname(self):
        del self.__surname

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @email.deleter
    def email(self):
        del self.__email

    @property
    def reported_issues(self):
        return self.__reported_issues

    @reported_issues.setter
    def reported_issues(self, value):
        self.__reported_issues = value

    @reported_issues.deleter
    def reported_issues(self):
        del self.__reported_issues

    def add_report_issue(self, report_issue):
        self.reported_issues.append(report_issue)