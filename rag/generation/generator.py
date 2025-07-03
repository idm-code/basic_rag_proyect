from typing import List, Any
from rag.generation.base_generator import BaseGenerator

class SimpleGenerator(BaseGenerator):
    def generate(self, query: str, contexts: List[Any]) -> str:
        context_text = "\n".join([c.content for c in contexts])
        return f"Pregunta: {query}\n\nContexto relevante:\n{context_text}\n\nRespuesta simulada basada en el contexto."