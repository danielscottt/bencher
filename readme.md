Bencher
=======

Benchmark some stuff if you want.

These tests:
```python
from bencher import Bencher
Bencher.limit = 10000

@Bencher
def with_while(i):
    while i < 1024:
        i = i**2

@Bencher
def with_reduce(i):
    reduce(lambda x, y: y**2, range(i, int(math.sqrt(1024)+1)))

if __name__ == '__main__':
    with_while(2)
    with_reduce(2)
```

Produces this output:
```
with_while:
  total exec time:      4ms
  avg op time:          0μs
  high op (seq 2404):   114μs
  low op (seq 4):       0μs
with_reduce:
  total exec time:      36ms
  avg op time:          3μs
  high op (seq 1588):   277μs
  low op (seq 3):       2μs
```
