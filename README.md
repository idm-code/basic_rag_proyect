# RAG Project

Este proyecto implementa un sistema modular para la carga, división, gestión de metadata y generación de embeddings de documentos en un flujo RAG (Retrieval-Augmented Generation), permitiendo la lectura eficiente de archivos `.txt` y `.pdf`, su fragmentación óptima, enriquecimiento con metadata y vectorización para procesamiento posterior.

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

Esto cargará los documentos desde la ruta especificada en `main.py`, los dividirá en fragmentos usando el splitter configurado, generará embeddings para cada fragmento y mostrará información relevante usando el sistema de logging, incluyendo la metadata y los embeddings asociados a cada documento y fragmento.

## Componentes principales

- **models/document.py**: Modelo de datos para representar un documento, con soporte para metadata flexible.
- **rag/loaders/base_loader.py**: Clase base abstracta para loaders de documentos.
- **rag/loaders/text.py**: Loader que permite la carga de archivos `.txt` y `.pdf`, añadiendo metadata relevante (tipo de archivo, número de página, etc.).
- **rag/splitters/base_splitter.py**: Clase base abstracta para splitters de documentos.
- **rag/splitters/splitter.py**: Splitters concretos, como `CharacterSplitter` y `ParagraphSplitter`, que dividen documentos en fragmentos y enriquecen la metadata de cada fragmento.
- **rag/embeddings/base_embeddings.py**: Clase base abstracta para generadores de embeddings.
- **rag/embeddings/embed.py**: Implementación de ejemplo de un generador de embeddings (`SimpleEmbedding`).
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

## Personalización y extensión

- Puedes extender el sistema añadiendo nuevos loaders para otros formatos de archivo siguiendo la estructura de `BaseLoader`.
- Puedes crear nuevos splitters para diferentes estrategias de fragmentación heredando de `BaseSplitter`.
- Puedes enriquecer la metadata en cualquier punto del pipeline para adaptarla a tus necesidades.
- Puedes implementar nuevos generadores de embeddings heredando de `BaseEmbedding`.

## Ejemplo de uso en código

```python
from rag.loaders.text import TextAndPdfFileLoader
from rag.splitters.splitter import CharacterSplitter
from rag.embeddings.embed import SimpleEmbedding
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

    # Embeddings
    embedder = SimpleEmbedding()
    embeddings = embedder.embed(all_chunks)
    logger.info(f"Embeddings generados para {len(embeddings)} fragmentos")
    for i, emb in enumerate(embeddings[:5]):
        logger.info(f"Embedding {i}: {emb}")

if __name__ == "__main__":
    main()
```

## Dependencias

- [PyPDF2](https://pypi.org/project/PyPDF2/): Para la lectura de archivos PDF.

---

¡Contribuciones y sugerencias son bienvenidas!

