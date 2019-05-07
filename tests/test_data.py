import unittest
from inputs.data import Scalar, Vector
import numpy as np
from pandas.util.testing import assert_frame_equal # <-- for testing dataframes


class TestScalar(unittest.TestCase):
    def setUp(self):
        """Set up a new object to be tested"""
        self.s1 = Scalar(2.57, unit='in/d')
        self.dec_places = 3

    def tearDown(self):
        """Destroy the object after running tests"""
        del self.s1

    def testChangeUnit(self):
        """Values should be converted correctly upon changing the unit"""
        new_unit = 'mm/d'
        s2 = self.s1
        s2.unit = new_unit
        self.assertAlmostEqual(s2.magnitude, 65.278, self.dec_places)

    def testChangeMagnitude(self):
        new_value = 3.1416
        s2 = self.s1
        s2.magnitude = new_value
        s2_si = s2.data.to_base_units()
        self.assertAlmostEqual(s2_si.magnitude, 9.236e-7, self.dec_places)
        
class TestVector(unittest.TestCase):
    def setUp(self):
        """Set up a new object to be tested"""
        self.rn = np.random.lognormal(size=12)
        self.v1 = Vector(self.rn, display_unit='in/d')
        self.v2 = Vector(self.rn, display_unit='in/d')
        self.dec_places = 3

    def tearDown(self):
        """Destroy the object after running tests"""
        del self.v1
        del self.v2

    def testChangeUnit(self):
        """Values should be converted correctly upon changing the unit"""
        new_unit = 'mm/d'
        self.v1.unit = new_unit
        self.v1.unit = 'in/d'
        assert_frame_equal(self.v1.data, self.v2.data)

    def testChangeMagnitude(self):
        new_value = np.random.lognormal(size=12)
        self.v1.magnitude = new_value
        np.testing.assert_almost_equal(self.v1.magnitude, new_value, self.dec_places)