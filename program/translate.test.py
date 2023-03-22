import unittest
import sys
import bpy


class TestAddon(unittest.TestCase):
    def test_translate_shapekeys(self):
        result = bpy.ops.cats_translate.shapekeys()
        self.assertTrue(result == {'FINISHED'})


suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAddon)
runner = unittest.TextTestRunner()
ret = not runner.run(suite).wasSuccessful()
sys.exit(ret)
