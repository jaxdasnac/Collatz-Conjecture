from time import perf_counter, sleep
from tqdm import tqdm
from matplotlib import pyplot as plt

def is_even(num: int) -> bool: 
    #Returns True if num is even, False otherwise.
    return False if num & 1 else True

def apply_conjecture(num: int) -> int:
    # Applies the conjecture to num and returns the result.
    return int(num/2) if is_even(num) else 3*num + 1

def is_previously_checked(num: int, current_num: int) -> bool:
    # Returns True if num has already been checked in the current loop, False otherwise.
    return num < current_num

def get_start_num(filename: str = 'start_num.txt') -> int:
    """Gets the starting number for the program from the specified file.
    
    If the file does not exist or there is an error reading it, returns 1.
    """
    try:
        with open(filename, 'r') as file:
            num = int(file.readline())
        return num
    except (IOError, ValueError):
        print(f'Error reading {filename}')
        return 1

def preformance():
    try:
        start_num = get_start_num('vars.txt')
        final_num = start_num + 1 + int(input('How many Numbers to Search: '))
        start_time = perf_counter()
        new_loop = []
        for num in tqdm(range(start_num, final_num), unit='checks'):
            current_num = num
            while num != 4:

                if len(new_loop) > len(set(new_loop)):
                    time_elapsed = perf_counter() - start_time
                    print(Summary(time_elapsed, start_num, final_num, new_loop))
                    with open('vars.txt', 'w') as file:
                        file.write(str(current_num))

                new_loop.append(num)
                num = 4 if is_previously_checked(num, current_num) else apply_conjecture(num)
            new_loop = []
        
        time_elapsed = perf_counter() - start_time
        print(Summary(time_elapsed, start_num, final_num, new_loop))
        with open('vars.txt', 'w') as file:
            file.write(str(current_num))
    
    except KeyboardInterrupt:
        new_loop = []
        time_elapsed = perf_counter() - start_time
        print(Summary(time_elapsed, start_num, final_num, new_loop))
        with open('vars.txt', 'w') as file:
            file.write(str(current_num))
    
    except ValueError:
          print('Only INTERGERS are ACCEPTED!')

def connected_dot_graph():
    try:
        start_num = get_start_num('var')
        final_num = start_num + 1 + int(input('How many Numbers to Search: '))
        start_time = perf_counter()
        new_loop = []
        for num in tqdm(range(start_num, final_num), unit='checks'):
            current_num = num
            step = 0
            while num != 1:
                new_loop.append(num)
                
                num = apply_conjecture(num)
                
                plt.scatter(step, num)
                plt.pause(0.05)

                step+=1
                
            new_loop = []
        
        time_elapsed = perf_counter() - start_time
        print(Summary(time_elapsed, start_num, final_num, new_loop))
        plt.show()
        with open('vars.txt', 'w') as file:
            file.write(str(current_num))
    
    except KeyboardInterrupt:
        new_loop = []
        time_elapsed = perf_counter() - start_time
        print(Summary(time_elapsed, start_num, final_num, new_loop))
        with open('vars.txt', 'w') as file:
            file.write(str(current_num))
    
    except ValueError:
          print('Only INTERGERS are ACCEPTED!')

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
New Loop:         {self.new_loop}
"""