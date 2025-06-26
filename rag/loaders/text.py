import os
from typing import List
from models.document import Document
from rag.loaders.base_loader import BaseLoader

try:
    import PyPDF2
except ImportError:
    PyPDF2 = None

class TextAndPdfFileLoader(BaseLoader):
    def load(self, path: str) -> List[Document]:
        documents = []
        if os.path.isfile(path):
            if path.endswith('.txt'):
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    metadata = {"type": "txt"}
                    documents.append(Document(content, path, metadata))
            elif path.endswith('.pdf') and PyPDF2:
                with open(path, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    for i, page in enumerate(reader.pages):
                        content = page.extract_text() or ""
                        metadata = {"type": "pdf", "page": i + 1}
                        documents.append(Document(content, path, metadata))
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file.endswith('.txt'):
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            metadata = {"type": "txt"}
                            documents.append(Document(content, file_path, metadata))
                    elif file.endswith('.pdf') and PyPDF2:
                        with open(file_path, 'rb') as f:
                            reader = PyPDF2.PdfReader(f)
                            for i, page in enumerate(reader.pages):
                                content = page.extract_text() or ""
                                metadata = {"type": "pdf", "page": i + 1}
                                documents.append(Document(content, file_path, metadata))
        return documents