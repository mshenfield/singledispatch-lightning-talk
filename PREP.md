# Jokes
"Can't teach an old dog new tricks"

Classes for the masses

Functions for the munchkins

Missing abstraction

Something Bad - https://iplegalforum.files.wordpress.com/2015/06/jared-dunn.gif

Ice T Unfrozen -  https://media.giphy.com/media/aMs88eUcW8Kic/giphy.gif

Groovy Arnold - https://s-media-cache-ak0.pinimg.com/originals/35/46/d6/3546d6be8ee96bbcedaebb61954ee294.gif

Criteria for abstraction
* doesn't exist in Python core
* requires different handling per class
* I can apply to at least one existing library class


```python

@dispatched()
def keys(d):
  return d.keys()

def is_three():
  return sys.version_info >= (3, 0)

def is_two():
  return (2, 0) <= sys.version_info < (3, 0)

@keys(is_three)
def _(d):
  return d.keys()

@keys(is_two)
def _(d):
  return d.iterkeys()
```

```python
import collections
from functools import singledispatch

@singledispatch
def flatten(item, **kwargs):
  """Flatten just returns the item by default"""
  return item

@flatten.register(dict)
def _flatten_dict(d, parent_key=''):
  items = []
  for key, value in d.items():
    if parent_key:
      new_key = '{parent_key}.{key}'.format(parent_key=parent_key, key=key)
    else:
      new_key = key
    result = flatten(v, parent_key=new_key)

    if isinstance(result, dict):
      items.extend(result.items())
    else:
      items.append((new_key, result))

  return dict(items)

@flatten.register(list)
@flatten.register(tuple)
def _flatten_list(l, **kwargs):
  items = []
  for i in l:
    result = flatten(i)
    if isinstance(result, list):
      items.extend(result)
    else:
      items.append(result)
  return items

example = {
  'g': {'et': {'d': ['o', ['w', ['n']]]}},
  'b': ['hu', 'm', {'b': {'l': 'e'}}]
}
```
