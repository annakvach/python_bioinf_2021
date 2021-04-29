import sys

# ANNA PART

list_flags_and_options = sys.argv[1:]
last_ind_in_list_flags_and_options = len(list_flags_and_options) - 1

# default values for filtration start
# str_new_name = list_flags_and_options[last_ind_in_list_flags_and_options].split('.')[0]
int_min_length = 0
# float_left_gc_bound = 0.0
# float_right_gc_bound = 100.0
bool_error_output_permission = False


def check_type_for_number(potential_number):
    try:
        float(potential_number)
        return True
    except ValueError:
        return False


# check is the argument in sys.argv[1:] is a flag
def is_flag(x):
    if "--" in x:
        return True
    else:
        return False


# check is the argument after flag is ok
def argument_after_flag(flag):
    try:
        x = flag
        y = list_flags_and_options.index(x) + 1
        if x in list_flags_and_options:
            if (is_flag(list_flags_and_options[y]) == True) or (y == last_ind_in_list_flags_and_options):
                sys.exit(f"You forgot to specify values after flag [{flag}]!")
            else:
                return True
    except ValueError:
        return False


# check is the argument after-after flag is ok
def argument_after_after_flag(flag):
    try:
        x = flag
        y = list_flags_and_options.index(x) + 2
        if x in list_flags_and_options:
            if (is_flag(list_flags_and_options[y]) == True) or (y == last_ind_in_list_flags_and_options):
                return False
            else:
                return True

    except ValueError:
        return False


# 1 part
def fastq_file_check(file_extinction):
    if file_extinction in str(list_flags_and_options[last_ind_in_list_flags_and_options]):
        str_path_to_dir_with_files = sys.path[0]
        str_input_fastq_file_name = str(sys.argv[len(sys.argv) - 1])
        str_path_to_input_fastq_file = str_path_to_dir_with_files + "/" + str_input_fastq_file_name

        return str_path_to_dir_with_files, str_input_fastq_file_name, str_path_to_input_fastq_file;
    else:
        raise TypeError("Last argument should be .fastq file")


str_path_to_dir_with_files, str_input_fastq_file_name, str_path_to_input_fastq_file = fastq_file_check(".fastq")

# 2 part
if (is_flag(list_flags_and_options[0]) == False) and (".fastq" not in str(list_flags_and_options[0])):
    sys.exit(
        "You should specify at least 1 flag and file name to start filtering!(or just a file name to remove error message (although filtration won't start)")


# 3 part

def OUT_PUT_BASE_NAME(flag):
    if argument_after_flag(flag):
        y1 = list_flags_and_options.index(flag) + 1
        return str(list_flags_and_options[y1])
    else:
        return list_flags_and_options[last_ind_in_list_flags_and_options].split('.')[0]


str_new_name = OUT_PUT_BASE_NAME("--output_base_name")


# 4 part

def MIN_LENGTH(flag):
    if argument_after_flag(flag):
        y2 = list_flags_and_options.index(flag) + 1
        print(list_flags_and_options[y2])
        if check_type_for_number(list_flags_and_options[y2]):
            if float(list_flags_and_options[y2]) % 2 == 0:
                if not int(list_flags_and_options[y2]) > 0:
                    raise ValueError(f'Min length [{list_flags_and_options[y2]}] value can`t be negative')
                return int(list_flags_and_options[y2])
            else:
                raise ValueError(f'Min length value [{list_flags_and_options[y2]}] must be integer number only (int)')
        else:
            raise TypeError(
                f'Min length [{list_flags_and_options[y2]}] value must be non-negative real integer number only (int)')
    else:
        return 0


int_min_length = MIN_LENGTH("--min-length")


# 5 part

def LEFT_GC_BOUNDS(flag):
    if argument_after_flag(flag):
        index = list_flags_and_options.index(flag) + 1
        if check_type_for_number(list_flags_and_options[index]):
            if float(list_flags_and_options[index]) > 0:
                return float(list_flags_and_options[index])
            else:
                raise ValueError(f'Lower GC% bound value [{list_flags_and_options[index]}] must be non-negative real '
                                 f'number only')
        else:
            raise TypeError(f'Lower GC% bound value [{list_flags_and_options[index]}] must be real '
                            f'number only (int or float)')
    else:
        return 0.0


