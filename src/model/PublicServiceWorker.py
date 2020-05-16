# -*- coding: UTF-8 -*-
import ScheduledMeeting
import ReportIssue
import User

class PublicServiceWorker(User):
	def get_meetings(self):
		"""@ReturnType ScheduledMeeting*"""
		pass

	def set_meetings(self, *aMeetings):
		"""@ParamType aMeetings ScheduledMeeting*
		@ReturnType void"""
		pass

	def get_public_service_name(self):
		"""@ReturnType string"""
		pass

	def set_public_service_name(self, aPublic_service_name):
		"""@ParamType aPublic_service_name string
		@ReturnType void"""
		pass

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
		self.__meetings = None
		"""@AttributeType ScheduledMeeting*"""
		self.__public_service_name = None
		"""@AttributeType string"""
		self.__reported_issues = None
		"""@AttributeType ReportIssue*"""

