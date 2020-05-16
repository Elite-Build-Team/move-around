from typing import List

from model import AFP


class AFPSuggestions:
    def __init__(self):
        self.afp_suggestions: List[AFP] = []

    @property
    def afp_suggestions(self):
        return self.__afp_suggestions

    @afp_suggestions.setter
    def afp_suggestions(self, value):
        self.__afp_suggestions = value

    @afp_suggestions.deleter
    def afp_suggestions(self):
        del self.__afp_suggestions
