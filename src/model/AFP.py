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

	def __init__(self):
		self.location = None
		"""@AttributeType Location"""
		self.__reviews = None
		"""@AttributeType Review*"""
		self._ = None
		"""@AttributeType Review
		# @AssociationType Review
		# @AssociationKind Composition"""

