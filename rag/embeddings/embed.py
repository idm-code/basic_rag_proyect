from typing import List
from models.document import Document
from rag.embeddings.base_embeddings import BaseEmbedding

class SimpleEmbedding(BaseEmbedding):
    def embed(self, documents: List[Document]) -> List[List[float]]:
        embeddings = []
        for doc in documents:
            if doc.content:
                avg_ascii = sum(ord(c) for c in doc.content) / len(doc.content)
            else:
                avg_ascii = 0.0
            embeddings.append([avg_ascii])
        return embeddings