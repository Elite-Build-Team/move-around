# -*- coding: UTF-8 -*-
class Review(object):
	def get_description(self):
		return self.__description

	def set_description(self, description):
		self.__description = description

	def get_stars(self):
		return self.__stars

	def set_stars(self, stars: int):
		if 0 <= stars <= 5:
			self.__stars = stars
		else:
			raise Exception("Stars must be in [0,5]")

	def update_review_details(self, description: str, stars: int):
		self.__description = description
		self.__stars = stars

	def __init__(self):
		self.__description: str = ''
		self.__stars: int = 0

