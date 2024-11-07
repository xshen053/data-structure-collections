# 按 data structure 分类

## Table of Contents

- [Topic 1: Arrays & Strings](#topic-1-arrays--strings)
- [Topic 2: Lists](#topic-2-lists)
- [Topic 3: Stacks & Queues](#topic-3-stacks--queues)
- [Topic 4: Hash & Maps](#topic-4-hash--maps)
- [Topic 5: Sorting Algorithms](#topic-5-sorting-algorithms)
- [Topic 6: Trees](#topic-6-trees)
- [Topic 7: Graphs (BFS & DFS)](#Graph)
- [Topic 8: Recursion](#topic-8-recursion)

# Lists

ll + math

- 2. Add Two Numbers

ll + other ds

- [lc 146. LRU Cache](https://leetcode.com/problems/lru-cache/)

ll + adjust pointers

- [lc 92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)
- [lc 203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)
- [lc 1669. Merge In Between Linked Lists](https://leetcode.com/problems/merge-in-between-linked-lists/)

ll + find mid, kth + reverse

- [lc 25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/description/)
- [lc 143. Reorder List](https://leetcode.com/problems/reorder-list/)
- [lc 19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

ll + recursion

- [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [430. Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)

# Stacks & Queues

Codepath:

- [lc 224. Basic Calculator](https://leetcode.com/problems/basic-calculator/)
- [lc 735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)
- [lc 946. Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/)
- [lc 232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
- [lc 933. Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/)

queue （抽象）

- [1823. Find the Winner of the Circular Game](https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/)

> 这题为什么用 queue

- 我们访问这些元素的顺序是按照 queue 的顺序访问的，然后我们想要维持它们的 order，先进先出

## priority queue

same pattern

> managing frequencies and reducing counts in a way that maintains a specific structure

- [358. Rearrange String k Distance Apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/)
- [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/)
- [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
- [767. Reorganize String](https://leetcode.com/problems/reorganize-string/)
- [1054. Distant Barcodes](https://leetcode.com/problems/distant-barcodes/)
- [1647. Minimum Deletions to Make Character Frequencies Unique](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/)
- [2182. Construct String With Repeat Limit](https://leetcode.com/problems/construct-string-with-repeat-limit/)
- [2914. Minimum Number of Changes to Make Binary String Beautiful](https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/)
- [amazon: getMinimumFruit](https://github.com/xshen053/OA/blob/main/amazon/intern/GetMininumFruit.py)

# Trees

Codepath:

Warmup Problems
Invert Binary Tree
Symmetric tree
Balanced Binary Tree

所有这些题都是 dfs 的，懂了 dfs，就很好办

bst + binary search

- [lc 108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

bfs

- [lc 515. Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/)

dfs + recursion (classic)

- [lc 111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
- [lc 814. Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/)

dfs + sorting

- [lc 987. Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)

dfs + global max

- [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- [508. Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum/)

# Graph

## Graph Traversals

Codepath:

- [lc 690. Employee Importance](https://leetcode.com/problems/employee-importance/)
- [lc 130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)
- [lc 787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
- [lc 994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
- [lc 542. 01 Matrix](https://leetcode.com/problems/01-matrix/)
- [lc 733. Flood Fill](https://leetcode.com/problems/flood-fill/)
- [lc 79. Word Search](https://leetcode.com/problems/word-search/)
- [lc 997. Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)

## Graph Representations

Codepath:

- [lc 547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/)
- [lc 133. Clone Graph](https://leetcode.com/problems/clone-graph/)
- [lc 841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)

## Graphs: Algorithms (Unit 7)
