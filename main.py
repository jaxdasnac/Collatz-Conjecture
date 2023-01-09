from utils import *

def main():
    while True:
        mode = int(input('Select Mode (1 -> 10), Quit (q), or List Modes (lm)? ').replace(' ', ''))
        if type(mode) == int:

            graph = Conjecture(number_range=(int(input('start number: ')), int(input('how many numbers :) ?'))), rand_color=True, make_sequence=True, do_graph=True)
            print(graph)
            graph.draw_graph()

        elif mode.lower()[0] == 'q':
            break

        elif mode.lower() == 'lm':
            print('''
1. Preformance Mode
2. Connected Dot Graph
''')

        else:
            print('Please Select an Option')

if __name__ == '__main__':
    main()