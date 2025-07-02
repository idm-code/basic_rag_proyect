from typing import Any, List, Tuple
from rag.retrievers.base_retriever import BaseRetriever
from rag.vectorstores.base_vectorstore import BaseVectorStore

class SimpleRetriever(BaseRetriever):
    def __init__(self, vectorstore: BaseVectorStore):
        self.vectorstore = vectorstore

    def retrieve(self, query_embedding: List[float], top_k: int = 5) -> List[Tuple[Any, float]]:
        return self.vectorstore.search(query_embedding, top_k=top_k)