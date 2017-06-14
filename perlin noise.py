from random import randint


def perlin_noise_gen(length=170, lowest=-50, highest=50, step=1):
    arr = []
    next = (lowest + highest) / 2
    for i in range(0, length):
        next_step = randint(-step, step)
        while (next + next_step) not in range(lowest, highest):
            next_step = randint(-1, 1)
        next = next + next_step
        int(next)
        arr.append(next)
    return arr


def find_range(list):
    minimum = min(list)
    maximum = max(list)
    range = maximum - minimum
    return range


def perlin_noise_visualisation(noise):
    diff = int(find_range(noise))
    for level in range(0,diff):
        for i in range(0, len(noise)):
            if noise[i] >= level+min(noise):
                step = ' '
            else:
                step = '@'
            print(step, end='')
            if i == len(noise) - 1:
                print('\n', end='')
    for i in range(0, len(noise)):
        print('@', end='')




noise = perlin_noise_gen()
print(noise)
print(find_range(noise))
perlin_noise_visualisation(noise)
