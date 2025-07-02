from typing import Any, List

class BaseRetriever:
    def retrieve(self, query_embedding: List[float], top_k: int = 5) -> List[Any]:
        raise NotImplementedError("Implement in subclasses.")