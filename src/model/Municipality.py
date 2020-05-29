# -*- coding: UTF-8 -*-
from typing import List

from model import IssuesUnderConstruction
from model import User
from model import PendingIssues
from model import ServiceInfo


class Municipality(User):
	def get_pending_issues(self) -> PendingIssues:
		return self.__pending_issues

	def set_pending_issues(self, pending_issues: List[PendingIssues]):
		self.__pending_issues = pending_issues

	def get_under_construction(self) -> IssuesUnderConstruction:
		return self.__under_construction

	def set_under_construction(self, under_construction: IssuesUnderConstruction):
		self.__under_construction = under_construction

	def get_service_catalog(self) -> List[ServiceInfo]:
		return self.__service_catalog

	def set_service_catalog(self, service_catalog: List[ServiceInfo]):
		self.__service_catalog = service_catalog

	def __init__(self):
		self.__pending_issues: PendingIssues = None
		self.__under_construction: IssuesUnderConstruction = None
		self.__service_catalog: List[ServiceInfo] = []

