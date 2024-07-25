import unittest
from CycleSort import cyclesort


class TestCycleSort(unittest.TestCase):
  def setUp(self) -> None:
    return super().setUp()
  
  def test1(self):
    assert cyclesort([2,3,1,0,5,4]) == [0,1,2,3,4,5]

if __name__ == '__main__':
    unittest.main()
