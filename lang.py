from typing import Dict, List
from dataclasses import dataclass
from config import load_data

@dataclass
class LanguageService:
    address : str

    def __post_init__(self) -> None:
        self._data = load_data(self.address)

    def get_name(self, key : str) -> str:
        return self._data.get("names").get(key)

    def get_description(self, key : str) -> str:
        return self._data.get("descriptions").get(key)

english : LanguageService = LanguageService('english.json')
persian : LanguageService = LanguageService('persian.json')