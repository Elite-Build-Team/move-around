# -*- coding: UTF-8 -*-
from Model import IssuesUnderConstruction
from Model import User

class Municipality(User):
	def get_rending_issues(self):
		"""@ReturnType Pending Issues"""
		pass

	def set_pending_issues(self, pending_issues):
		"""@ParamType pending_issues Pending Issues
		@ReturnType void"""
		pass

	def get_under_construction(self):
		"""@ReturnType Model.IssuesUnderConstruction"""
		pass

	def set_under_construction(self, under_construction):
		"""@ParamType under_construction Model.IssuesUnderConstruction
		@ReturnType void"""
		pass

	def get_service_catalog(self):
		"""@ReturnType Service Info*"""
		pass

	def set_service_catalog(self, *service_catalog):
		"""@ParamType service_catalog Service Info*
		@ReturnType void"""
		pass

	def __init__(self):
		self.__pending_issues = None
		"""@AttributeType Pending Issues"""
		self.__under_construction = None
		"""@AttributeType Model.IssuesUnderConstruction"""
		self.__service_catalog = None
		"""@AttributeType Service Info*"""

