from typing import Any

class BaseIndexer:
    def index(self, *args, **kwargs) -> Any:
        raise NotImplementedError("Implement in subclasses.")