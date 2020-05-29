# -*- coding: UTF-8 -*-
from model import ServiceInfo
from model import ReportIssue

from typing import List


class IssuesUnderConstruction(object):
	def get_service_info(self) -> ServiceInfo:
		return self.__service_info

	def set_service_info(self, service_info: ServiceInfo):
		self.__service_info = service_info

	def get_report_issues(self) -> List[ReportIssue]:
		return self.__report_issues

	def set_report_issues(self, report_issues: List[ReportIssue]):
		self.__report_issues = report_issues

	def add_issue_under_construction(self, issue_under_consturction: ReportIssue):
		self.__report_issues.append(issue_under_consturction)

	def delete_issue_under_construction(self, issue_under_construction: ReportIssue):
		self.__report_issues.remove(issue_under_construction)

	def __init__(self):
		self.__service_info = None
		self.__report_issues = None

