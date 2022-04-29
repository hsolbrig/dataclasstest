from dataclasses import dataclass, field
from typing import List

# A dataclass without a default_factory copies correctly
@dataclass
class Orig1:
    a: int
    b: int = 1
    c: int = 2


Copy1 = dataclass(Orig1)

# A dataclass WITH a default_factory fails
# Note:`b` is required, because `c` is recorded as missing
@dataclass
class Orig2:
    a: int
    b: int = 1
    c: List[int] = field(default_factory=list)

Copy2 = dataclass(Orig2)
