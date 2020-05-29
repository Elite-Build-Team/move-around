# -*- coding: UTF-8 -*-
class Review(object):
	def get_description(self):
		"""@ReturnType string"""
		pass

	def set_description(self, description):
		"""@ParamType description string
		@ReturnType void"""
		pass

	def get_stars(self):
		"""@ReturnType int"""
		pass

	def set_stars(self, stars):
		"""@ParamType stars int
		@ReturnType void"""
		pass

	def update_review_details(self, string, int):
		"""@ReturnType void"""
		pass

	def __init__(self):
		self.__description = None
		"""@AttributeType string"""
		self.__stars = None
		"""@AttributeType int"""

