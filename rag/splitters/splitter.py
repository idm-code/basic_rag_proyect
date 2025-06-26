from typing import List
from models.document import Document
from rag.splitters.base_splitter import BaseSplitter


class CharacterSplitter(BaseSplitter):
    def __init__(self, chunk_size: int = 1000, overlap: int = 0):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, document: Document) -> List[Document]:
        content = document.content
        chunks = []
        start = 0
        idx = 0
        while start < len(content):
            end = min(start + self.chunk_size, len(content))
            chunk_content = content[start:end]
            chunk_source = f"{document.source} [chars {start}:{end}]"
            metadata = dict(document.metadata)
            metadata.update({"chunk_index": idx, "char_start": start, "char_end": end})
            chunks.append(Document(chunk_content, chunk_source, metadata))
            start += self.chunk_size - self.overlap if self.chunk_size > self.overlap else self.chunk_size
            idx += 1
        return chunks

class ParagraphSplitter(BaseSplitter):
    def split(self, document: Document) -> List[Document]:
        paragraphs = [p for p in document.content.split('\n\n') if p.strip()]
        result = []
        for i, p in enumerate(paragraphs):
            metadata = dict(document.metadata)
            metadata.update({"paragraph_index": i})
            result.append(Document(p, f"{document.source} [paragraph {i}]", metadata))
        return result