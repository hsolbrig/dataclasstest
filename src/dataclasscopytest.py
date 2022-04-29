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

# Without the fix, this fails with:
# Traceback (most recent call last):
#   File "/Users/hsolbrig/git/hsolbrig/dataclasstest/src/dataclasscopytest.py", line 24, in <module>
#     Copy2 = dataclass(Orig2)
#   File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/dataclasses.py", line 1024, in dataclass
#     return wrap(cls)
#   File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/dataclasses.py", line 1016, in wrap
#     return _process_class(cls, init, repr, eq, order, unsafe_hash, frozen)
#   File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/dataclasses.py", line 930, in _process_class
#     _init_fn(flds,
#   File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/dataclasses.py", line 504, in _init_fn
#     raise TypeError(f'non-default argument {f.name!r} '
# TypeError: non-default argument 'c' follows default argument

# IF we change the following:
# lines 961 through 975 from the python 3.10
#            # field) exists and is of type 'Field', replace it with the
#         # real default.  This is so that normal class introspection
#         # sees a real default value, not a Field.
#         if isinstance(getattr(cls, f.name, None), Field):
#             if f.default is MISSING ---> and f.default_factory is MISSING <-- :
#                 # If there's no default, delete the class attribute.
#                 # This happens if we specify field(repr=False), for
#                 # example (that is, we specified a field object, but
#                 # no default value).  Also if we're using a default
#                 # factory.  The class attribute should not be set at
#                 # all in the post-processed class.
#                 delattr(cls, f.name)
#             else:
#                 setattr(cls, f.name, f.default --> if f.default is not MISSING else f.default_factory <--)
#
Copy2 = dataclass(Orig2)
x1 = Copy2(1)
print(x1)
x2 = Copy2(1, 12)
print(x2)
x3 = Copy2(1, c=[1,2,3])
print(x3)
