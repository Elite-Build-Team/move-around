# -*- coding: UTF-8 -*-
from Model import ReportIssue
from Model import User

class Citizen(User):
	def get_reported_issues(self):
		"""@ReturnType Model.ReportIssue*"""
		pass

	def set_reported_issues(self, *reported_issues):
		"""@ParamType reported_issues ReportIssue*
		@ReturnType void"""
		pass

	def add_report_issue(self, report_issue):
		"""@ParamType report_issue Model.ReportIssue
		@ReturnType void"""
		pass

	def delete_report_issue(self, report_issue):
		"""@ParamType report_issue Model.ReportIssue
		@ReturnType void"""
		pass

	def __init__(self):
		self.__reported_issues = None
		"""@AttributeType Model.ReportIssue*"""

