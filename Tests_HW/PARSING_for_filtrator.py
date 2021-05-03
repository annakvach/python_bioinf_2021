import sys

# ANNA PART

# Собираю аргументы и флаги
list_flags_and_options = sys.argv[1:]



def check_type_for_number(potential_number):
    try:
        float(potential_number)
        return True
    except TypeError:
        print('TypeError')
        return False
    except ValueError:
        print('ValueError')
        return False
    except NameError:
        print('NameError')
        return False


def check_int(number):
    try:
        int(number)
        return True
    except TypeError:
        print('TypeError')
        return False
    except ValueError:
        print('ValueError')
        return False
    except NameError:
        print('NameError')
        return False


# check is the argument in sys.argv[1:] is a flag
def is_flag(x):
    if "--" in x and iter(x):
        return True
    else:
        return False


def flag_check(my_list):
    List = ["--output_base_name", "--min_length", "--gc_bounds", "--keep_filtered"]
    for i in my_list:
        if is_flag(i):
            if not any(i in s for s in List):
                raise ValueError(f'You misspelled the flag: [{i}] \n'
                                 f'Valid flags: \n'
                                 f'\t --output_base_name \n'
                                 f'\t --min_length \n'
                                 f'\t --gc_bounds \n'
                                 f'\t --keep_filtered \n')

        else:
            continue


# check is the argument after flag is ok
def argument_after_flag(flag, my_list):
    last_ind_in_list_flags_and_options = len(my_list) - 1
    try:
        y = my_list.index(flag) + 1
        if flag in my_list:
            if (is_flag(my_list[y])) or (y == last_ind_in_list_flags_and_options):
                raise SystemExit(f"You forgot to specify values after flag [{flag}]!")
            else:
                return True
    except ValueError:
        return False


# check is the argument after-after flag is ok
def argument_after_after_flag(flag, my_list):
    last_ind_in_list_flags_and_options = len(my_list) - 1
    try:
        x = flag
        y = my_list.index(x) + 2
        if x in my_list:
            if (is_flag(my_list[y])) or (y == last_ind_in_list_flags_and_options):
                return False
            else:
                return True
    except ValueError:
        return False


# 1 part
def fastq_file_check(file_extinction, my_list):
    last_ind_in_list_flags_and_options = len(my_list) - 1
    if file_extinction in str(my_list[last_ind_in_list_flags_and_options]):
        # str_path_to_dir_with_files = sys.path[0]
        # str_input_fastq_file_name = str(sys.argv[len(sys.argv) - 1])
        # str_path_to_input_fastq_file = str_path_to_dir_with_files + "/" + str_input_fastq_file_name

        return sys.path[0], str(sys.argv[len(sys.argv) - 1]), sys.path[0] + "/" + str(sys.argv[len(sys.argv) - 1])
    else:
        raise TypeError("Last argument should be .fastq file")


'''str_path_to_dir_with_files, str_input_fastq_file_name, str_path_to_input_fastq_file = fastq_file_check(".fastq")'''

'''# 2 part
if (is_flag(list_flags_and_options[0]) == False) and (".fastq" not in str(list_flags_and_options[0])):
    sys.exit(
        "You should specify at least 1 flag and file name to start filtering!(or just a file name to "
        "remove error message (although filtration won't start)")
'''

# 3 part

def OUT_PUT_BASE_NAME(flag, my_list):
    last_ind_in_list_flags_and_options = len(my_list) - 1
    if argument_after_flag(flag, my_list):
        value = my_list[my_list.index(flag) + 1]
        return str(value)
    else:
        return my_list[last_ind_in_list_flags_and_options].split('.')[0]


'''str_new_name = OUT_PUT_BASE_NAME("--output_base_name")'''


# 4 part

def MIN_LENGTH(flag, my_list):
    last_ind_in_list_flags_and_options = len(my_list) - 1
    if argument_after_flag(flag, my_list):
        value = my_list[my_list.index(flag) + 1]
        if check_type_for_number(value):
            if check_int(value):

                if int(value) < 0:
                    raise ValueError(f'Min length value can`t be negative: [{value}]')
                else:
                    return int(value)
            else:
                raise ValueError(f'Min length value must be integer number only (int): [{value}]')

        else:
            raise TypeError(
                f'Min length value must be non-negative real integer number only (int): [{value}]')
    else:
        return 0


