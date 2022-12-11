from unittest import TestCase
from grid_traveller import grid_traveller

class GridTravelerTest(TestCase):
    def test_grid_0_by_0(self):
      assert grid_traveller(0,0) == 0
    
    def test_grid_0_by_1(self):
      assert grid_traveller(0,1) == 0

    def test_grid_2_by_3(self):
      assert grid_traveller(2,3) == 3

    def test_grid_3_by_3(self):
      assert grid_traveller(3,3) == 6

    def test_grid_16_by_16(self):
      assert grid_traveller(16,16) == 155117520

    def test_grid_18_by_18(self):
      assert grid_traveller(18,18) == 2333606220