from __future__ import absolute_import
from modelling.py import gaus

from nose.tools import assert_almost_equal

def test_gaus_symmetry():
	A = 100
	B = 0
	C = 1
	xr = 2.0
	xl = -xr
	assert_almost_equal(gaus(xr, A, B, C) == gaus(xl, A, B, C))
