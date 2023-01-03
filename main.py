from utils import *
from tqdm import tqdm
if __name__ == '__main__':

    try: 
        start = get_start_num('vars.txt')
        og = start
        for num in tqdm(range(start, start+int(float(input('How many numbers to iterate through: ')))), unit=''):
            start = num+1
            
            new_loop = []

            while num != 1:

                new_loop.append(num)
                if len(new_loop) > len(set(new_loop)):
                    print(start)

                # num set to 1 to break loop if number is < current number 
                # else it applies the conjecture
                num = 1 if is_previously_checked(num, start) else apply_conjecture(num)
                
        with open('vars.txt', 'w') as file:
            file.write(str(start))

    except KeyboardInterrupt:
        print('Stopped')
        with open('vars.txt', 'w') as file:
            file.write(str(start))

summary(og, start)