def RIGHT_GC_BOUNDS(flag):

    if argument_after_after_flag(flag):
        index = list_flags_and_options.index(flag) + 2
        if check_type_for_number(list_flags_and_options[index]):
            if float(list_flags_and_options[index]) > 0:
                return float(list_flags_and_options[index])
            else:
                raise ValueError(f'Upper GC% bound value [{list_flags_and_options[index]}] must be non-negative real '
                                 f'number only. \n Remember to use a period and not a comma for numbers')
        else:
            raise TypeError(f'Upper GC% bound value [{list_flags_and_options[index]}] must be real '
                            f'number only int or float type. \n Remember to use a period and not a comma for numbers')
    else:
        return 100.0


def gc_bound_adequacy(left_gc_bound, right_gc_bound):
    if left_gc_bound >= right_gc_bound:
        raise ValueError('Lower GC% bound value must be strictly less than upper GC bound.')


gc_bound_adequacy(LEFT_GC_BOUNDS("--gc_bounds"), RIGHT_GC_BOUNDS("--gc_bounds"))

float_left_gc_bound = LEFT_GC_BOUNDS("--gc_bounds")
float_right_gc_bound = RIGHT_GC_BOUNDS("--gc_bounds")


def error_output_permission(flag):
    if flag in list_flags_and_options:
        return True
    else:
        return False


error_output_permission = error_output_permission("--keep_filtered")


# IGNAT PART

# GC count caculation
def gc_count(read):
    count = 0
    for base in read:
        if base == 'C' or base == 'G':
            count += 1
    return count * 100 / len(read)


# ez
# check for good reads
def passed(read, int_min_length, float_left_gc_bound, float_right_gc_bound):
    if "--min_length" in list_flags_and_options:
        if len(read) < int_min_length:  # if l(read) < min length => F
            return False
        else:
            return True

    if "--gc_bounds" in list_flags_and_options:
        less = gc_count(read) < float_left_gc_bound  # if less than left GC bound => True
        more = gc_count(read) > float_right_gc_bound  # if more than right GC bound => True
        if less or more == True:
            return False
        else:
            return True


# ez
# save in file
def file_output(readlines, file):
    file.write('\n'.join(readlines) + '\n')


# ez af
# open file
fastq_input = open(str_input_fastq_file_name, 'r')
# read all input lines
all_reads = fastq_input.read().splitlines()
# N of reads in file
total_reads = str(len(all_reads) // 4)
# create output blank file and creating failed .fastq if necessary
fastq_passed = open(str_new_name + '_passed.fastq', 'w')
if error_output_permission == True:
    fastq_failed = open(str_new_name + '_failed.fastq', 'w')

# counter for passed/failed reads and their filtration
reads_passed = 0
reads_failed = 0
for i in range(0, len(all_reads), 4):  # we need to read lines by 4, e.g. 1-4, 5-8, 9-12 etc.
    current_read = all_reads[i:i + 4]  # reading 2nd line where ATGC's are
    if i == 0:  # check if empty
        print()
    if passed(current_read[1], int_min_length, float_left_gc_bound, float_right_gc_bound):
        file_output(current_read, fastq_passed)
        reads_passed += 1
    else:
        if error_output_permission == True:
            file_output(current_read, fastq_failed)
        reads_failed += 1

# don't forget to close file
print('Done!')
print('Total reads number is ' + str_input_fastq_file_name + ': ' + total_reads)
print(str(reads_passed) + ' (' + str(round(reads_passed * 100 / int(total_reads), 2)) + '%) reads passed filtering.')
print(str(reads_failed) + ' (' + str(round(reads_failed * 100 / int(total_reads), 2)) + '%) reads failed filtering.')

fastq_passed.close()
fastq_input.close()
if error_output_permission == True:
    fastq_failed.close()
