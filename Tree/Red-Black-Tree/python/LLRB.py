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
    no need to change its parent here
    """
    newRoot = node.right
    node.right = newRoot.left
    newRoot.left = node
    self.__flipColor(newRoot)
    self.__flipColor(newRoot.left)
    return newRoot

  def rotateRight(self, node) -> LLRBNode:
    """
    @precondition: node.left is not None
    @return: root of new subtree after rotation
    no need to change its parent here
    """
    pass  
  
  def insert(self, node):
    pass

  def isRed(self, node):
    return node is not None and node.isBlack == False
  
  # Helper functions
  def __flipColor(self, node):
    """
    flip color of given node
    """
    node.isBlack = not node.isBlack  
