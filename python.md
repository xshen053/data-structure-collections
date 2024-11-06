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

```Python
stack = []
stack.append(1)    # Push 1 onto the stack
stack.append(2)    # Push 2 onto the stack
print(stack.pop()) # Pop (removes and returns 2)
print(stack.pop()) # Pop (removes and returns 1)
```

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
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)

# Iterating Over a Set
my_set = {1, 2, 3, 4, 5}
for element in my_set:
    print(element)
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

## Sort

```Python
# Example: Sort a list of tuples by the second element
data = [(1, 'banana'), (3, 'apple'), (2, 'cherry')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data) # Output: [(3, 'apple'), (1, 'banana'), (2, 'cherry')]

# sort with a custom key
data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}]
data.sort(key=lambda x: x['age'])
print(data)

# sort in descending order
numbers = [4, 1, 3, 2]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)

# Custom Sort with Multiple Criteria
# Example: Sort by age, then by name alphabetically
data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 20}]
data.sort(key=lambda x: (x['age'], x['name']))
print(data)

# custom sort
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age  # Sort by age

people = [Person('Alice', 25), Person('Bob', 20)]
sorted_people = sorted(people)
for person in sorted_people:
    print(person.name, person.age)
'''
Output
- Bob 20
- Alice 25
'''
```

# 数据规模和时间复杂度的关系

| 数据规模 | 时间复杂度 | 算法举例                              |
| -------- | ---------- | ------------------------------------- |
| 10       | O(n!)      | 排列 permutation                      |
| 20-30    | O(2^n)     | 组合 combination                      |
| 50       | O(n^4)     | DFS 搜索, DP 动态规划                 |
| 100      | O(n^3)     | 任意两点最短路径, DP 动态规划         |
| 1000     | O(n^2)     | 稠密图, DP 动态规划                   |
| 10^6     | O(n log n) | 排序, 堆, 递归与分治                  |
| 10^7     | O(n)       | DP 动态规划, 图遍历, 拓扑排序, 树遍历 |
| 10^9     | O(sqrt(n)) | 质数数, 求平方根                      |
| 10^10    | O(log n)   | 二分搜索                              |
| +inf     | O(1)       | 数学相关算法                          |
