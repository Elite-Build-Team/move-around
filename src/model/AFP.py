# -*- coding: UTF-8 -*-
import Location
import Review

class AFP(object):
	def get_location(self):
		"""@ReturnType Location"""
		pass

	def set_location(self, aLocation):
		"""@ParamType aLocation Location
		@ReturnType void"""
		pass

	def get_reviews(self):
		"""@ReturnType Review*"""
		pass

	def set_reviews(self, *aReviews):
		"""@ParamType aReviews Review*
		@ReturnType void"""
		pass

	def add_review(self, aReview):
		"""@ParamType aReview Review
		@ReturnType void"""
		pass

	def delete_review(self, aReview):
		"""@ParamType aReview Review
		@ReturnType void"""
		pass

	def setLocation(self, aLocation):
		""""""@ParamType aLocation Location"""
		@ParamType aLocation Location"""
		self.location = aLocation

	def getLocation(self):
		""""""@ReturnType Location"""
		@ReturnType Location"""
		return self.location

	def setReviews(self, *aReviews):
		""""""@ParamType aReviews Review*"""
		@ParamType aReviews Review*"""
		self.__reviews = aReviews

	def getReviews(self):
		""""""@ReturnType Review*"""
		@ReturnType Review*"""
		return self.__reviews

	def __init__(self):
		self.location = None
		"""@AttributeType Location"""
		self.__reviews = None
		"""@AttributeType Review*"""
		self._ = None
		"""@AttributeType Review
		# @AssociationType Review
		# @AssociationKind Composition"""

