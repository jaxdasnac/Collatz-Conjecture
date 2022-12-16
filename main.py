from utils import *

if __name__ == '__main__':

    start = get_start('vars.txt')
    vars = open('vars.txt', 'w')
    current_num = start
    for num in range(start, start+int(input('How many numbers to iterate through: '))):

        current_num = num+1
        new_loop = []

        while num != 1:

            new_loop.append(num)
            if len(new_loop) > len(set(new_loop)):
                print(current_num)

            # num set to 1 to break loop if number is < current number 
            # else it applies the conjecture
            num = 1 if is_previously_checked(num, current_num) else apply_conjecture(num)
            
                
    vars.write(f'{current_num}')
    vars.close()

summary(start, current_num)