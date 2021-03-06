# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, sys

from winsys._compat import unittest
from winsys._compat import *
from winsys.tests import utils as testutils
from winsys import scheduled_tasks

class TestBasic(unittest.TestCase):
    """
    Do just enough to exercise the module: ensure that it imports
    and that basically functionality functions
    """

    def test_tasks(self):
        t = iter(scheduled_tasks.tasks())
        self.assertTrue(next(t))

if __name__ == "__main__":
  unittest.main()
  if sys.stdout.isatty(): raw_input("Press enter...")
