import unittest
from unittest import TestCase

import pythonapp


class TestApp(TestCase):
    def test_str(self):
        s = pythonapp.msg()
        self.assertTrue(not isinstance(s, str))


