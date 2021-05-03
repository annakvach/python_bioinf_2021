import pytest
from Tests_HW.PARSING_for_filtrator import \
    check_type_for_number, \
    check_int, \
    is_flag, \
    gc_count, \
    passed, \
    flag_check, \
    argument_after_flag, \
    argument_after_after_flag


# Parsing part
@pytest.mark.parametrize("a, result", [(8, True),
                                       ('vosem', False),
                                       ([8], False),
                                       ({8, 8, 8}, False)])
def test_NUMBER_for_Check_int_and_Check_type_for_number(a, result):
    assert check_type_for_number(a) == result
    assert check_int(a) == result


def test_flag_check():
    with pytest.raises(ValueError):
        flag_check(["--output_bosee_name", "0-o" "--min-length", "10", "--gc_bunds", "50" "--keep_filtered"])


# check is the argument after flag is ok (not a flag) | True
@pytest.mark.parametrize("flag, list_flags_and_options, result", [
    ('--min_length',
     ['--min_length', '15', '--gc_bounds', '40', '41', '--keep_filtered', '--output_base_name', 'new_name',
      'file.fastq'], True),
    ('--gc_bounds',
     ['--min_length', '15', '--gc_bounds', '40', '41', '--keep_filtered', '--output_base_name', 'new_name',
      'file.fastq'], True),
    ('--output_base_name',
     ['--min_length', '15', '--gc_bounds', '40', '41', '--keep_filtered', '--output_base_name', 'new_name',
      'file.fastq'], True),
])
def test_argument_after_flag(flag, list_flags_and_options, result):
    assert argument_after_flag(flag, list_flags_and_options) == result


# check is the argument after flag is ok (not a flag) | SystemExit
def test_exit_argument_after_flag():
    with pytest.raises(SystemExit):
        argument_after_flag('--min_length', ['--min_length', '--gc_bounds', '40', '41', '--keep_filtered',
                                             '--output_base_name', 'new_name', 'file.fastq'])
        argument_after_flag('--gc_bounds',
                            ['--min_length', '8', '--gc_bounds', '--keep_filtered', '--output_base_name',
                             'new_name', 'file.fastq'])
        argument_after_flag('--output_base_name',
                            ['--min_length', '8', '--gc_bounds', '40', '41', '--keep_filtered', '--output_base_name',
                             'file.fastq'])

'''
def argument_after_after_flag(flag, my_list):
    last_ind_in_list_flags_and_options = len(my_list) - 1
    try:
        x = flag
        y = my_list.index(x) + 2
        if x in my_list:
            if (is_flag(my_list[y]) == True) or (y == last_ind_in_list_flags_and_options):
                return False
            else:
                return True
    except ValueError:
        return False
'''


@pytest.mark.parametrize("flag, list_flags_and_options, result", [
    # flag and arguments in different places
    ('--gc_bounds',
     ['--min_length', '15', '--keep_filtered', '--output_base_name', 'new_name', '--gc_bounds', '40', '41',
      'file.fastq'], True),

    ('--gc_bounds',
     ['--min_length', '15', '--keep_filtered', '--gc_bounds', '40', '41', '--output_base_name', 'new_name',
      'file.fastq'], True),

    ('--gc_bounds',
     ['--gc_bounds', '40', '41', '--min_length', '15',  '--keep_filtered', '--output_base_name', 'new_name',
      'file.fastq'], True),

    # without flag
    ('--gc_bounds',
     ['--min_length', '15', '--keep_filtered', '--output_base_name', 'new_name', '--gc_bounds', '40',
      'file.fastq'], False),

    # without second value in different places
    ('--gc_bounds',
     ['--gc_bounds', '15', '--keep_filtered', '--gc_bounds', '41', '--output_base_name', 'new_name',
      'file.fastq'], False),

    ('---gc_bounds',
     ['--gc_bounds', '40', '--min_length', '15', '--keep_filtered', '--output_base_name', 'new_name',
      'file.fastq'], False),

    ('---gc_bounds',
     ['--gc_bounds', '--min_length', '15', '--keep_filtered', '--output_base_name', 'new_name',
      'file.fastq'], False),
])
def test_argument_after_after_flag(flag, list_flags_and_options, result):
    assert argument_after_after_flag(flag, list_flags_and_options) == result











# Filtration part
@pytest.mark.parametrize("read, result_gc_count", [('AAAAAGGGGG', 50.0),
                                                   ('AAAAAA', 0.0),
                                                   ('CCCGGG', 100.0)])
def test_gc_count(read, result_gc_count):
    assert gc_count(read) == result_gc_count


@pytest.mark.parametrize(
    "read, int_min_length, float_left_gc_bound, float_right_gc_bound, list_flags_and_options, read_destiny",
    [('AAAAAGGGGG', 5, 40.0, 45.0, ["--min_length", "--gc_bounds"], False),
     ('AAAAAGGGGG', 5, 60.0, 75.0, ["--min_length", "--gc_bounds"], False),
     ('AAAAAGGGGG', 5, 40.0, 55.0, ["--min_length", "--gc_bounds"], True),
     ('AAAAAGGGGG', 11, 40.0, 45.0, ["--min_length", "--gc_bounds"], False),
     ('AAAAAGGGGG', 1, 40, 45, ["--min_length", "--gc_bounds"], False),
     ])
def test_passed(read, int_min_length, float_left_gc_bound, float_right_gc_bound, list_flags_and_options, read_destiny):
    assert passed(read, int_min_length, float_left_gc_bound, float_right_gc_bound,
                  list_flags_and_options) == read_destiny
