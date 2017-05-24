"""Flatten anything"""
from functools import singledispatch
from hyperextend import hyperextend
from hupdate import hupdate


@singledispatch
def raze(item, **kwargs):
    """Just returns the item by default"""
    return item


@raze.register(dict)
def _(d, parent_key=''):
    """Flattens dictionaries by grouping nested keys

    e.g. {'a': {'b': {'c': 'd'}}} becomes {'a.b.c': 'd'}
    """
    items = {}
    for key, value in d.items():
        new_key = '{parent_key}.{key}'.format(parent_key=parent_key, key=key) if parent_key else key
        result = raze(value, parent_key=new_key)
        hupdate(result, items, key=new_key)
    return items


@raze.register(list)  # noqa
@raze.register(tuple)
def _(l, **kwargs):
    """Flattens iterables by unwrapping nested iterables

    e.g. [1, [2, (3, 4)] becomes [1, 2, 3, 4]
    """
    items = []
    for i in l:
        result = raze(i)
        hyperextend(result, items)
    return items