'''int_min_length = MIN_LENGTH("--min_length")'''


# 5 part

def LEFT_GC_BOUNDS(flag, my_list):
    last_ind_in_list_flags_and_options = len(my_list) - 1
    if argument_after_flag(flag, my_list):
        value = my_list[my_list.index(flag) + 1]
        if check_type_for_number(value):
            if float(value) > 0:
                return float(value)
            else:
                raise ValueError(f'Lower GC% bound value must be non-negative real number only: [{value}] ')
        else:
            raise TypeError(f'Lower GC% bound value must be real number only (int or float): [{value}]')
    else:
        return 0.0


def RIGHT_GC_BOUNDS(flag, my_list):
    last_ind_in_list_flags_and_options = len(my_list) - 1
    if argument_after_after_flag(flag, my_list):
        value = my_list[my_list.index(flag) + 2]
        if check_type_for_number(value):
            if float(value) > 0:
                return float(value)
            else:
                raise ValueError(f'Upper GC% bound value must be non-negative real number only: [{value}]. '
                                 f'\n Remember to use a period and not a comma for numbers')
        else:
            raise TypeError(f'Upper GC% bound value [{value}] must be real number only int or float type: [{value}]. '
                            f'\n Remember to use a period and not a comma for numbers')
    else:
        return 100.0


def gc_bound_adequacy(left_gc_bound, right_gc_bound):
    if left_gc_bound >= right_gc_bound:
        raise ValueError(f'Lower GC% bound value must be strictly less than upper GC bound. [{left_gc_bound} >= {right_gc_bound}]')


'''gc_bound_adequacy(LEFT_GC_BOUNDS("--gc_bounds"), RIGHT_GC_BOUNDS("--gc_bounds"))
float_left_gc_bound = LEFT_GC_BOUNDS("--gc_bounds")
float_right_gc_bound = RIGHT_GC_BOUNDS("--gc_bounds")'''


def error_output_permission(flag, my_list):
    if flag in my_list:
        return True
    else:
        return False


'''
# проверяю аргуенты и флаги и сохраняю их для дальнейшего пользования
flag_check(list_flags_and_options)

str_path_to_dir_with_files, str_input_fastq_file_name, str_path_to_input_fastq_file = fastq_file_check(".fastq", list_flags_and_options, last_ind_in_list_flags_and_options)

str_new_name = OUT_PUT_BASE_NAME("--output_base_name", list_flags_and_options, last_ind_in_list_flags_and_options)

int_min_length = MIN_LENGTH("--min_length", list_flags_and_options, last_ind_in_list_flags_and_options)

gc_bound_adequacy(LEFT_GC_BOUNDS("--gc_bounds", list_flags_and_options, last_ind_in_list_flags_and_options),
                  RIGHT_GC_BOUNDS("--gc_bounds", list_flags_and_options, last_ind_in_list_flags_and_options))
float_left_gc_bound = LEFT_GC_BOUNDS("--gc_bounds", list_flags_and_options, last_ind_in_list_flags_and_options)

float_right_gc_bound = RIGHT_GC_BOUNDS("--gc_bounds", list_flags_and_options, last_ind_in_list_flags_and_options)

error_output_permission = error_output_permission("--keep_filtered", list_flags_and_options)
'''

# IGNAT PART

# GC count caculation
def gc_count(read):
    count = 0
    for base in read:
        if base == 'C' or base == 'G':
            count += 1
    return count * 100 / len(read)


def passed(read, int_min_length, float_left_gc_bound, float_right_gc_bound, list_flags_and_options):
    if "--min_length" in list_flags_and_options:
        if len(read) > int_min_length:  # if l(read) < min length => F
            l = True
        else:
            l = False

    if "--gc_bounds" in list_flags_and_options:
        if float_left_gc_bound < gc_count(read) < float_right_gc_bound:
            b = True
        else:
            b = False
    return b and l