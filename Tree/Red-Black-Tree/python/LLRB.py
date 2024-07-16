import collections
class LLRB:
  class LLRBNode:
    def __init__(self, isBlack, item, left = None, right = None):
      self.isBlack = isBlack
      self.item = item
      self.left = left
      self.right = right
  
  def __init__(self, root = None):
    self.root = root
  
  def flipColors(self, node):
    self.__flipColor(node)
    self.__flipColor(node.left)
    self.__flipColor(node.right)

  def rotateLeft(self, node) -> LLRBNode:
    """
    @precondition: node.right is not None
    @return: root of new subtree after rotation
    we need to swap color of new and old nodes, not **flip** them
    """
    newRoot = node.right
    node.right = newRoot.left
    newRoot.left = node
    newRoot.isBlack, node.isBlack = node.isBlack, newRoot.isBlack
    return newRoot

  def rotateRight(self, node) -> LLRBNode:
    """
    @precondition: node.left is not None
    @return: root of new subtree after rotation
    we need to swap color of new and old nodes, not **flip** them
    """
    newRoot = node.left
    node.left = newRoot.right
    newRoot.right = node
    newRoot.isBlack, node.isBlack = node.isBlack, newRoot.isBlack
    return newRoot
  
  def insert(self, item):   
    self.root = self.__insert(self.root, item)
    self.root.isBlack = True
    return self.root


    

  def isRed(self, node):
    return node is not None and node.isBlack == False
  
  # Helper functions
  def __flipColor(self, node):
    """
    flip color of given node
    """
    node.isBlack = not node.isBlack  

  def __debugPrintTree(self):
    """
    inorder traversal to print tree
    """
    res = []
    def helper(node):
      if not node:
        return
      helper(node.left)
      res.append(node.item)
      helper(node.right)
      return res
    helper(self.root)

  def __debugLevelOrderPrint(self):
    """
    Level order traversal
    """
    if not self.root:
      return  
    queue = collections.deque()
    queue.append(self.root)
    while queue:
      size = len(queue)
      t = []
      for _ in range(size):
        node = queue.popleft()
        t.append(node.item)
        if self.isRed(node):
          t.append("red")
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)

  def __insert(self, node, item):
    """
    insert item into a red black tree rooted as node
    """
    if not node:
      return self.LLRBNode(False, item)

    if item == node.item:
      return node
    elif item < node.item:
      node.left = self.__insert(node.left, item)
    else:
      node.right = self.__insert(node.right, item)
      
    # so far, we finished the insertion of a bst
    # now we need to make sure it is balanced

    # Fix any right-leaning links
    if self.isRed(node.right) and not self.isRed(node.left):
        node = self.rotateLeft(node)

    # Fix any consecutive red links on the left
    if self.isRed(node.left) and self.isRed(node.left.left):
        node = self.rotateRight(node)        

    # flip colors
    if not self.isRed(node) and self.isRed(node.left) and self.isRed(node.right):
      self.flipColors(node)      
    
    return node
