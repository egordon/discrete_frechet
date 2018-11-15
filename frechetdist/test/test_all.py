
import pytest
import sys, os
import numpy as np
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from frechetdist import frdist

test_cases = [
    {
        'P': np.array([ [1,1], [2,1], [2,2] ]),
        'Q': np.array([ [2,2], [0,1], [2,4] ]),
        'expected': 2.0
    },

    {
        'P': np.array([[1,1], [2,1], [2,2]]),
        'Q': np.array([[1,1], [2,1], [2,2]]),
        'expected': 0
    },
    
    {
        'P': np.array([ [-1,0], [0,1], [1,0], [0, -1] ]),
        'Q': np.array([ [-2,0], [0,2], [2,0], [0, -2] ]),
        'expected': 1.0
    }
]

def test_main():
    for test_case in test_cases:
        P = test_case['P']
        Q = test_case['Q']
        eo = test_case['expected']

        assert frdist(P,Q) == eo

def test_errors():

    P=np.array([[1,1], [2,1]])
    Q=np.array([[2,2], [0,1], [2,4]])
    with pytest.raises(ValueError):
        assert frdist(P,Q) == 2.0

    P=np.array([])
    Q=np.array([[2,2], [0,1], [2,4]])
    with pytest.raises(ValueError):
        assert frdist(P,Q) == 2.0
    
