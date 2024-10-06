class BST:
  class BSTNode:
    def __init__(self, num, cnt=1):
      self.num = num
      self.cnt = cnt
      self.left = None
      self.right = None

  def __init__(self):
    self.root = None

  def insert(self, num):
    """
    @return number of num in the tree
    """
    def helper(node, num):
      if not node:
        return self.BSTNode(num), 1
      elif num > node.num:
        node.right, cnt = helper(node.right, num)
      elif num < node.num:
        node.left, cnt = helper(node.left, num)
      else:
        node.cnt += 1
        return node, node.cnt
      return node, cnt
    
    self.root, cnt = helper(self.root, num)
    return cnt
    
  def search(self, num):
    """
    @return True if num exists in the tree, otherwise, False
    """
    def helper(node, num):
      if not node:
        return False
      elif num > node.num:
        return helper(node.right, num)
      elif num < node.num:
        return helper(node.left, num)
      else:
        return True
    return helper(self.root, num)

  def preorderTraversal(self):
    """
    @return a list of all elements in the tree in preorder 
    """
    res = []
    def helper(node):
      if not node:
        return 
      res.append(node.num)
      helper(node.left)
      helper(node.right)
      return
      
    helper(self.root)
    return res

  def findMax(self):
    '''
      - if node.right is None, return node.val
      - else
        - helper(node.right)
    '''
    def helper(node):
      if not node.right:
        return node.num
      else:
        return helper(node.right)
    return helper(self.root)

  '''
  2
    5
  4   7
    6

  fP(5) -> 4
  fp(7) -> 6
  fp(4) -> 2

  this node doesn't have left child, the prev is its parent
  otherwise, the prev is node.left

  Solution 1:
    - do in order traversal, store the result
    - find the prev element in the result array
    - Time: O(N)
    - Space: O(N)

  Solution 2:
    - record each node's parent using a map (need traverse the tree too)
    - findPrev based on these 2 cases
    - Time: O(N)
    - Space: O(N)

  Solution 3:
    - do this on the fly
    - Time: O(N) worst case

  '''
  def findPrev(self, num):
    stack = []
    cur = self.root
    prev = None
    res = [-1]
    while cur or stack:
      while cur:
        stack.append(cur)
        cur = cur.left
      cur = stack.pop()
      if cur.num == num:
        return res[-1]
      res.append(cur.num)
      cur = cur.right
  