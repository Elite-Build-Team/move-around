# -*- coding: UTF-8 -*-
from typing import List

from model import PendingIssues, IssuesUnderConstruction, ServiceInfo, User


class Municipality(User):
    def __init__(self):
        self.pending_issues: PendingIssues = None
        self.under_construction: IssuesUnderConstruction = None
        self.service_catalog: List[ServiceInfo] = []

    @property
    def pending_issues(self):
        return self.__pending_issues

    @pending_issues.setter
    def pending_issues(self, value):
        self.__pending_issues = value

    @pending_issues.deleter
    def pending_issues(self):
        del self.__pending_issues

    @property
    def under_construction(self):
        return self.__under_construction

    @under_construction.setter
    def under_construction(self, value):
        self.__under_construction = value

    @under_construction.deleter
    def under_construction(self):
        del self.__under_construction

    @property
    def service_catalog(self):
        return self.__service_catalog

    @service_catalog.setter
    def service_catalog(self, value):
        self.__service_catalog = value

    @service_catalog.deleter
    def service_catalog(self):
        del self.__service_catalog
