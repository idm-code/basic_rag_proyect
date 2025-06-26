from rag.loaders.text import TextAndPdfFileLoader
from rag.splitters.splitter import CharacterSplitter
from utils.logger import get_logger

def main():
    logger = get_logger()
    loader = TextAndPdfFileLoader()
    logger.info("Iniciando carga de documentos...")
    docs = loader.load("resources/")
    logger.info(f"Documentos cargados: {len(docs)}")
    for doc in docs:
        logger.info(f"Documento cargado: {doc.source} (longitud: {len(doc.content)} caracteres) | Metadata: {doc.metadata}")

    splitter = CharacterSplitter(chunk_size=1000, overlap=100)
    all_chunks = []
    for doc in docs:
        chunks = splitter.split(doc)
        all_chunks.extend(chunks)
        logger.info(f"Documento {doc.source} dividido en {len(chunks)} fragmentos")
        for chunk in chunks:
            logger.info(f"Fragmento metadata: {chunk.metadata}")
    logger.info(f"Total de fragmentos generados: {len(all_chunks)}")

if __name__ == "__main__":
    main()