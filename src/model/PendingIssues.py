# -*- coding: UTF-8 -*-
from Model import ReportIssue

class PendingIssues(object):
	def get_pending_issues(self):
		"""@ReturnType Model.ReportIssue*"""
		pass

	def set_pending_issues(self, *pending_issues):
		"""@ParamType pending_issues Model.ReportIssue*
		@ReturnType void"""
		pass

	def add_pending_issue(self, pending_issue):
		"""@ParamType pending_issue PendingIssue
		@ReturnType void"""
		pass

	def delete_pending_issue(self, pending_issue):
		"""@ParamType pending_issue PendingIssue
		@ReturnType void"""
		pass

	def get_issue_details(self):
		pass

	def __init__(self):
		self.__pending_issues = None
		"""@AttributeType Model.ReportIssue*"""

