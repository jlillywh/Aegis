import unittest

# Import all tests here
import test_store_bounds
import test_store_outflow
import test_awbm_buckets
import test_surface_store

# Initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Add test to the test suite
suite.addTests(loader.loadTestsFromModule(test_store_outflow))
suite.addTests(loader.loadTestsFromModule(test_store_bounds))
suite.addTests(loader.loadTestsFromModule(test_awbm_buckets))
suite.addTests(loader.loadTestsFromModule(test_surface_store))

# Initialize a runner, pass it the suite and run it
runner = unittest.TextTestRunner(verbosity=1)
result = runner.run(suite)
