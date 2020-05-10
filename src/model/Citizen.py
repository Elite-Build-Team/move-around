# -*- coding: UTF-8 -*-
import ReportIssue
import User

from typing import List


class Citizen(User):
    def __init__(self):
        self.__reported_issues: List[ReportIssue] = None

    @property
    def __reported_issues(self):
        return

    @__reported_issues.setter
    def __reported_issues(self, value):
        pass

    @__reported_issues.deleter
    def __reported_issues(self):
        pass