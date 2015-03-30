#!/usr/bin/python
import collections
cnt = collections.Counter()
colors = ['red', 'blue', 'green', 'yellow', 'red', 'green', 'blue', 'blue', 'yellow', 'red']
for words in colors:
    cnt[words] += 1
print cnt
