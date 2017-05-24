"""Add anything to a list"""
from functools import singledispatch


@singledispatch
def hyperextend(item, l):
    """Append the item by default"""
    l.append(item)


@hyperextend.register(list)
@hyperextend.register(tuple)
def _(item, l):
    """Extend a list with other iterables"""
    l.extend(item)
