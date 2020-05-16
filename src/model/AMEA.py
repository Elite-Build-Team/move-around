# -*- coding: UTF-8 -*-
import Location
import AFP
import ReportIssue
import User

class AMEA(User):
	def get_current_location(self):
		"""@ReturnType Location"""
		pass

	def set_current_location(self, aCurrent_location):
		"""@ParamType aCurrent_location Location
		@ReturnType void"""
		pass

	def get_liked_afp(self):
		"""@ReturnType AFP*"""
		pass

	def set_liked_afp(self, *aLiked_afp):
		"""@ParamType aLiked_afp AFP*
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

	def add_liked_afp(self, aAfp):
		"""@ParamType aAfp AFP
		@ReturnType void"""
		pass

	def delete_liked_afp(self, aAfp):
		"""@ParamType aAfp AFP
		@ReturnType void"""
		pass

	def __init__(self):
		self.__current_location = None
		"""@AttributeType Location"""
		self.__liked_afp = None
		"""@AttributeType AFP*"""
		self.__reported_issues = None
		"""@AttributeType ReportIssue*"""

