# RAG Proyect

Este proyecto implementa un sistema modular para la carga de documentos en un flujo RAG (Retrieval-Augmented Generation), permitiendo la lectura eficiente de archivos `.txt` y `.pdf` para su posterior procesamiento.

> **Nota:**  
> Este proyecto irá creciendo exponencialmente, añadiendo todos los pasos de la técnica RAG (Retrieval-Augmented Generation). Por lo tanto, se irá modificando y ampliando periódicamente hasta finalizar el desarrollo completo del sistema.

## Estructura del proyecto

```
main.py
requirements.txt
.gitignore
README.md
rag/loaders/
    base.py
    text.py
models/
    document.py
resources/
    AÑADE AQUI TU FICHERO.PDF
utils/
    logger.py
```

## Instalación

1. Clona el repositorio.
2. Instala las dependencias.

```sh
pip install -r requirements.txt
```

## Uso

Ejecuta el archivo principal:

```sh
python main.py
```

Esto cargará los documentos `.txt` y `.pdf` desde la ruta especificada en `main.py` y mostrará información relevante usando el sistema de logging.

## Componentes principales

- **rag/loaders/base.py**: Clase base abstracta para loaders de documentos.
- **rag/loaders/text.py**: Loader que permite la carga de archivos `.txt` y `.pdf`.
- **models/document.py**: Modelo de datos para representar un documento.
- **utils/logger.py**: Configuración centralizada del logger para el proyecto.
- **resources/**: Carpeta sugerida para almacenar los documentos a cargar.

## Personalización

Puedes extender el sistema añadiendo nuevos loaders para otros formatos de archivo siguiendo la estructura de `BaseLoader`.

