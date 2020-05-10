# -*- coding: UTF-8 -*-
from typing import List

import ReportIssue


class PendingIssues(object):
    def __init__(self):
        self.__pending_issues: List[ReportIssue] = None

    @property
    def __pending_issues(self):
        return

    @__pending_issues.setter
    def __pending_issues(self, value):
        pass

    @__pending_issues.deleter
    def __pending_issues(self):
        pass
