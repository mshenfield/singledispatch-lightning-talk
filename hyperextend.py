"""Safe extend that handles normal values"""
from functools import singledispatch


@singledispatch
def hyperextend(item, l):
    """Append the item by default"""
    l.append(item)


@hyperextend.register(list)
@hyperextend.register(tuple)
@hyperextend.register(dict)
def _(item, l):
    """Extend a list with other iterables"""
    l.extend(item)
