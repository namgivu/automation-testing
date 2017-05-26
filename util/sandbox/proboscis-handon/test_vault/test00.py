"""Demo @test at class level"""

import unittest
from proboscis.asserts import assert_equal
from proboscis import test


@test(groups=["unit", "numbers"])
class TestIsNegative(unittest.TestCase):
  """Confirm that utils.is_negative works correctly."""

  def test_should_return_true_for_negative_numbers(self):
    self.assertTrue(-47<0)

  def test_should_return_false_for_positive_numbers(self):
    self.assertFalse(56<0)

  def test_should_return_false_for_zero(self):
    self.assertFalse(0<0)
