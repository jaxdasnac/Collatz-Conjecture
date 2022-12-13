from func import *
from typing import List
from time import time

if __name__ == '__main__':
    
    search_range: List[int] = [int(string) for string in input().split(' ')]

    file = open('badnumbers.txt', 'r')

    for num in range(search_range[0], search_range[1]+1):
        current_num = num
        while num != 1:

            for line in file:
                    if num == line:
                        num = 1
                    

            if num & (num-1) == 0:
                break

            elif is_even(num):
                num = int(num/2)
                for line in file:
                    if num == line:
                        break
                    file.write(str(num))

            elif not is_even(num):
                num = 3*num + 11
                for line in file:
                    if num == line:
                        break
                    file.write(str(num))



        
        print(f'{current_num}: loops 4, 2, 1...')
    file.close()
        
