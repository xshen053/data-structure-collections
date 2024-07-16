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

    def test_insert_upward_propagation(self):
      self.assertEqual(self.llrb.root, None)
      self.llrb.insert(5)
      self.llrb.insert(11)
      self.llrb.insert(3)
      self.llrb.insert(9)
      self.llrb.insert(7)
      self.llrb.insert(1)
      self.llrb.insert(2)
      """   
      LLRB Tree Representation:
          (5)
          ├── (2)
          │   ├── (1)
          │   └── (3)
          └── (9)
              ├── (7)
              └── (11)      
      """
      self.assertIsNotNone(self.llrb.root)
      self.assertFalse(self.llrb.isRed(self.llrb.root))
      self.assertEqual(self.llrb.root.item, 5)

      # left
      self.assertIsNotNone(self.llrb.root.left)
      self.assertTrue(self.llrb.root.left.isBlack)
      self.assertEqual(self.llrb.root.left.item, 2)

      # left.left
      self.assertIsNotNone(self.llrb.root.left.left)
      self.assertTrue(self.llrb.root.left.left.isBlack)
      self.assertEqual(self.llrb.root.left.left.item, 1)

      # left.right
      self.assertIsNotNone(self.llrb.root.left.right)
      self.assertTrue(self.llrb.root.left.right.isBlack)
      self.assertEqual(self.llrb.root.left.right.item, 3)

      # right
      self.assertIsNotNone(self.llrb.root.right)
      self.assertTrue(self.llrb.root.right.isBlack)
      self.assertEqual(self.llrb.root.right.item, 9)

      # right.left
      self.assertIsNotNone(self.llrb.root.right.left)
      self.assertTrue(self.llrb.root.right.left.isBlack)
      self.assertEqual(self.llrb.root.right.left.item, 7)

      # right.right
      self.assertIsNotNone(self.llrb.root.right.right)
      self.assertTrue(self.llrb.root.right.right.isBlack)
      self.assertEqual(self.llrb.root.right.right.item, 11)
      

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
      """

        9
          \'\
            10

        leftRotate(9)
        
            10
          /
        9

      """
      self.assertEqual(self.llrb.root, None)      
      node1 = self.llrb.LLRBNode(True, 9)
      node2 = self.llrb.LLRBNode(False, 10)
      node1.right = node2

      newRoot = self.llrb.rotateLeft(node1)
      self.assertEqual(newRoot.item, 10)
      self.assertEqual(newRoot.left.item, 9)
      self.assertFalse(self.llrb.isRed(newRoot))
      self.assertTrue(self.llrb.isRed(newRoot.left))

    def test_rotate_left_case2(self):
      """
          2
        1   4(red)
          3   5
      
        leftRotate(2)

                4
          2(red)   5
        1   3

      """
      two = self.llrb.LLRBNode(True, 2)
      one = self.llrb.LLRBNode(True, 1)
      four = self.llrb.LLRBNode(False, 4)
      three = self.llrb.LLRBNode(True, 3)
      five = self.llrb.LLRBNode(True, 5)
      two.left = one
      two.right = four
      four.left = three
      four.right = five
      # rotate(2)
      newRoot = self.llrb.rotateLeft(two)
      self.assertEqual(newRoot.item, 4)      
      self.assertEqual(newRoot.right.item, 5)      
      self.assertEqual(newRoot.left.item, 2)      
      self.assertEqual(newRoot.left.left.item, 1)      
      self.assertEqual(newRoot.left.right.item, 3)      
      self.assertTrue(self.llrb.isRed(newRoot.left))
      self.assertFalse(self.llrb.isRed(newRoot))
      self.assertFalse(self.llrb.isRed(newRoot.left.left))
      self.assertFalse(self.llrb.isRed(newRoot.left.right))
      self.assertFalse(self.llrb.isRed(newRoot.right))

    def test_rotate_left_case3(self):
      """
          3
        1(red)
          2(red)
        rotateLeft(1)
            3
          2(red)
        1(red)
      """

      three = self.llrb.LLRBNode(True, 3)
      two = self.llrb.LLRBNode(False, 2)
      one = self.llrb.LLRBNode(False, 1)
      three.left = one
      one.right = two
      
      self.assertTrue(self.llrb.isRed(one))
      self.assertTrue(self.llrb.isRed(two))      
      self.llrb.rotateLeft(one)
      self.assertTrue(self.llrb.isRed(one))
      self.assertTrue(self.llrb.isRed(two))

    def test_rotate_right(self):
      """
              3
            /
          2(red)
        /    \'\
        1(red)    4
      
        rotateRight(1)

           2
        /    \'\
      1(red)    3(red)
               /
              4    
      """
      one = self.llrb.LLRBNode(False, 1)
      two = self.llrb.LLRBNode(False, 2)
      three = self.llrb.LLRBNode(True, 3)
      four = self.llrb.LLRBNode(True, 4)
      three.left = two
      two.left = one
      two.right = four
      newRoot = self.llrb.rotateRight(three)
      # check value
      self.assertEqual(newRoot.item, 2)
      self.assertEqual(newRoot.left.item, 1)
      self.assertEqual(newRoot.right.item, 3)
      self.assertEqual(newRoot.right.left.item, 4)
      # check color
      self.assertFalse(self.llrb.isRed(newRoot))
      self.assertTrue(self.llrb.isRed(newRoot.left))
      self.assertTrue(self.llrb.isRed(newRoot.right))
      self.assertFalse(self.llrb.isRed(newRoot.right.left))

    def test_flip(self):
      """
            2
          /   \'\
        1(red)   4(red)

        flipColors(2)

            2(red)
          /   \'\
        1       4      
      
      """
      two = self.llrb.LLRBNode(True, 2)
      one = self.llrb.LLRBNode(False, 1)
      four = self.llrb.LLRBNode(False, 4)
      two.left = one
      two.right = four
      self.assertFalse(self.llrb.isRed(two))
      self.assertTrue(self.llrb.isRed(one))
      self.assertTrue(self.llrb.isRed(four))
      self.llrb.flipColors(two)   
      self.assertTrue(self.llrb.isRed(two))
      self.assertFalse(self.llrb.isRed(one))
      self.assertFalse(self.llrb.isRed(four))       

if __name__ == '__main__':
    unittest.main()

