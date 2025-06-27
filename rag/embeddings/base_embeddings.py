from typing import List
from models.document import Document

class BaseEmbedding:
    def embed(self, documents: List[Document]) -> List[List[float]]:
        raise NotImplementedError("Implement in subclasses.")