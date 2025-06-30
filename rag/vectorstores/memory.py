from typing import List, Any, Tuple
from rag.vectorstores.base_vectorstore import BaseVectorStore
import numpy as np

class MemoryVectorStore(BaseVectorStore):
    def __init__(self):
        self.embeddings: List[List[float]] = []
        self.documents: List[Any] = []

    def add(self, embeddings: List[List[float]], documents: List[Any]):
        self.embeddings.extend(embeddings)
        self.documents.extend(documents)

    def search(self, query_embedding: List[float], top_k: int = 5) -> List[Tuple[Any, float]]:
        if not self.embeddings:
            return []
        emb_matrix = np.array(self.embeddings)
        query = np.array(query_embedding)
        norms = np.linalg.norm(emb_matrix, axis=1) * np.linalg.norm(query)
        sims = emb_matrix @ query / (norms + 1e-10)
        top_indices = np.argsort(sims)[::-1][:top_k]
        return [(self.documents[i], float(sims[i])) for i in top_indices]