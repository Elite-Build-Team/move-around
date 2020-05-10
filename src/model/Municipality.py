# -*- coding: UTF-8 -*-
from typing import List

import IssuesUnderConstruction
import PendingIssues
import ServiceInfo
import User


class Municipality(User):
    def __init__(self):
        self.__pending_issues: PendingIssues = None
        self.__under_construction: IssuesUnderConstruction = None
        self.__service_catalog: List[ServiceInfo] = None

    @property
    def __pending_issues(self):
        return

    @__pending_issues.setter
    def __pending_issues(self, value):
        pass

    @__pending_issues.deleter
    def __pending_issues(self):
        pass

    @property
    def __under_construction(self):
        return

    @__under_construction.setter
    def __under_construction(self, value):
        pass

    @__under_construction.deleter
    def __under_construction(self):
        pass

    @property
    def __service_catalog(self):
        return

    @__service_catalog.setter
    def __service_catalog(self, value):
        pass

    @__service_catalog.deleter
    def __service_catalog(self):
        pass
