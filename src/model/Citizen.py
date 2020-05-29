# -*- coding: UTF-8 -*-
from model import ReportIssue
from model import User

from typing import List


class Citizen(User):
	def get_reported_issues(self) -> List[ReportIssue]:
		return self.__reported_issues

	def set_reported_issues(self, reported_issues: List[ReportIssue]):
		self.__reported_issues = reported_issues

	def add_report_issue(self, report_issue: ReportIssue):
		self.__reported_issues.append(report_issue)

	def delete_report_issue(self, report_issue: ReportIssue):
		self.__reported_issues.remove(report_issue)

	def __init__(self):
		self.__reported_issues: List[ReportIssue] = []