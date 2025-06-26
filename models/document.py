from typing import Optional, Dict, Any

class Document:
    def __init__(self, content: str, source: str, metadata: Optional[Dict[str, Any]] = None):
        self.content = content
        self.source = source
        self.metadata = metadata or {}