# -*- coding: UTF-8 -*-
from model import Photograph
from model import Location
from typing import Tuple
from model import PendingIssues
import itertools

class ReportIssue(object):
    def get_photograph(self) -> Photograph:
        return self.__photograph

    def set_photograph(self, photograph: Photograph):
        self.__photograph = photograph

    def get_location(self) -> Location:
        return self.__location

    def set_location(self, location: Location):
        self.__location = location

    def get_summary(self) -> str:
        return self.__summary

    def set_summary(self, summary: str):
        self.__summary = summary

    def is_pending(self,ListPendings,__id):
        if self.__id in ListPendings: return True
        else: return False

    def get_issue_details(self) -> Tuple[Photograph, Location, str]:
        return self.__photograph, self.__location, self.__summary

    def update_issue_details(self, photograph: Photograph, location: Location, summary: str):
        self.__photograph = photograph
        self.__location = location
        self.__summary = summary

    def __init__(self):
        self.__id: int = itertools.count().next #TO CHECK
        self.__photograph: Photograph = None
        self.__location: Location = None
        self.__summary: str = ''
        PendingIssues.add_pending_issue(self.__id)