# -*- coding: UTF-8 -*-
from model import Photograph, Location, ReportIssueStatus


class ReportIssue(object):
    def __init__(self):
        self.photograph: Photograph = None
        self.location: Location = None
        self.summary: str = ''
        self.status: ReportIssueStatus = None

    @property
    def photograph(self):
        return self.__photograph

    @photograph.setter
    def photograph(self, value):
        self.__photograph = value

    @photograph.deleter
    def photograph(self):
        del self.__photograph

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        self.__location = value

    @location.deleter
    def location(self):
        del self.__location

    @property
    def summary(self):
        return self.__summary

    @summary.setter
    def summary(self, value):
        self.__summary = value

    @summary.deleter
    def summary(self):
        del self.__summary

    def is_pending(self) -> bool:
        return self.status == ReportIssueStatus.PENDING
