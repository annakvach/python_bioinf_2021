import pytest
from Tests_HW.PARSING_for_filtrator import \
    check_type_for_number, \
    check_int, \
    is_flag, \
    gc_count,\
    passed


@pytest.mark.parametrize("a, result", [(8, True),
                                       ('vosem', False),
                                       ([8], False),
                                       ({8, 8, 8}, False)])
def test_NUMBER_for_Check_int_and_Check_type_for_number(a, result):
    assert check_type_for_number(a) == result
    assert check_int(a) == result


@pytest.mark.parametrize("read, result_gc_count", [('AAAAAGGGGG', 50.0),
                                                   ('AAAAAA', 0.0),
                                                   ('CCCGGG', 100.0)])
def test_gc_count(read, result_gc_count):
    assert gc_count(read) == result_gc_count




@pytest.mark.parametrize("read, int_min_length, float_left_gc_bound, float_right_gc_bound, list_flags_and_options, read_destiny",
                         [('AAAAAGGGGG', 5, 40.0, 45.0, ["--min_length", "--gc_bounds"], False),
                          ('AAAAAGGGGG', 5, 60.0, 75.0, ["--min_length", "--gc_bounds"],  False),
                          ('AAAAAGGGGG', 5, 40.0, 55.0, ["--min_length", "--gc_bounds"], True),
                          ('AAAAAGGGGG', 11, 40.0, 45.0, ["--min_length", "--gc_bounds"], False),
                          ('AAAAAGGGGG', 1, 40, 45, ["--min_length", "--gc_bounds"], False),
                          ])
def test_passed(read, int_min_length, float_left_gc_bound, float_right_gc_bound, list_flags_and_options, read_destiny):

    assert passed(read, int_min_length, float_left_gc_bound, float_right_gc_bound, list_flags_and_options) == read_destiny
