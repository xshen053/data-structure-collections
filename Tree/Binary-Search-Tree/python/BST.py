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
        return helper(node.right)
      elif num < node.num:
        return helper(node.left)
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

