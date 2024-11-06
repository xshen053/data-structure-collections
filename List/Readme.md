- [x] find mid -[ ] find kth node

- reverse list
- recursion
- dummy node, iterate 从 it 还是 dummy?

# find mid

```Python
fast = head
slow = head

# 这里slow是下半linked list的前一个节点，原因是我们要把它.next变成None
while fast and fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next


# 1 2 3 4 5
#   s

# 1 2 3 4
#   s

fast = head
slow = head

# 这里slow就是后半linked list的第一个节点了
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

# 1 2 3 4 5
#     s

# 1 2 3 4
#     s
```
