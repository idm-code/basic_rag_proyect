# RAG Project

Este proyecto implementa un sistema modular para la carga y división de documentos en un flujo RAG (Retrieval-Augmented Generation), permitiendo la lectura eficiente de archivos `.txt` y `.pdf`, así como su fragmentación óptima para procesamiento posterior.

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

Esto cargará los documentos desde la ruta especificada en `main.py`, los dividirá en fragmentos usando el splitter configurado y mostrará información relevante usando el sistema de logging.

## Componentes principales

- **rag/loaders/base_loader.py**: Clase base abstracta para loaders de documentos.
- **rag/loaders/text.py**: Loader que permite la carga de archivos `.txt` y `.pdf`.
- **rag/splitters/base_splitter.py**: Clase base abstracta para splitters de documentos.
- **rag/splitters/splitter.py**: Splitters concretos, como `CharacterSplitter` y `ParagraphSplitter`, para dividir documentos en fragmentos.
- **models/document.py**: Modelo de datos para representar un documento.
- **utils/logger.py**: Configuración centralizada del logger para el proyecto.
- **resources/**: Carpeta sugerida para almacenar los documentos a cargar.

## Personalización y extensión

- Puedes extender el sistema añadiendo nuevos loaders para otros formatos de archivo siguiendo la estructura de `BaseLoader`.
- Puedes crear nuevos splitters para diferentes estrategias de fragmentación heredando de `BaseSplitter`.

## Ejemplo de uso en código

```python
from rag.loaders.text import TextAndPdfFileLoader
from rag.splitters.splitter import CharacterSplitter
from utils.logger import get_logger

def main():
    logger = get_logger()
    loader = TextAndPdfFileLoader()
    docs = loader.load("resources/")
    splitter = CharacterSplitter(chunk_size=1000, overlap=100)
    all_chunks = []
    for doc in docs:
        chunks = splitter.split(doc)
        all_chunks.extend(chunks)
        logger.info(f"Documento {doc.source} dividido en {len(chunks)} fragmentos")
    logger.info(f"Total de fragmentos generados: {len(all_chunks)}")

if __name__ == "__main__":
    main()
```

## Dependencias

- [PyPDF2](https://pypi.org/project/PyPDF2/): Para la lectura de archivos PDF.

---

¡Contribuciones y sugerencias son bienvenidas!

