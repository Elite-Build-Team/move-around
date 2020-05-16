# -*- coding: UTF-8 -*-
import IssuesUnderConstruction
import User

class Municipality(User):
	def get_rending_issues(self):
		"""@ReturnType Pending Issues"""
		pass

	def set_pending_issues(self, aPending_issues):
		"""@ParamType aPending_issues Pending Issues
		@ReturnType void"""
		pass

	def get_under_construction(self):
		"""@ReturnType IssuesUnderConstruction"""
		pass

	def set_under_construction(self, aUnder_construction):
		"""@ParamType aUnder_construction IssuesUnderConstruction
		@ReturnType void"""
		pass

	def get_service_catalog(self):
		"""@ReturnType Service Info*"""
		pass

	def set_service_catalog(self, *aService_catalog):
		"""@ParamType aService_catalog Service Info*
		@ReturnType void"""
		pass

	def __init__(self):
		self.__pending_issues = None
		"""@AttributeType Pending Issues"""
		self.__under_construction = None
		"""@AttributeType IssuesUnderConstruction"""
		self.__service_catalog = None
		"""@AttributeType Service Info*"""

