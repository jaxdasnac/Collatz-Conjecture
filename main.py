from utils import *
import time

def main():
    try:
        start_num = get_start_num('vars.txt')
        final_num = start_num + 1 + abs(int(input('How many Numbers to Search: ')))
        start_time = time.perf_counter()
        new_loop = []

        for num in tqdm(range(start_num, final_num), unit='checks'):
            current_num = num
            print(current_num)
            while num != 4:

                if len(new_loop) > len(set(new_loop)):
                    time_elapsed = time.perf_counter() - start_time
                    print(Summary(time_elapsed, start_num, final_num, new_loop))
                    with open('vars.txt', 'w') as file:
                        file.write(str(current_num))

                new_loop.append(num)
                num = 4 if is_previously_checked(num, current_num) else apply_conjecture(num)
            new_loop = []
        
        time_elapsed = time.perf_counter() - start_time
        print(Summary(time_elapsed, start_num, final_num, new_loop))
        with open('vars.txt', 'w') as file:
            file.write(str(current_num))

    except KeyboardInterrupt:
        new_loop = []
        time_elapsed = time.perf_counter() - start_time
        print(Summary(time_elapsed, start_num, final_num, new_loop))
        with open('vars.txt', 'w') as file:
            file.write(str(current_num))
    
    except ValueError:
        print('Only INTERGERS are ACCEPTED!')

   

if __name__ == '__main__':
    main()