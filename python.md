- [Topic 1: Arrays & Strings](#topic-1-arrays--strings)
- [Topic 2: Lists](#topic-2-lists)
- [Topic 3: Stacks & Queues](#topic-3-stacks--queues)
- [Topic 4: Hash & Maps](#topic-4-hash--maps)
- [Topic 5: Sorting Algorithms](#topic-5-sorting-algorithms)
- [Topic 6: Trees](#topic-6-trees)
- [Topic 7: Graphs (BFS & DFS)](#Graph)
- [Topic 8: Recursion](#topic-8-recursion)

# python coding 指南

https://interview-cheatsheet.streamlit.app/data_structures

https://interview-cheatsheet.streamlit.app/build_in_functions

# python 各个数据结构复习，要点

## stacks

## queue

```Python
from queue import Queue

q = Queue()
q.put(1)      # Add item to the queue
q.put(2)
print(q.get())  # Remove and return the first item (1)
print(q.get())  # Remove and return the next item (2)

from collections import deque

# OR
q = deque()
q.append(1)       # Add item to the end of the queue
q.append(2)
print(q.popleft())  # Remove and return the first item (1)
print(q.popleft())  # Remove and return the next item (2)
```

## hash table

```Python
# Dictionary with hashable keys
my_dict = {"apple": 1, "banana": 2}
print(my_dict["apple"])  # Accessing via hash of "apple"

# Set with hashable elements
my_set = {"apple", "banana", "cherry"}
print("banana" in my_set)  # Uses hash of "banana" for fast lookup

# iterate dict


#
```

## heap

```Python
'''
	•	heapq.heapify(list): Convert a list into a heap in-place.
	•	heapq.heappush(heap, item): Add an item to the heap.
	•	heapq.heappop(heap): Remove and return the smallest item.
	•	heapq.heapreplace(heap, item): Pop the smallest item, then push a new item.
	•	heapq.heappushpop(heap, item): Push a new item, then pop the smallest item.
'''
import heapq

heap = [3, 1, 4, 1, 5]
heapq.heapify(heap)  # Converts the list into a min-heap in-place
print(heap)  # Output will be in heap order, e.g., [1, 1, 4, 3, 5]

# Pass custom comparator
# lc 692. Top K Frequent Words as an example
class Word:
    def __init__(self, key, freq):
        self._key = key
        self._freq = freq
    def __lt__(self, other):
      '''
        @return True if self should be considered “less than” other.
      '''
        if self._freq == other._freq:
            return self._key > other._key
        else:
            return self._freq < other._freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq_hash_map = Counter(words)
        min_heap = []
        for word, freq in word_freq_hash_map.items():
            heapq.heappush(min_heap, Word(word, freq))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        min_heap.sort(reverse=True)
        return [item._key for item in min_heap]


```

- how ds are represented in python?

- custom comparator?

  - create a class to compare

- sort?
  - use lambda?

# 数据规模和时间复杂度的关系
