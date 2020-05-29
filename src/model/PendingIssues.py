# -*- coding: UTF-8 -*-
from Model import ReportIssue

class PendingIssues(object):
	def get_pending_issues(self) -> List[ReportIssue]:
		return self.__pending_issues

	def set_pending_issues(self, pending_issues: List[ReportIssue]):
		self.__pending_issues = pending_issues

	def add_pending_issue(self, pending_issue: ReportIssue):
		self.__pending_issues.append(pending_issue)

	def delete_pending_issue(self, pending_issue: ReportIssue):
		self.__pending_issues.remove(pending_issue)

	def get_issue_details(self):  #ToDo
		return self.__issue_details

	def __init__(self):
		self.__pending_issues: List[ReportIssue] = None


