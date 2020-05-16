# -*- coding: UTF-8 -*-
class Review(object):
	def get_description(self):
		"""@ReturnType string"""
		pass

	def set_description(self, aDescription):
		"""@ParamType aDescription string
		@ReturnType void"""
		pass

	def get_stars(self):
		"""@ReturnType int"""
		pass

	def set_stars(self, aStars):
		"""@ParamType aStars int
		@ReturnType void"""
		pass

	def __init__(self):
		self.description = None
		"""@AttributeType string"""
		self.stars = None
		"""@AttributeType int"""

