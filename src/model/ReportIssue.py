# -*- coding: UTF-8 -*-
import Photograph
import Location

class ReportIssue(object):
	def get_photograph(self):
		"""@ReturnType Photograph"""
		pass

	def set_photograph(self, aPhotograph):
		"""@ParamType aPhotograph Photograph
		@ReturnType void"""
		pass

	def get_location(self):
		"""@ReturnType Location"""
		pass

	def set_location(self, aLocation):
		"""@ParamType aLocation Location
		@ReturnType void"""
		pass

	def get_summary(self):
		"""@ReturnType string"""
		pass

	def set_summary(self, aSummary):
		"""@ParamType aSummary string
		@ReturnType void"""
		pass

	def is_pending(self):
		"""@ReturnType bool"""
		pass

	def __init__(self):
		self.__photograph = None
		"""@AttributeType Photograph"""
		self.__location = None
		"""@AttributeType Location"""
		self.__summary = None
		"""@AttributeType string"""

