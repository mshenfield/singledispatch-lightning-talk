"""Flatten anything"""
from functools import singledispatch
from hyperextend import hyperextend


@singledispatch
def raze(item):
    """Just returns the item by default"""
    return item


@raze.register(dict)
def _(d):
    items = []
    for item in d.items():
        hyperextend(raze(item), item)
    return items


@raze.register(list)  # noqa
@raze.register(tuple)
def _(l, **kwargs):
    items = []
    for item in l:
        result = raze(item)
        hyperextend(result, items)
    return items
