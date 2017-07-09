# Задача от Олега
# Anton Demkin, 2017
#
# Задача объединить два текстовых файла с цифрами в один.

import random
import sys


def create_files():
    '''
    Create two files: text1.txt and text2.txt.
    Both files are filled with random numbers separated by new lines.
    '''
    length = 5
    gap = 6
    
    with open('file1.txt', 'w') as f:
        r = 0
        for i in range(length):
            r += random.randint(0, gap)
            f.write(str(r) + '\n')
    
    with open('file2.txt', 'w') as f:
        r = 0
        for i in range(length):
            r += random.randint(0, gap)
            f.write(str(r) + '\n')


def merge_files(file1, file2):
    '''
    returns list with file1 and file2 sorted data
    '''
    # create new list
    new_list = []
    
    # read first lines
    next1 = file1.readline()
    next2 = file2.readline()
    
    # check if file end is reached
    while next1 is not '' and next2 is not '':
        
        # compare and get next value
        if next1 < next2:
            new_list.append(next1)
            next1 = file1.readline()
        else:
            new_list.append(next2)
            next2 = file2.readline()
    
    # check for end file individually
    if next1 is '':
        while next2 is not '':
            new_list.append(next2)
            next2 = file2.readline()
    if next2 is '':
        while next1 is not '':
            new_list.append(next1)
            next1 = file1.readline()
    
    # end
    return new_list


def open_files_to_sort():
    '''
    Create file3.txt with numbers from opened files.
    '''
    with open('file3.txt', 'w') as result:
        with open(sys.argv[1], 'r') as file1:
            with open(sys.argv[2], 'r') as file2:
                newlist = merge_files(file1, file2)
                for number in newlist:
                    result.write(number)


def main():
    create_files()
    open_files_to_sort()


if __name__ == '__main__':
    main()