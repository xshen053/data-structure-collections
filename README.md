# Data-structure-collections

This repo includes various common abstract data structures (ADT) and their implementation details using Java / Python.

# Difference between abstract data type and data structure

- ADT: Describes the operations and properties (e.g., each node's left subtree contains only nodes with keys less than the node's key).
- Data Structure: Only describe the structure (don't think about operations and properties),
  - e.g. binary tree is a structure where each node points to left and right children

## Data structure

- Array: a linear data structure - elements are stored at a contiguous location
- Linked List: a linear data structure - elements are not stored at a contiguous location
- Binary Tree: a tree data structure in which each node has at most two children, referred to as the left child and the right child
- Graph: a collection of nodes connected by edges
- Hash Table: A data structure that uses a hash function to map keys to values (consider it as an array with a mechanism for efficient key-based access)

## Abstract Data Type

- List
- Stack
  - Monotonic stack
- Queue
  - Monotonic queue
- Tree
  - Binary Search Tree
  - AVL Tree
  - Red-Black Tree
- Map
  - Hash Map
  - Tree Map
- Graph
- Heaps and Priority Queue
- Disjoint Sets

## Algorithms

- Sorting
- Greedy
- BFS
- DFS
- Dynamic Programming

## 按照数据需求分类

> input 对顺序无要求

- list
- set / map

> input 顺序无要求，但需要考虑组合排列问题

- set / map （把 set 看成袋子，里面拿球）

> 当需要维护 input 的 order，比如 increasing，decreasing

- heap (priority queue)
  - insert O(logn)
  - delete O(n)
- ordereddict / orderedset （python 特有）
  - insert O(logn)
  - delete O(logn)
- treeset / treemap
  - insert O(logn)
  - delete O(logn)
