# -*- coding: UTF-8 -*-
from Model import Location
from Model import AFP
from Model import ReportIssue
from Model import TaxiBooking
from Model import User

class AMEA(User):
	def get_current_location(self):
		"""@ReturnType Model.Location"""
		pass

	def set_current_location(self, current_location):
		"""@ParamType current_location Model.Location
		@ReturnType void"""
		pass

	def get_liked_afp(self):
		"""@ReturnType Model.AFP*"""
		pass

	def set_liked_afp(self, *liked_afp):
		"""@ParamType liked_afp AFP*
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

	def add_liked_afp(self, afp):
		"""@ParamType afp Model.AFP
		@ReturnType void"""
		pass

	def delete_liked_afp(self, afp):
		"""@ParamType afp Model.AFP
		@ReturnType void"""
		pass

	def add_to_taxi_bookings(self, taxi_booking):
		"""@ParamType taxi_booking Model.TaxiBooking"""
		pass

	def get_created_afp(self):
		"""@ReturnType Model.AFP*"""
		pass

	def set_created_afp(self, *created_afp):
		"""@ParamType created_afp Model.AFP*
		@ReturnType void"""
		pass

	def delete_created_afp(self, AFP):
		"""@ReturnType void"""
		pass

	def set_created_afp(self, *created_afp):
		""""""@ParamType created_afp Model.AFP*"""
		@ParamType created_afp Model.AFP*"""
		self.__created_afp = created_afp

	def get_created_afp(self):
		""""""@ReturnType Model.AFP*"""
		@ReturnType Model.AFP*"""
		return self.__created_afp

	def __init__(self):
		self.__current_location = None
		"""@AttributeType Model.Location"""
		self.__liked_afp = None
		"""@AttributeType Model.AFP*"""
		self.__reported_issues = None
		"""@AttributeType Model.ReportIssue*"""
		self.__taxi_bookings = None
		"""@AttributeType Model.TaxiBooking*"""
		self.__created_afp = None
		"""@AttributeType Model.AFP*"""

