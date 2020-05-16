# -*- coding: UTF-8 -*-
from typing import List

from model import ReportIssue


class PendingIssues(object):
    def __init__(self):
        self.pending_issues: List[ReportIssue] = []

    @property
    def pending_issues(self):
        return self.__pending_issues

    @pending_issues.setter
    def pending_issues(self, value):
        self.__pending_issues = value

    @pending_issues.deleter
    def pending_issues(self):
        del self.__pending_issues

    def add_pending_issue(self, pending_issue: ReportIssue):
        self.pending_issues.append(pending_issue)

    def delete_pending_issue(self, pending_issue: ReportIssue):
        self.pending_issues.remote(pending_issue)
