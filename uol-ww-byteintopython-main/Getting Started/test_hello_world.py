from hello_world import *


def test_simple_sum_function():
    assert sum_two_values(1, 4) == 5
    assert sum_two_values(43, 22) == 65
    
    
def test_sum_all_function():
    assert sum_all([2,3,4,5]) == 14
    assert sum_all([1,30,4]) == 35
    
    
    
    

