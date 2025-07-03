from typing import List, Any

class BaseGenerator:
    def generate(self, query: str, contexts: List[Any]) -> str:
        raise NotImplementedError("Implement in subclasses.")