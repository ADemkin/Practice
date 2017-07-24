import random


def random_numbers(high=1000):
    while True:
        yield random.randint(0, high)

# for i in random_numbers():
#     print(i)


def return_one_two_three():
    yield 1
    yield 2
    yield 3
    

it123 = return_one_two_three()
# print(it123)
# # -> <generator object return_one_two_three at 0x102269bf8>
# print(next(it123))
# # -> 1
# print(next(it123))
# # -> 2
# print(next(it123))
# # -> 3
# print(next(it123))
# # -> StopIteration

nums = (i for i in range(10))

while True:
    try:
        number = next(nums)
        print(number)
    except StopIteration:
        print('out of values')
        break