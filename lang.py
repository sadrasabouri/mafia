
from Role import Role
from dataclasses import dataclass
from config_loader import load_data

@dataclass
class LanguageService:
    address : str

    def __post_init__(self) -> None:
        self._data = load_data(self.address)

    def get_name(self, key : Role) -> str:
        return self._data.get("names").get(key.name)

    def get_description(self, key : Role) -> str:
        return self._data.get("descriptions").get(key.name)

english : LanguageService = LanguageService('english.json')
persian : LanguageService = LanguageService('persian.json')