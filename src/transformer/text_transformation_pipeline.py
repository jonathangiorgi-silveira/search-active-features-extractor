import unicodedata
import re

from abc import (ABC, abstractmethod)


class TextTransformer(ABC):
    
    @abstractmethod
    def transform(self, text: str) -> str:
        pass

class WhiteSpaceToUnderscoreReplacement(TextTransformer):
    
    def transform(self, text: str) -> str:
        return text.replace(" ", "_")
    
class LowerCaseTransformer(TextTransformer):
    
    def transform(self, text: str) -> str:
        return text.lower()
    
class SpecialCharacterRemovalTransformer(TextTransformer):
    
    def transform(self, text: str) -> str:
        return re.sub(r"[^a-zA-Z0-9\s]", "", text)
    
class AccentRemovalTransformer(TextTransformer):
    
    def transform(self, text: str) -> str:
        nfkd_form = unicodedata.normalize('NFKD', text)
        return "".join([c for c in nfkd_form if not unicodedata.combining(c)])
    
class TextTransformationPipeline:

    def __init__(self, transformers: list[TextTransformer]):
        self.transformers = transformers

    def transform(self, text: str) -> str:
        transformed_text = text
        for transformer in self.transformers:
            transformed_text = transformer.transform(transformed_text)
        return transformed_text