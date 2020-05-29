# -*- coding: UTF-8 -*-
from Model import ScheduledMeeting
from Model import ReportIssue
from Model import User

class PublicServiceWorker(User):
	def get_meetings(self) -> List[ScheduledMeeting]:
		return self.__meetings

	def set_meetings(self, meetings: List[ScheduledMeeting]):
		self.__meetings = meetings

	def get_public_service_name(self) -> str:
		return self.__public_service_name

	def set_public_service_name(self, public_service_name: str):
		self.__public_service_name = public_service_name

	def get_reported_issues(self) -> List[ReportIssue]:
		return self.__reported_issues

	def set_reported_issues(self, reported_issues: List[ReportIssue]):
		self.__reported_issues = reported_issues

	def add_report_issue(self, report_issue: ReportIssue):
		self.__reported_issues.append(report_issue)

	def delete_report_issue(self, report_issue: ReportIssue):
		self.__reported_issues.remove(report_issue)

	def delete_meeting(self, meeting: ScheduledMeeting):
		self.__meetings.remove(meeting)

	def add_meeting(self, meeting: ScheduledMeeting):
		self.__meetings.append(meeting)

	def __init__(self):
		self.__meetings: List[ScheduledMeeting] = None
		self.__public_service_name: str = " "
		self.__reported_issues: List[ReportIssue] = None

