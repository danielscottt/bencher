Bencher
=======

Benchmark some stuff if you want.

```python
from bench import Bencher
Bencher.limit = 10000
 
@Bencher
def a_method(i):
    while i < 1024:
        i = i**2
 
if __name__ == '__main__':
    a_method(2)
```
