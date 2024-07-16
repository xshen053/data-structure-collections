import unittest
from LLRB import LLRB

# class TestLLRBBstProperty(unittest.TestCase):
#     def setUp(self):
#       self.llrb = LLRB()

#     def test_insert(self):
#       self.assertEqual(self.llrb.insert(5), 1)
#       self.assertEqual(self.llrb.insert(5), 2)
#       self.assertEqual(self.llrb.insert(5), 3)
#       self.assertEqual(self.llrb.insert(4), 1)
#       self.assertEqual(self.llrb.insert(5), 4)

#     def test_search(self):
#       self.assertTrue(self.llrb.search(5))
#       self.llrb.insert(5)
#       self.assertTrue(self.llrb.search(5))
#       self.assertTrue(self.llrb.search(6))
#       self.llrb.insert(6)
#       self.assertTrue(self.llrb.search(6))
  
#     def test_preorderTraversal(self):
#         self.llrb.insert(5)
#         self.llrb.insert(3)
#         self.llrb.insert(7)
#         self.llrb.insert(2)
#         self.llrb.insert(4)
#         self.llrb.insert(6)
#         self.llrb.insert(8)
#         self.assertEqual(self.llrb.preorderTraversal(), [5, 3, 2, 4, 7, 6, 8])

class TestLLRBInvariant(unittest.TestCase):
    def setUp(self):
      self.llrb = LLRB()

    def test_is_red(self):
      self.assertEqual(self.llrb.root, None)
      node1 = self.llrb.LLRBNode(True, 10)
      node2 = self.llrb.LLRBNode(False, 9)
      node3 = self.llrb.LLRBNode(False, 8)
      self.assertFalse(self.llrb.isRed(node1))
      self.assertFalse(self.llrb.isRed(self.llrb.root)) # None node is black
      self.assertTrue(self.llrb.isRed(node2))
      self.assertTrue(self.llrb.isRed(node3))

    def test_rotate_left_case1(self):
      self.assertEqual(self.llrb.root, None)      
      node1 = self.llrb.LLRBNode(True, 10)
      node2 = self.llrb.LLRBNode(False, 9)
      node1.right = node2

      newRoot = self.llrb.rotateLeft(node1)
      self.assertEqual(newRoot.item, 9)
      self.assertEqual(newRoot.left.item, 10)
      self.assertFalse(self.llrb.isRed(newRoot))
      self.assertTrue(self.llrb.isRed(newRoot.left))


    # def test_rotate_right(self):
    #   self.assertEqual(self.llrb.root, None)      
    #   node1 = self.llrb.LLRBNode(True, 10)
    #   node2 = self.llrb.LLRBNode(False, 9)
    #   node3 = self.llrb.LLRBNode(False, 8)
    #   node1.left = node2
    #   node1.right = node3

    #   newRoot = self.llrb.rotateRight(node1)
    #   self.assertEqual(newRoot.item, 9)
    #   self.assertEqual(newRoot.left.item, 8)
    #   self.assertEqual(newRoot.right.item, 10)

if __name__ == '__main__':
    unittest.main()

