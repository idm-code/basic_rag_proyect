from typing import List, Any

class BaseVectorStore:
    def add(self, embeddings: List[List[float]], documents: List[Any]):
        raise NotImplementedError("Implement in subclasses.")

    def search(self, query_embedding: List[float], top_k: int = 5) -> List[Any]:
        raise NotImplementedError("Implement in subclasses.")