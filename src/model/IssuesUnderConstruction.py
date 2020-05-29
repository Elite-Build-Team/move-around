# -*- coding: UTF-8 -*-
from Model import ServiceInfo
from Model import ReportIssue

class IssuesUnderConstruction(object):
	def get_service_info(self):
		"""@ReturnType Model.ServiceInfo"""
		pass

	def set_service_info(self, service_info):
		"""@ParamType service_info Model.ServiceInfo
		@ReturnType void"""
		pass

	def get_report_issues(self):
		"""@ReturnType Model.ReportIssue*"""
		pass

	def set_report_issues(self, *report_issues):
		"""@ParamType report_issues Model.ReportIssue*
		@ReturnType void"""
		pass

	def add_issue_under_construction(self, issue_under_consturction):
		"""@ParamType issue_under_consturction IssueUnderConstruction
		@ReturnType void"""
		pass

	def delete_issue_under_construction(self, issue_under_construction):
		"""@ParamType issue_under_construction IssueUnderConstruction
		@ReturnType void"""
		pass

	def __init__(self):
		self.__service_info = None
		"""@AttributeType Model.ServiceInfo"""
		self.__report_issues = None
		"""@AttributeType Model.ReportIssue*"""

