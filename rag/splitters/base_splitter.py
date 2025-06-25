from typing import List
from models.document import Document

class BaseSplitter:
    def split(self, document: Document) -> List[Document]:
        raise NotImplementedError("Implement in subclasses.")