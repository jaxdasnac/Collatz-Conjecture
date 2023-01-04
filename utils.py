from typing import List
from tqdm import tqdm

def is_even(num: int) -> bool: 
    return False if num & 1 else True

def apply_conjecture(num: int) -> int:
    return int(num/2) if is_even(num) else 3*num + 1


def is_previously_checked(num: int, current_num: int) -> bool:
    return num < current_num

def get_start_num(filename: str = 'start_num.txt') -> int:
    try:
        with open(filename, 'r') as file:
            num = int(file.readline())
        return num
    except (IOError, ValueError):
        print(f'Error reading {filename}')
        return 1

class Summary():
    def __init__(self, time_elapsed, start_num, final_num, new_loop) -> None:
        self.time_elapsed = time_elapsed
        self.start_num = start_num
        self.final_num = final_num-1
        self.new_loop = new_loop if new_loop != [] else 'All Loops End in 4, 2, 1...'

    def __str__(self):
        return f"""
=====Summary=====
Time Elapsed:     {self.time_elapsed:.2f}s
Start Number:     {self.start_num} 
End Number:       {self.final_num}
New Start Number: {self.final_num+1}
Numbers Searched: {self.final_num-self.start_num}
New Loop:         {self.new_loop}"""