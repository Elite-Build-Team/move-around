# -*- coding: UTF-8 -*-
from Model import ScheduledMeeting
from Model import ReportIssue
from Model import User

class PublicServiceWorker(User):
	def get_meetings(self):
		"""@ReturnType Model.ScheduledMeeting*"""
		pass

	def set_meetings(self, *meetings):
		"""@ParamType meetings Model.ScheduledMeeting*
		@ReturnType void"""
		pass

	def get_public_service_name(self):
		"""@ReturnType string"""
		pass

	def set_public_service_name(self, public_service_name):
		"""@ParamType public_service_name string
		@ReturnType void"""
		pass

	def get_reported_issues(self):
		"""@ReturnType Model.ReportIssue*"""
		pass

	def set_reported_issues(self, *reported_issues):
		"""@ParamType reported_issues Model.ReportIssue*
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

	def delete_meeting(self, meeting):
		"""@ParamType meeting Model.ScheduledMeeting
		@ReturnType void"""
		pass

	def add_meeting(self, meeting):
		"""@ParamType meeting Model.ScheduledMeeting
		@ReturnType void"""
		pass

	def __init__(self):
		self.__meetings = None
		"""@AttributeType Model.ScheduledMeeting*"""
		self.__public_service_name = None
		"""@AttributeType string"""
		self.__reported_issues = None
		"""@AttributeType Model.ReportIssue*"""

