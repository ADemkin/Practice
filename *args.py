# print out individual elements of lists inside lists

from random import randint as rnd

def create_nested_list():
    if rnd(0,1) == 0:
        x=  rnd(0,10)
    else:
        x= create_nested_list()
    return [x for i in range(0,rnd(0,5))]


def print_nested_list_recursive(lists,indentation=0):
    #print('new list:', lists)
    for number, element in enumerate(lists):
        if type(element) == list:
            print_nested_list_recursive(element, indentation+4)
        else:
            spaces = ''
            for i in range(0,indentation):
                spaces += ' '
            print("%s %s: %s" % (spaces, number, element))

def print_nested_list_linear(*args):
    for element in args:
        if len(element) == 1:
            print(element)
        else:
            print_nested_list_linear(element)
            print(element)






def main():
    list = create_nested_list()
    #print(list)
    #print_nested_list_recursive(list)
    #print_nested_list_recursive([1,[1,[1,1]],[2,[2,2]],[[3,[3,[3]],3]],24])
    print_nested_list_linear([1,[1,[1,1]],[2,[2,2]],[[3,[3,[3]],3]],24])


if __name__ == "__main__":
    main()
