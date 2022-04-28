from typing import Any, Union


class RCItem:
    def __init__(self, v: Union[Any, "RCItem"]) -> None:
        if isinstance(v, RCItem):
            self._r = v._r
            self._c = v._c
        else:
            self._r = self._c = None
        super().__init__()

    def yaml_loc(self) -> str:
        return f"row={self._r} col={self._c}: {self}" if self._r else repr(self)


class AnnotatedStr(str, RCItem):
    pass


i1 = AnnotatedStr("test")
print(str(i1))
print(i1.yaml_loc())
i1._r = 1
i1._c = 2
print(str(i1))
print(i1.yaml_loc())
