# -*- coding: UTF-8 -*-
import ReportIssue
import User

class Citizen(User):
	def get_reported_issues(self):
		"""@ReturnType ReportIssue*"""
		pass

	def set_reported_issues(self, *aReported_issues):
		"""@ParamType aReported_issues ReportIssue*
		@ReturnType void"""
		pass

	def add_report_issue(self, aReport_issue):
		"""@ParamType aReport_issue ReportIssue
		@ReturnType void"""
		pass

	def delete_report_issue(self, aReport_issue):
		"""@ParamType aReport_issue ReportIssue
		@ReturnType void"""
		pass

	def __init__(self):
		self.__reported_issues = None
		"""@AttributeType ReportIssue*"""

