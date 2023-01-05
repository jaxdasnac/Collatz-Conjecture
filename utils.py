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


#def connected_dot_graph(get_sn):
    try:
        start_num = get_sn
        final_num = start_num + int(input('How many Numbers to Search: '))
        start_time = time()
        new_loop = [start_num]
        sequence = []
        colors = []
        for num in tqdm(range(start_num, final_num), unit='lines'):
            current_num = num
            #color set
            color = (uniform(0.4, 0.9), uniform(0.4, 0.9), uniform(0.4, 0.9))
            while num != 1:
                new_loop.append(num)
                num = apply_conjecture(num)
                
                
            new_loop.append(num)
            #current loop drawn
            for i in range(len(new_loop)):
                plt.plot(range(i+1), new_loop[0:i+1], color=color, marker='o')
                plt.pause(0.05)

            sequence.append(new_loop)
            colors.append(color)
            new_loop = []
            #cleared
            plt.cla()
            #all loops drawn
            for i, loop in enumerate(sequence):
                plt.plot(range(len(loop)), loop, color=colors[i], marker='o')
        
        time_elapsed = time() - start_time
        print(Summary(time_elapsed, start_num, current_num, final_num, new_loop))
        plt.show()
        with open('vars.txt', 'w') as file:
            file.write(str(current_num))
    
    except KeyboardInterrupt:
        new_loop = []
        time_elapsed = time() - start_time
        print(Summary(time_elapsed, start_num, current_num, final_num, new_loop))
        with open('vars.txt', 'w') as file:
            file.write(str(current_num))
    
    except ValueError:
          print('Only INTERGERS are ACCEPTED!')

class Conjecture():

    def __init__(self, mode=1, filename='start_num.txt', number_range=None, save_num=False, make_sequence=False, unit='checks', draw_graph=False) -> None:
        self.mode = mode
        self.filename = filename
        self.start_num = get_start_num(self.filename) if get_start_num(self.filename) else number_range[0]
        self.final_num = number_range[1]
        self.save_num = save_num
        self.start_time: float = time()
        self.time_elapsed: float = time() - self.start_time
        self.new_loop = [self.start_num]
        self.sequence = [] if make_sequence else None
        self.unit: str = unit
        self.colors = []

        self.run_conjecture()

        self.summary()

        if draw_graph:
            self.draw_graph()
    
    def run_conjecture(self):
        for num in tqdm(range(self.start_num, self.final_num), unit=self.unit):

            if self.sequence == []:
                self.sequence.append(self.new_loop)

            self.new_loop = []

            self.new_loop.append(num)

            while num != 4:

                if len(self.new_loop) > len(set(self.new_loop)):

                    if self.save_num:
                        with open(self.filename, 'w') as file:
                            file.write(str(self.new_loop[-1]))

                self.new_loop.append(num)

                num = 4 if is_previously_checked(num, self.new_loop[-1]) else apply_conjecture(num) if self.mode in [1] else apply_conjecture(num)
            
            
            

                        
    
    def summary(self):
        return print(f"""
=====Summary=====
Time Elapsed:     {self.time_elapsed:.2f}s
Start Number:     {self.start_num} 
End Number:       {self.final_num-1}
New Start Number: {self.final_num}
Numbers Searched: {self.new_loop[-1]-self.start_num}
New Loop:         {self.new_loop}
""")

    def get_start_num(self) -> int:
        """Gets the starting number for the program from the specified file.
        
        If the file does not exist or there is an error reading it, returns 1.
        """
        try:
            with open(self.filename, 'r') as file:
                num = int(file.readline())
            return num
        except (IOError, ValueError):
            print(f'Error reading {self.filename}')
            return False

    def make_graph(self):
        pass

    