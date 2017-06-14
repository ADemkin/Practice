from random import randint


def make_random_list(length):
    arr = []
    for i in range(0, length):
        arr.append(randint(0, 100))
    return arr


def find_lowest_index(list):
    lowest = list[0]
    lowest_index = 0
    for i in range(0, len(list)):
        if list[i] < lowest:
            lowest = list[i]
            lowest_index = i
    return lowest_index


def some_kind_of_sort(list):
    new_array = []
    for i in range(0, len(list)):
        lowest_index = find_lowest_index(list)
        lowest = list[lowest_index]
        new_array.append(lowest)
        list.pop(lowest_index)
    return new_array


array = make_random_list(20)
print(array)
print(some_kind_of_sort(array))


def main():
    pass


if __name__ == "__main__":
    main()
