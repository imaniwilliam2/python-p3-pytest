#!/usr/bin/env python3

from not_none_functions import return_not_none

def test_return_not_none():
    '''Test if return_not_none function returns a value that is not None.'''
    result = return_not_none()
    assert result is None, "The return value should be None"
