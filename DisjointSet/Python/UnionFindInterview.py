"""
2024 @ Copyright Xiaxi Shen
"""
class UnionFind:
  def __init__(self, N):
    self.data = {}
    for i in range(N):
      self.data[i] = -1

  def sizeOf(self, v):
    """
    Returns the size of the set V belongs to
    """
    return -self.data[self.find(v)]
  
  def connected(self, v1, v2):
    """
    Returns true if nodes/vertices V1 and V2 are connected
    """
    r1 = self.find(v1)
    r2 = self.find(v2)
    return r1 == r2

  def find(self, v):
    if self.data[v] < 0:
      return v
    self.data[v] = self.find(self.data[v])
    return self.data[v]

  def union(self, v1, v2):
    rootV1 = self.find(v1)
    rootV2 = self.find(v2)
    size1 = self.sizeOf(v1)
    if rootV1 != rootV2:
      self.data[rootV1] = rootV2
      self.data[rootV2] -= size1

  """
  Optional: weighted quick union
  def union(self, v1, v2):
    \"""
    Key Operation 2
    Connects two items V1 and V2 together by connecting their respective
    sets. V1 and V2 can be any element, and a union-by-size heuristic is
    used. If the sizes of the sets are equal, tie break by connecting V1's
    root to V2's root. Union-ing a item with itself or items that are
    already connected should not change the structure.
    \"""
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
  """
