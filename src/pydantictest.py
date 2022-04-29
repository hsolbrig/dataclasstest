from dataclasses import dataclass, field
from typing import List

import pydantic.dataclasses as pydc


@dataclass
class PyFoo:
    a: int
    b: int = 0
    c: List[int] = field(default_factory=list)
    d: int = 1


x = PyFoo(1, 2, d=17)
print(x)

WrappedPyFoo = pydc.dataclass(PyFoo)

y = WrappedPyFoo(2,3,d=18)
print(y)
