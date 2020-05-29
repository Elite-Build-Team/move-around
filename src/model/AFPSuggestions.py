# -*- coding: UTF-8 -*-
from typing import List

from model import AFP


class AFPSuggestions(object):
    def get_afp_suggestions(self) -> List[AFP]:
        return self.__afp_suggestions

    def set_afp_suggestions(self, afp_suggestions: List[AFP]):
        self.__afp_suggestions = afp_suggestions

    def add_suggestion(self, suggestion: AFP):
        self.__afp_suggestions.append(suggestion)

    def delete_suggestion(self, suggestion: AFP):
        self.__afp_suggestions.remove(suggestion)

    def __init__(self):
        self.__afp_suggestions: List[AFP] = []
