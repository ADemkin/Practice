# ask user for initial sum, year percentage and how many years

'''
deposit = 0
percentage = 0
years = 0
'''


def main():
    deposit = int(input('Enter sum to deposit: '))
    percentage = float(input('Enter annual %: ')) / 100
    years = int(input('Enter length of deposit in years: '))
    
    for i in range(1, years + 1):
        deposit = deposit * percentage + deposit
        if i < 10:
            j = '0'
        else:
            j = ''
        print('Year: %s%d. Sum: %.2f' % (j, i, deposit))


if __name__ == "__main__":
    main()
