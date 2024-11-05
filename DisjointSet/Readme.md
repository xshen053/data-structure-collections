# Disjoint Sets

The disjoint sets data structure represents a collection of sets that are disjoint, meaning that any item in this data structure is found in no more than one set.

## Operations

> There are 2 main operations

- Union: Combine 2 sets into 1 set
- Find: take in an item, and tell us which set that item belongs to

### Optimization

#### weighted quick union

make the smaller tree a subtree of the larger one, breaking ties arbitrarily

#### Path compression

move the leaf up the tree so it becomes a direct child of the root

# Reference

[UCB CS 61 Lab 06](https://fa23.datastructur.es/materials/lab/lab06/)
