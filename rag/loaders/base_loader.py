from typing import List
from models.document import Document

class BaseLoader:
    def load(self, path: str) -> List[Document]:
        raise NotImplementedError("Implement in subclasses.")