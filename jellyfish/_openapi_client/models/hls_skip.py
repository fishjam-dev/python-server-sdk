from enum import Enum


class HlsSkip(str, Enum):
    YES = "YES"

    def __str__(self) -> str:
        return str(self.value)
