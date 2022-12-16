from typing import List

def is_even(num: int) -> bool: 
    return False if num & 1 else True

def get_start(filename) -> int:
    file = open(filename, 'r')
    start = int(file.readline())
    file.close()
    return start

def apply_conjecture(num: int) -> int:
    if num & (num-1) == 0:
        return 1

    elif is_even(num):
        return int(num/2)

    elif not is_even(num):
        return 3*num + 1

def is_previously_checked(num: int, current_num: int) -> bool:
    if num < current_num:
        return True
    else:
        return False

def summary(start, current_num):
    summary = f"""    =====Summary=====
    Range Searched: {start} to {current_num}
    Numbers Searched: {current_num-start}

    
    """
    print(summary)