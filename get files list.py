# /Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
# -*- coding: utf8 -*-
'''
A very simple script to get list of all files in a working dir and write all file names into Files_list.txt,
which will be created in a working dir.

Anton Demkin, 2017

'''

import os

files = []
path = ''
exclude = ['.asd', 'Files_list.txt', 'get files list.py']


def main():
    path = os.getcwd()
    files_list = os.listdir(path)
    
    with open('Files_list.txt', 'w') as file:
        for line in files_list:
            if line[0] == '.':
                continue
            elif exclude in line:
                continue
            file.write(line + '\n')


if __name__ == "__main__":
    main()
