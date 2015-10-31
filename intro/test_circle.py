import circle
import numpy as np
import numpy.testing as npt

def test_area():
    npt.assert_equal(circle.area(1), np.pi)
    npt.assert_almost_equal(circle.area(np.sqrt(np.pi)) , (np.pi ** 2))

