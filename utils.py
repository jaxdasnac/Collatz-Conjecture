from time import time
from tqdm import tqdm
from matplotlib import pyplot as plt
from random import uniform

def is_even(num: int) -> bool: 
    #Returns True if num is even, False otherwise.
    return False if num & 1 else True


def apply_conjecture(num: int) -> int:
    # Applies the conjecture to num and returns the result.
    return int(num/2) if is_even(num) else 3*num + 1

def is_previously_checked(num: int, current_num: int) -> bool:
    # Returns True if num has already been checked in the current loop, False otherwise.
    return num < current_num

def get_start_num(filename):
        try:
            with open(filename, 'r') as file:
                num = int(file.readline())
            return num
        except (IOError, ValueError):
            print(f'Error reading {filename}')
            return 1

class Conjecture():
    def __init__(self, number_range=(1, 10), make_sequence=False, unit='checks', rand_color=False, do_graph=False) -> None:
        """
        number_range: must be a tuple object containing a start integer and how many integers to loop through
        make_sequence: must be set to True to make a graph, otherwise set to False for speed
        unit: this will change the units on the tqdm progress bar
        rand_color: defualt False will set graph color to black, setting to True will make each graph line be a different color
        """

        # start and end num
        self.start_num = number_range[0]
        self.final_num = self.start_num+number_range[-1]

        # timers
        self.start_time: float = time()
        self.time_elapsed: float = time() - self.start_time

        # loop and sequence of loops
        self.new_loop = []
        self.sequence = [] if make_sequence else None

        # tqdm load bar units
        self.unit: str = unit

        # graph color
        self.do_graph = do_graph
        self.rand_color = rand_color
        self.colors = []

        self.run_conjecture()
    
    def run_conjecture(self):
        """
        iterates through each integer in a range between the start and end numbers
            current number is added to loop
            if the number isn't 1:
                checks to see if a loop does not hit 4, 2, 1 which will break while loop\n
                applies 3N + 1 to the num\n
                adds new number to the loop\n
            checks to see if a loop does not hit 4, 2, 1 which will break for loop
            adds the loop to the sequence
        saves the end time
        """
        for num in tqdm(range(self.start_num, self.final_num), unit=self.unit):
            
            self.new_loop.append(num)
            
            while num != 1:

                if len(self.new_loop) > len(set(self.new_loop)):
                    break

                num = apply_conjecture(num)
                self.new_loop.append(num)

            if len(self.new_loop) > len(set(self.new_loop)):
                    break

            self.sequence.append(self.new_loop)
            
            #current modifiers
            if self.do_graph:
                if self.rand_color:
                    self.colors.append((uniform(0.4, 0.9), uniform(0.4, 0.9), uniform(0.4, 0.9)))
                else:
                    self.colors.append('black')

                for i in range(len(self.new_loop)):
                    plt.plot(range(len(self.new_loop[:i])), self.new_loop[:i], color=self.colors[-1], marker='o')
                    plt.pause(0.05)

                plt.cla()

                #print lines up to current line
                for i in range(len(self.sequence)):
                    plt.plot(range(len(self.sequence[i])), self.sequence[i], color=self.colors[i], marker='o')

            self.new_loop = []

        self.time_elapsed = time() - self.start_time

        
    
    def __str__(self):
        return f"""
=====Summary=====
Time Elapsed:     {self.time_elapsed:.2f}s
Start Number:     {self.start_num} 
End Number:       {self.final_num-1}
Numbers Searched: {self.final_num-self.start_num}
New Loop:         {self.new_loop if self.new_loop != [] else 'All Numbers Loop 4, 2, 1...'}
"""

    def draw_graph(self):
        
        self.colors = [(uniform(0.4, 0.9), uniform(0.4, 0.9), uniform(0.4, 0.9)) if self.rand_color else 'black' for _ in range(len(self.sequence))]

        #loop over sequence
        for loop_number, loop in enumerate(self.sequence):
            #draw current line
            for i in range(len(loop)):
                plt.plot(range(len(loop[:i])), loop[:i], color=self.colors[loop_number], marker='o')
                plt.pause(0.05)
            #clear all lines to reduce dot lag :)
            plt.cla()

            #print lines up to current line
            for color, line in enumerate(self.sequence[:loop_number+1]):
                plt.plot(range(len(line)), line, color=self.colors[color], marker='o')

    