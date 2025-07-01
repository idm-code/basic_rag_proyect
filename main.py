from rag.loaders.text import TextAndPdfFileLoader
from rag.splitters.splitter import CharacterSplitter
from rag.embeddings.embed import SimpleEmbedding
from rag.vectorstores.memory import MemoryVectorStore
from rag.indexing.indexer import SimpleIndexer
from utils.logger import get_logger

def main():
    # logger config
    logger = get_logger()

    # Loader
    loader = TextAndPdfFileLoader()
    logger.info("Iniciando carga de documentos...")
    docs = loader.load("resources/")
    logger.info(f"Documentos cargados: {len(docs)}")
    for doc in docs:
        logger.info(f"Documento cargado: {doc.source} (longitud: {len(doc.content)} caracteres) | Metadata: {doc.metadata}")

    # Splitter
    splitter = CharacterSplitter(chunk_size=1000, overlap=100)
    all_chunks = []
    for doc in docs:
        chunks = splitter.split(doc)
        all_chunks.extend(chunks)
        logger.info(f"Documento {doc.source} dividido en {len(chunks)} fragmentos")
        for chunk in chunks:
            logger.info(f"Fragmento metadata: {chunk.metadata}")
    logger.info(f"Total de fragmentos generados: {len(all_chunks)}")

    # Embeddings
    embedder = SimpleEmbedding()
    embeddings = embedder.embed(all_chunks)
    logger.info(f"Embeddings generados para {len(embeddings)} fragmentos")
    for i, emb in enumerate(embeddings[:5]):
        logger.info(f"Embedding {i}: {emb}")

    # Vector Store
    vectorstore = MemoryVectorStore()
    vectorstore.add(embeddings, all_chunks)
    logger.info("Embeddings y fragmentos añadidos al vector store.")

    # Indexing
    indexer = SimpleIndexer(loader, splitter, embedder, vectorstore)
    logger.info("Iniciando indexación...")
    chunks = indexer.index("resources/")
    logger.info(f"Total de fragmentos indexados: {len(chunks)}")

    # Ejemplo de búsqueda
    if chunks:
        embeddings = embedder.embed(chunks)
        results = vectorstore.search(embeddings[0], top_k=3)
        logger.info("Resultados de búsqueda (top 3):")
        for doc, score in results:
            logger.info(f"Score: {score:.4f} | Metadata: {doc.metadata}")

if __name__ == "__main__":
    main()