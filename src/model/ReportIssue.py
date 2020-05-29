# -*- coding: UTF-8 -*-
from Model import Photograph
from Model import Location

class ReportIssue(object):
	def get_photograph(self):
		"""@ReturnType Model.Photograph"""
		pass

	def set_photograph(self, photograph):
		"""@ParamType photograph Model.Photograph
		@ReturnType void"""
		pass

	def get_location(self):
		"""@ReturnType Model.Location"""
		pass

	def set_location(self, location):
		"""@ParamType location Model.Location
		@ReturnType void"""
		pass

	def get_summary(self):
		"""@ReturnType string"""
		pass

	def set_summary(self, summary):
		"""@ParamType summary string
		@ReturnType void"""
		pass

	def is_pending(self):
		"""@ReturnType bool"""
		pass

	def get_issue_details(self):
		"""@ReturnType Photograph, Location, string"""
		pass

	def update_issue_details(self, photograph, location, string):
		pass

	def __init__(self):
		self.__photograph = None
		"""@AttributeType Model.Photograph"""
		self.__location = None
		"""@AttributeType Model.Location"""
		self.__summary = None
		"""@AttributeType string"""

