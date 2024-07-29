"""
2024 @ Copyright Xiaxi Shen
"""
class UnionFind:
  def __init__(self, N):
    self.data = [-1] * N

  def sizeOf(self, v):
    """
    Returns the size of the set V belongs to
    """
    return -self.parent(self.find(v))

  def parent(self, v):
    """
    Returns the parent of V. If V is the root of a tree, returns the
    negative size of the tree for which V is the root. 
    """
    if v < 0 or v >= len(self.data):
      raise ValueError("Please give an valid value")
    return self.data[v] 

  def connected(self, v1, v2):
    """
    Returns true if nodes/vertices V1 and V2 are connected
    """
    r1 = self.find(v1)
    r2 = self.find(v2)
    return r1 == r2

  def find(self, v):
    """
    Key Opeation 1
    Returns the root of the set V belongs to. 
    Path-compression is employed allowing for fast search-time. 
    If invalid items are passed into this function, 
    throw an ValueError.
    """
    if v < 0 or v >= len(self.data):
      raise ValueError("Please give an valid value")
    cur = v
    while self.parent(cur) > 0:
      cur = self.data[cur]
    root = cur

    # Path Compression
    cur = v
    while self.parent(cur) > 0:
      temp = self.data[cur]
      self.data[cur] = root
      cur = temp
    return root

  def union(self, v1, v2):
    """
    Key Operation 2
    Connects two items V1 and V2 together by connecting their respective
    sets. V1 and V2 can be any element, and a union-by-size heuristic is
    used. If the sizes of the sets are equal, tie break by connecting V1's
    root to V2's root. Union-ing a item with itself or items that are
    already connected should not change the structure.
    """
    r1 = self.find(v1)
    r2 = self.find(v2)
    size1 = self.sizeOf(v1)
    size2 = self.sizeOf(v2)
    if r1 != r2:
      if size1 == size2:
        self.data[r1] = r2
        self.data[r2] -= size1
      elif size1 > size2:
        self.data[r2] = r1
        self.data[r1] -= size2
      else:
        self.data[r1] = r2
        self.data[r2] -= size1

  def print(self):
    print(self.data)
