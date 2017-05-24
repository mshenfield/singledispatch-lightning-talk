"""Update with superpowers"""
from functools import singledispatch


@singledispatch
def hupdate(value, d, key=None):
    """Set d[key] to value by default"""
    d[key] = value


@hupdate.register(dict)
def _(value, d, key=None):
    """Update the dict if the value is a dictionary, ignoring key"""
    d.update(value)
