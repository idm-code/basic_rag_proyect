from rag.loaders.text import TextAndPdfFileLoader
from utils.logger import get_logger

def main():
    logger = get_logger()
    loader = TextAndPdfFileLoader()
    docs = loader.load("ADD HERE YOUR PDF OR TXT FILES PATH")
    logger.info(f"Documents loaded: {len(docs)}")
    for doc in docs:
        logger.info(f"Source: {doc.source}, Long: {len(doc.content)} characters")

if __name__ == "__main__":
    main()