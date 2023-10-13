import pytest
import pandas as pd
from utils import xy_sum, over_5

def test_xy_sum():
    returned_value = xy_sum(1, 2)
    expected_value = 3
    assert returned_value == expected_value

def test_over_5():
    test_df = pd.DataFrame([
                {'ChildID':'ID1',
                'Age':5},
                 {'ChildID':'ID2',
                'Age':4},
                 {'ChildID':'ID3',
                'Age':10},
                 {'ChildID':'ID4',
                'Age':16},
                {'ChildID':'ID5',
                'Age':1},
    ])

    result_df = over_5(test_df)
    results_list = result_df['ChildID'].to_list()
    expected_df = pd.DataFrame([
                {'ChildID':'ID1',
                'Age':5},
                 {'ChildID':'ID3',
                'Age':10},
                 {'ChildID':'ID4',
                'Age':16},
    ])
    expected_list = expected_df['ChildID'].to_list()
    pd.testing.assert_frame_equal(result_df, expected_df)

    assert results_list == expected_list

