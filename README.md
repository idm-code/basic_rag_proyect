# RAG Project

Este proyecto implementa un sistema modular para la carga, división, gestión de metadata, generación de embeddings, almacenamiento/búsqueda vectorial e indexación de documentos en un flujo RAG (Retrieval-Augmented Generation). Permite la lectura eficiente de archivos `.txt` y `.pdf`, su fragmentación óptima, enriquecimiento con metadata, vectorización, indexación y búsqueda semántica para procesamiento posterior.

> **Nota:**  
> Este proyecto irá creciendo exponencialmente, añadiendo todos los pasos de la técnica RAG (Retrieval-Augmented Generation). Por lo tanto, se irá modificando y ampliando periódicamente hasta finalizar el desarrollo completo del sistema.

## Estructura del proyecto

```
main.py
requirements.txt
.gitignore
README.md
rag/
    loaders/
        base_loader.py
        text.py
    splitters/
        base_splitter.py
        splitter.py
    embeddings/
        base_embeddings.py
        embed.py
    vectorstores/
        base_vectorstore.py
        memory.py
    indexing/
        base_indexer.py
        indexer.py
models/
    document.py
resources/
    AÑADE AQUI TU FICHERO.PDF O .TXT
utils/
    logger.py
```

## Instalación

1. Clona el repositorio.
2. Instala las dependencias:

```sh
pip install -r requirements.txt
```

## Uso

1. Coloca tus archivos `.txt` o `.pdf` en la carpeta `resources/`.
2. Ejecuta el archivo principal:

```sh
python main.py
```

Esto cargará los documentos desde la ruta especificada en `main.py`, los dividirá en fragmentos usando el splitter configurado, generará embeddings para cada fragmento, almacenará los embeddings y fragmentos en una vector store en memoria, realizará la indexación y permitirá búsquedas semánticas. Toda la información relevante (metadata, embeddings, resultados de búsqueda) se muestra usando el sistema de logging.

## Componentes principales

- **models/document.py**: Modelo de datos para representar un documento, con soporte para metadata flexible.
- **rag/loaders/base_loader.py**: Clase base abstracta para loaders de documentos.
- **rag/loaders/text.py**: Loader que permite la carga de archivos `.txt` y `.pdf`, añadiendo metadata relevante (tipo de archivo, número de página, etc.).
- **rag/splitters/base_splitter.py**: Clase base abstracta para splitters de documentos.
- **rag/splitters/splitter.py**: Splitters concretos, como `CharacterSplitter` y `ParagraphSplitter`, que dividen documentos en fragmentos y enriquecen la metadata de cada fragmento.
- **rag/embeddings/base_embeddings.py**: Clase base abstracta para generadores de embeddings.
- **rag/embeddings/embed.py**: Implementación de ejemplo de un generador de embeddings (`SimpleEmbedding`).
- **rag/vectorstores/base_vectorstore.py**: Clase base abstracta para almacenamiento vectorial.
- **rag/vectorstores/memory.py**: Implementación de una vector store en memoria con búsqueda por similitud de coseno.
- **rag/indexing/base_indexer.py**: Clase base abstracta para indexadores.
- **rag/indexing/indexer.py**: Implementación de un indexador (`SimpleIndexer`) que orquesta el pipeline de carga, división, embedding y almacenamiento.
- **utils/logger.py**: Configuración centralizada del logger para el proyecto.
- **resources/**: Carpeta sugerida para almacenar los documentos a cargar.

## Metadata

Cada instancia de `Document` incluye un diccionario `metadata` que almacena información relevante, como:
- Tipo de documento (`txt`, `pdf`)
- Número de página (para PDFs)
- Índices de fragmento o párrafo (añadidos por los splitters)
- Otros campos personalizables según necesidades futuras

## Embeddings

El sistema incluye una arquitectura extensible para la generación de embeddings:
- **rag/embeddings/base_embeddings.py**: Define la interfaz base para cualquier generador de embeddings.
- **rag/embeddings/embed.py**: Implementa un ejemplo sencillo (`SimpleEmbedding`). Puedes sustituirlo o ampliarlo con modelos reales (por ejemplo, spaCy, SentenceTransformers, OpenAI, etc.).

## Vector Store

El sistema soporta almacenamiento y búsqueda vectorial:
- **rag/vectorstores/base_vectorstore.py**: Define la interfaz base para cualquier vector store.
- **rag/vectorstores/memory.py**: Implementa una vector store en memoria usando listas y búsqueda por similitud de coseno. Puedes extenderlo para usar FAISS, Pinecone, ChromaDB, etc.

## Indexing

El sistema centraliza el pipeline de indexación:
- **rag/indexing/base_indexer.py**: Define la interfaz base para cualquier indexador.
- **rag/indexing/indexer.py**: Implementa `SimpleIndexer`, que orquesta la carga, división, embedding y almacenamiento en la vector store.

## Personalización y extensión

- Puedes extender el sistema añadiendo nuevos loaders para otros formatos de archivo siguiendo la estructura de `BaseLoader`.
- Puedes crear nuevos splitters para diferentes estrategias de fragmentación heredando de `BaseSplitter`.
- Puedes enriquecer la metadata en cualquier punto del pipeline para adaptarla a tus necesidades.
- Puedes implementar nuevos generadores de embeddings heredando de `BaseEmbedding`.
- Puedes crear nuevas vector stores heredando de `BaseVectorStore`.
- Puedes crear nuevos indexadores heredando de `BaseIndexer` para flujos personalizados.

## Ejemplo de uso en código

```python
from rag.loaders.text import TextAndPdfFileLoader
from rag.splitters.splitter import CharacterSplitter
from rag.embeddings.embed import SimpleEmbedding
from rag.vectorstores.memory import MemoryVectorStore
from rag.indexing.indexer import SimpleIndexer
from utils.logger import get_logger

def main():
    logger = get_logger()
    loader = TextAndPdfFileLoader()
    splitter = CharacterSplitter(chunk_size=1000, overlap=100)
    embedder = SimpleEmbedding()
    vectorstore = MemoryVectorStore()

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
```

## Dependencias

- [PyPDF2](https://pypi.org/project/PyPDF2/): Para la lectura de archivos PDF.
- [numpy](https://pypi.org/project/numpy/): Para operaciones vectoriales en la vector store.

---

¡Contribuciones y sugerencias son bienvenidas!

