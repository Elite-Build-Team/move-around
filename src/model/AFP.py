# -*- coding: UTF-8 -*-
from Model import Location
from Model import Review

class AFP(object):
	def get_location(self):
		"""@ReturnType Model.Location"""
		pass

	def set_location(self, location):
		"""@ParamType location Model.Location
		@ReturnType void"""
		pass

	def get_reviews(self):
		"""@ReturnType Model.Review*"""
		pass

	def set_reviews(self, *reviews):
		"""@ParamType reviews Model.Review*
		@ReturnType void"""
		pass

	def add_review(self, review):
		"""@ParamType review Model.Review
		@ReturnType void"""
		pass

	def delete_review(self, review):
		"""@ParamType review Model.Review
		@ReturnType void"""
		pass

	def get_afp_details(self):
		"""@ReturnType Location, Review*"""
		pass

	def like_afp(self):
		pass

	def set_location(self, location):
		""""""@ParamType location Model.Location"""
		@ParamType location Model.Location"""
		self.__location = location

	def get_location(self):
		""""""@ReturnType Model.Location"""
		@ReturnType Model.Location"""
		return self.__location

	def set_reviews(self, *reviews):
		""""""@ParamType reviews Model.Review*"""
		@ParamType reviews Model.Review*"""
		self.__reviews = reviews

	def get_reviews(self):
		""""""@ReturnType Model.Review*"""
		@ReturnType Model.Review*"""
		return self.__reviews

	def __init__(self):
		self.__location = None
		"""@AttributeType Model.Location"""
		self.__reviews = None
		"""@AttributeType Model.Review*"""
		self._ = None
		"""@AttributeType Model.Review
		# @AssociationType Model.Review
		# @AssociationKind Composition"""

