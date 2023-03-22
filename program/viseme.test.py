import unittest
import sys
import bpy


class TestAddon(unittest.TestCase):
    def test_viseme_button(self):
        # first fix armature
        bpy.ops.cats_armature.fix()

suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAddon)
runner = unittest.TextTestRunner()
ret = not runner.run(suite).wasSuccessful()
sys.exit(ret)
