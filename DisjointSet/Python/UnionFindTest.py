import unittest
from UnionFind import UnionFind

class TestUnionFind(unittest.TestCase):
    def setUp(self):
      self.uf = None
    
    def test1(self):
      """
      Test if the initial state of the disjoint sets are correct
      """
      self.uf = UnionFind(4)
      self.assertFalse(self.uf.connected(0, 1))
      self.assertFalse(self.uf.connected(0, 2))
      self.assertFalse(self.uf.connected(0, 3))
      self.assertFalse(self.uf.connected(1, 2))
      self.assertFalse(self.uf.connected(1, 3))
      self.assertFalse(self.uf.connected(2, 3))
      # we union then
      self.uf.union(0, 1)
      self.uf.union(2, 3)
      self.uf.union(0, 2)
      # 
      self.assertTrue(self.uf.connected(0, 1))
      self.assertTrue(self.uf.connected(0, 2))
      self.assertTrue(self.uf.connected(0, 3))
      self.assertTrue(self.uf.connected(1, 2))
      self.assertTrue(self.uf.connected(1, 3))
      self.assertTrue(self.uf.connected(2, 3))
      self.uf.print()

    def test3(self):
      """
      Test the union-find operations and connections
      """
      self.uf = UnionFind(10)
      self.uf.union(0, 1)
      self.assertEqual(self.uf.find(0), self.uf.find(1))
      self.uf.union(2, 3)
      self.assertEqual(self.uf.find(2), self.uf.find(3))
      self.uf.union(0, 2)
      self.assertEqual(self.uf.find(1), self.uf.find(3))

      self.uf.union(4, 5)
      self.uf.union(6, 7)
      self.uf.union(8, 9)
      self.uf.union(4, 8)
      self.uf.union(4, 6)

      self.assertEqual(self.uf.find(5), self.uf.find(9))
      self.assertEqual(self.uf.find(7), self.uf.find(9))
      self.assertEqual(self.uf.find(8), self.uf.find(9))

      self.uf.union(9, 2)
      self.assertEqual(self.uf.find(3), self.uf.find(9))
      
    def test4(self):
      self.uf = UnionFind(4)
      self.uf.union(1, 1)
      for i in range(4):
         self.assertEqual(self.uf.find(i), i)
       

if __name__ == '__main__':
    unittest.main()
