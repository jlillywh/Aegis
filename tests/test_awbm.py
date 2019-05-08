import unittest
from hydrology.awbm import Awbm


class TestBucketCase(unittest.TestCase):
    def setUp(self):
        """Set up a new object to be tested"""

        self.a1 = Awbm()
        self.init_quantity_buckets = [4.2, 140.4, 42.9]
        self.a1.buckets.set_quantities(self.init_quantity_buckets)
        self.a1.base.quantity = 10.0
        self.a1.surface.quantity = 10.0
        self.a1.runoff(10.0, 1.0)
        self.precision = 3

    def tearDown(self):
        """Destroy the object after running tests"""
        del self.a1

    def testUpdateCompCapacity(self):
        """New bucket capacity == user defined array"""
        new_buckets = [57.43, 143.33, 298.49]
        self.a1.set_comp_capacity(new_buckets)
        for i in range(len(new_buckets)):
            self.assertEqual(self.a1.buckets.stores[i].capacity, new_buckets[i] * self.a1.partial_area_fraction[i])

    def testBucketsQuantity(self):
        """change the total quantity in the buckets"""
        self.assertEqual(self.a1.buckets.total_qantity(), 192.047)

    def testBucketsOverflow(self):
        """change the total quantity in the buckets"""
        self.assertAlmostEqual(self.a1.buckets.total_overflow(), 4.221, self.precision)

    def testSurfaceQuantity(self):
        """change the total quantity in the buckets"""
        self.assertAlmostEqual(self.a1.surface.quantity, 10.134, self.precision)

    def testBucketsQuantity(self):
        """change the total quantity in the buckets"""
        self.assertAlmostEqual(self.a1.base.quantity, 5.867, self.precision)


class TestSurfaceStore(unittest.TestCase):
    def setUp(self):
        """Set up a new object to be tested"""
        self.a2 = Awbm()
        self.a2.buckets.set_quantities([5.01696, 140.465, 63.4778])
        self.precision = 3

    def tearDown(self):
        """Destroy the object after running tests"""
        del self.a2

    def testStoreOutflow(self):
        """Make sure the outflow from the store is correct"""
        precip = 6.54
        et = 0.25
        outflow = 0.0
        for i in range(0, 10):
            outflow += self.a2.runoff(precip, et)

        self.assertAlmostEqual(outflow, 44.522, self.precision)


if __name__ == '__main__':
    unittest.main()