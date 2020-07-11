# -*- coding: utf-8 -*-

import pytest
from model_personal_finance.skeleton import fib

__author__ = "Mike Dennis"
__copyright__ = "Mike Dennis"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
