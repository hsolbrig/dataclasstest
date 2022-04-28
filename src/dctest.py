import pydantic.dataclasses as pydc
import dataclasses
from typing import List, Dict, Any, Optional

from src.rcitem import RCItem, AnnotatedStr

# loc_fn = dataclasses._create_fn
#
#
# def dc_create_fn(name, args, body, *posargs, **kwargs):
#     if name == '__init__':
#         if dataclasses._POST_INIT_NAME in body[-1]:
#             pi_parms = body[-1].rsplit(')', 1)[0]
#             body[-1] = pi_parms + ('' if pi_parms[-1] == '(' else ',') + ' **kwargs)'
#         return loc_fn(name, list(args) + ["**kwargs"], body, *posargs, **kwargs)
#     else:
#         return loc_fn(name, args, body, *posargs, **kwargs)
#
#
# dataclasses._create_fn = dc_create_fn


@dataclasses.dataclass
class Foo2:
    i: int
    j: str = "None"
    l: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        for k, v in kwargs.items():
            print(f"Unrecognized argument: {k}=<{v.yaml_loc() if isinstance(v, RCItem) else v}>")

Foo = pydc.dataclass(Foo2)

print(Foo(10, "test1"))
print(Foo(11))
print(Foo(i=12, j="foo"))
print(Foo(i=12, j="bar", k="typo"))
kloc = AnnotatedStr("another_k")
kloc._r = 10
kloc._c = 12
print(Foo(i=13, j="kale", k = kloc))
