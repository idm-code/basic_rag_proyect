from typing import Any, List
from rag.loaders.base_loader import BaseLoader
from rag.splitters.base_splitter import BaseSplitter
from rag.embeddings.base_embeddings import BaseEmbedding
from rag.vectorstores.base_vectorstore import BaseVectorStore
from rag.indexing.base_indexer import BaseIndexer
from models.document import Document

class SimpleIndexer(BaseIndexer):
    def __init__(
        self,
        loader: BaseLoader,
        splitter: BaseSplitter,
        embedder: BaseEmbedding,
        vectorstore: BaseVectorStore,
    ):
        self.loader = loader
        self.splitter = splitter
        self.embedder = embedder
        self.vectorstore = vectorstore

    def index(self, path: str) -> List[Document]:
        # Load documents
        documents = self.loader.load(path)
        # Split documents
        chunks = []
        for doc in documents:
            chunks.extend(self.splitter.split(doc))
        # Generate embeddings
        embeddings = self.embedder.embed(chunks)
        # Store in vector store
        self.vectorstore.add(embeddings, chunks)
        return chunks