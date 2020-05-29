# -*- coding: UTF-8 -*-
from model import Location
from model import AFP
from model import ReportIssue
from model import TaxiBooking
from model import User
from typing import List

class AMEA(User):
	def get_current_location(self) -> Location:
		return self.__current_location

	def set_current_location(self, current_location : Location):
		self.__current_location = current_location

	def get_liked_afp(self) -> List[AFP]:
		return self.__liked_afp

	def set_liked_afp(self, liked_afp : List[AFP]):
		self.__liked_afp = liked_afp

	def get_reported_issues(self) -> List[ReportIssue]:
		return self.__reported_issues

	def set_reported_issues(self, reported_issues : List[ReportIssue]):
		self.__reported_issues = reported_issues

	def add_report_issue(self, report_issue : ReportIssue):
		self.__reported_issues.append(report_issue)

	def delete_report_issue(self, report_issue : ReportIssue):
		self.__reported_issues.delete(report_issue)

	def add_liked_afp(self, afp : AFP):
		self.__liked_afp.append(afp)

	def delete_liked_afp(self, afp):
		self.__liked_afp.delete(afp)

	def add_to_taxi_bookings(self, taxi_booking : TaxiBooking):
		self.__taxi_bookings.append(taxi_booking)
	
	def get_taxi_bookings(self) -> List[TaxiBooking]:
		return self.__taxi_bookings

	def set_taxi_bookings(self, taxi_bookings : List[TaxiBooking]):
		self.__taxi_bookings = taxi_bookings

	def get_created_afp(self) -> List[AFP]:
		return self.__created_afp

	def set_created_afp(self, created_afp : AFP):
		self.__created_afp = created_afp

	def delete_created_afp(self, afp : AFP):
		self.__created_afp.delete(afp)

	def __init__(self):
		self.__current_location = None
		self.__liked_afp = None
		self.__reported_issues = None
		self.__taxi_bookings = None
		self.__created_afp = None

