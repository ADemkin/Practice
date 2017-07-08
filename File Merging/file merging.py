# Задача от Олега
# Anton Demkin, 2017
#
# Задача объединить два текстовых файла с цифрами в один.

import random


def create_files():
    '''
    Create two files: text1.txt and text2.txt.
    Both files are filled with random numbers separated by new lines.
    '''
    with open('file1.txt', 'w') as f:
        for i in range(10):
            r = random.randint(0,1000)
            f.write(str(r) + '\n')
    
    with open('file2.txt', 'w') as f:
        for i in range(10):
            r = random.randint(0,1000)
            f.write(str(r) + '\n')


#create_files()

def merge_files():
    '''
    Create file3.txt with numbers from file1.txt and file2.txt
    '''
    with open('file3.txt', 'w') as result:
        with open('file1.txt', 'r') as file1:
            with open('file2.txt', 'r') as file2:
                for line1, line2 in zip(file1, file2):
                    # simply merge data, no sorting here
                    result.write(str(line1) + str(line2))

                    
merge_files()

