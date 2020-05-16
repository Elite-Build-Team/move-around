# -*- coding: UTF-8 -*-
import AFP

class AFPSuggestions(object):
	def get_afp_suggestions(self):
		"""@ReturnType Suggestions*"""
		pass

	def set_afp_suggestions(self, *aAfp_suggestions):
		"""@ParamType aAfp_suggestions Suggestions*
		@ReturnType void"""
		pass

	def add_suggestion(self, aAfp):
		"""@ParamType aAfp AFP
		@ReturnType void"""
		pass

	def delete_suggestion(self, aAfp):
		"""@ParamType aAfp AFP
		@ReturnType void"""
		pass

	def __init__(self):
		self.__afp_suggestions = None
		"""@AttributeType AFP*"""
		self._ = None
		"""@AttributeType AFP
		# @AssociationType AFP"""

