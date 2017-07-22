# a program prints out 'Fizz' if number is divisable by 3,
# 'Buzz' if number divisable by 5
# and 'FizzBuzz' if a number divisable by both

def fizzbuzz(number):
    for i in range(0, number):
        if i % 5 == 0 & i % 3 == 0:
            print('FizzBuzz: ', i)
        elif i % 3 == 0:
            print('Fizz:', i)
        elif i % 5 == 0:
            print('Buzz:', i)


def main():
    fizzbuzz(150)


if __name__ == "__main__":
    main()
