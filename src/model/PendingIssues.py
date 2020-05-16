# -*- coding: UTF-8 -*-
import ReportIssue

class PendingIssues(object):
	def get_pending_issues(self):
		"""@ReturnType ReportIssue*"""
		pass

	def set_pending_issues(self, *aPending_issues):
		"""@ParamType aPending_issues ReportIssue*
		@ReturnType void"""
		pass

	def add_pending_issue(self, aPending_issue):
		"""@ParamType aPending_issue PendingIssue
		@ReturnType void"""
		pass

	def delete_pending_issue(self, aPending_issue):
		"""@ParamType aPending_issue PendingIssue
		@ReturnType void"""
		pass

	def __init__(self):
		self.__pending_issues = None
		"""@AttributeType ReportIssue*"""

