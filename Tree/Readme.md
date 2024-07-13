> This folder includes binary search tree and its 2 variants

- binary search tree
- avl tree (balanced bst)
- red-black tree (balanced bst)

# Progression from Binary Tree to Advanced Tree Structures

## 1. Binary Tree
> We know a binary tree is a fundamental data structure. It is a tree structure where each node has 0 to 2 children.

## 2. Binary Search Tree (BST)

> A Binary Search Tree (BST) is a binary tree with the following properties:
- For each node ` N `:
  - The value of ` N ` is greater than the values of all nodes in its left subtree.
  - The value of ` N ` is less than the values of all nodes in its right subtree.

### Operations of Binary Search Tree

- search(num) 
  - O(logn) self-balanced 
  - O(n^2) not self-balanced
- insert(num) O(logn)
  - O(logn) self-balanced 
  - O(n^2) not self-balanced

## 3. B-Tree
> The problem of BST is it's not self-balanced, which brings some performance issue when the tree is skewed. That's why we bring up B-Tree which is just a self-balanced binary search tree

- B-trees of order L=3 (like we used today) are also called a 2-3-4 tree or a 2-4 tree. 
“2-3-4” refers to the number of children that a node can have, e.g. a 2-3-4 tree node may have 2, 3, or 4 children.
- B-trees of order L=2 are also called a 2-3 tree.

> real-world usage

File System:
- BTRFS



## 4. Red-Black Tree
> B-Tree is good, but it's hard to implement, so that's why we have red-black tree



> real-world usage

File System:
- EXT

