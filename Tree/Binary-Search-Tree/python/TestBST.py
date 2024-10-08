import unittest
from BST import BST

class TestBST(unittest.TestCase):
    def setUp(self):
      self.bst = BST()

    def test_insert(self):
      self.assertEqual(self.bst.insert(5), 1)
      self.assertEqual(self.bst.insert(5), 2)
      self.assertEqual(self.bst.insert(5), 3)
      self.assertEqual(self.bst.insert(4), 1)
      self.assertEqual(self.bst.insert(5), 4)

    def test_search(self):
      self.assertFalse(self.bst.search(5))
      self.bst.insert(5)
      self.assertTrue(self.bst.search(5))
      self.assertFalse(self.bst.search(6))
      self.bst.insert(6)
      self.assertTrue(self.bst.search(6))
       
    def test_preorderTraversal(self):
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(2)
        self.bst.insert(4)
        self.bst.insert(6)
        self.bst.insert(8)
        self.assertEqual(self.bst.preorderTraversal(), [5, 3, 2, 4, 7, 6, 8])

    def test_findMax_happy_path(self):
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(2)
        self.bst.insert(4)
        self.bst.insert(6)
        self.bst.insert(8)
        self.assertEqual(self.bst.findMax(), 8)      

    def test_findPrev(self):
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(2)
        self.bst.insert(4)
        self.bst.insert(6)
        self.bst.insert(8)
        self.assertEqual(self.bst.findPrev(8), 7)  
        self.assertEqual(self.bst.findPrev(7), 6)  
        self.assertEqual(self.bst.findPrev(2), -1)  

if __name__ == '__main__':
    unittest.main()

