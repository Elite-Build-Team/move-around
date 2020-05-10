# -*- coding: UTF-8 -*-
import Location
import AFP
import ReportIssue
import User
from typing import List


class AMEA(User):
    def __init__(self):
        self.__current_location: Location = None
        self.__liked_afp: List[AFP] = None
        self.__reported_issues = None

    @property
    def __current_location(self):
        return

    @__current_location.setter
    def __current_location(self, value):
        pass

    @__current_location.deleter
    def __current_location(self):
        pass

    @property
    def __liked_afp(self):
        return

    @__liked_afp.setter
    def __liked_afp(self, value):
        pass

    @__liked_afp.deleter
    def __liked_afp(self):
        pass
