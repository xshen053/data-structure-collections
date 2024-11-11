# Pattern

- [x] linked list traversal
- [x] find mid
- [x] find kth node
- [x] reverse list
- [x] reverse sub list
- [ ] recursion
- [ ] dummy node, iterate 从 it 还是 dummy?

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

# find kth node

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(-1, head)
        slow = dummy_node
        fast = dummy_node
        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy_node.next
```

# reverse list

```Python
def reverseList(node):
    new_head = None
    it = node
    # loop inv: new_head always point to new head
    while it:
        # save next node
        nxt = it.next
        # point current node to the previous node
        it.next = new_head
        # update new_head to current node
        new_head = it
        # move forward to next node
        it = nxt
    return new_head
```

# reverse sub list

> 我们的 it 从第二个节点开始，因为如果 reverse list 的长度为 1，根本没必要 reverse

这里，

- 对 old_head，每一个 iteration 都要 point 到新的 it 节点（sublist 之后的第一个节点）
- 对于 prev (在 old_head 前面的那个 node)，每个 iteration 都要 point 到最新的 node
- 查看循环不变量

```Python
old_head = prev.next
it = old_head.next

# inv:
# prev.next always points to new head
# old_head.next always points to the first node after reversed list

for _ in range(right - left):
    # point 1st node to 3rd node (because 1st node is the last node in reversed list)
    old_head.next = it.next
    # point 2nd node to previous node (1st)
    it.next = prev.next
    # previous node point to 2nd node
    prev.next = it
    # update it to 3rd node
    it = old_head.next
```
