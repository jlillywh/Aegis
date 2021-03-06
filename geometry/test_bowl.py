import unittest
from geometry.bowl import Bowl


class TestBowl(unittest.TestCase):
    def setUp(self):
        """Set up a new object to be tested"""
        elevations = [0.0, 1.0, 2.0, 3.0, 4.0]
        areas = [0.0, 300.0, 375.0, 400.0, 415.0]
        self.b = Bowl(elevations, areas)

    def tearDown(self):
        """Destroy the object after running tests"""
        del self.b

    def testPlot(self):
        """Head loss should be correct"""
        
        self.b.plot_elevation_volume()
 