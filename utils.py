from typing import List

def is_even(num: int) -> bool: 
    return False if num & 1 else True

def get_start_num(filename) -> int:
    with open(filename, 'r') as file:
        num = int(file.readline())
    return num

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
    Start Number:     {start} 
    End Number:       {current_num}
    Numbers Searched: {current_num-start}

    
    """
    print(summary)