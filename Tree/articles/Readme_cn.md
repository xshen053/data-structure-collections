# Tree 的故事

Tree 比较常见的

- binary tree
- binary search tree
- red black tree

对于 leetcode tree 的问题，通常比较常见的 pattern

- traversal

虽然我们有 in, pre, post, level order 遍历

但其实 level order 的本质就是 bfs，其他的本质是 dfs

tree 问题最大的特性，考点就是它的 recursive 的特性，一个 tree 的 children 本身又是 tree。所以 tree 问题特别能考察对于理解 recursion 的理解

recursion 和 traversal 的区别就是

- recursion 考虑的是如何把一个 tree 分解成 subtree
- traversal 则是通过遍历一遍 tree，就能找到答案
  - traversal 可以通过递归的 recursion 的方式来做

区分两者我觉得最直接的方法就是，traversal 遍历的问题，可以通过 iteration 解决。
而分解的问题，最直接的方法是通过 recursion 解决。但两者不冲突，一道题可以从 2 种思维方式解决

而对于重复的子问题，就可以用 dp，memo 来优化了，但问题本质还是穷举所有的可能性

## traversal 写法

> 对于 3 种 traversal，我们既可以用 recursion 也可以用 iteration

recursion 非常的直观

```Python
def traverse(node):
  if not node:
    return
  # preorder
  traverse(node.left)
  # inorder
  traverse(node.right)
  # postorder
```

iteration，可以把 preorder 和 postorder 分成一类

```Python
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root

        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

        return res
```

inorder

```Python
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        cur = root
        res = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
```

## 题型分析

> recursion 通过分解思维可以解决的相关题目

- 95. Unique Binary Search Trees II
- 100. Same Tree
- 101. Symmetric Tree
- 104. Maximum Depth of Binary Tree
- 105. Construct Binary Tree from Preorder and Inorder
- 106. Construct Binary Tree from Inorder and Postorder Traversal
  - 需要借助 hash table 维护 index
- 108. Convert Sorted Array to Binary Search Tree
- 109. Convert Sorted List to Binary Search Tree
- 110. Balanced Binary Tree

> BFS

- 102. Binary Tree Level Order Traversal
- 103. Binary Tree Zigzag Level Order Traversal
- 107. Binary Tree Level Order Traversal II
