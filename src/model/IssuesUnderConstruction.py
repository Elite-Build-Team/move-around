# -*- coding: UTF-8 -*-
import ServiceInfo
import ReportIssue

class IssuesUnderConstruction(object):
	def get_service_info(self):
		"""@ReturnType ServiceInfo"""
		pass

	def set_service_info(self, aService_info):
		"""@ParamType aService_info ServiceInfo
		@ReturnType void"""
		pass

	def get_report_issues(self):
		"""@ReturnType ReportIssue*"""
		pass

	def set_report_issues(self, *aReport_issues):
		"""@ParamType aReport_issues ReportIssue*
		@ReturnType void"""
		pass

	def add_issue_under_construction(self, aIssue_under_consturction):
		"""@ParamType aIssue_under_consturction IssueUnderConstruction
		@ReturnType void"""
		pass

	def delete_issue_under_construction(self, aIssue_under_construction):
		"""@ParamType aIssue_under_construction IssueUnderConstruction
		@ReturnType void"""
		pass

	def __init__(self):
		self.__service_info = None
		"""@AttributeType ServiceInfo"""
		self.__report_issues = None
		"""@AttributeType ReportIssue*"""

