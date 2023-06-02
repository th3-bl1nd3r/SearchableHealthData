from pybloom import BloomFilter
f = BloomFilter(capacity=1000, error_rate=0.001)
[f.add(x) for x in range(99991, 99991 + 1000)]
print(10 in f)
print(99999 in f)
