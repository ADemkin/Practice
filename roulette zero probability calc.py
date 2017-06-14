# roulette has a 36 slots and one of them is zero (0).
# this scrips plays 100 roulette rounds and add all results to list
# after 100 rounds played scrips calculates a prints zero(0) probability based on 100 rounds played

from random import randint
import datetime

results = []
rounds = 10**9
start_time = datetime.datetime.now()

def main():
    for i in range(0, rounds):
        current = randint(0, 36)
        results.append(current)
    # print(results) # working
    # print(len(results)) # 100
    zeros = list(filter(lambda x:(x == 0), results))  # FUCKING REMEMBER HOW TO WRITE THIS STUFF, NOOB!!!
    print("%d / %d" % (len(zeros), len(results)))  # working
    # to print a percentage you need to cover it with another % sign, print('%d%%' % 33) # -> 33%
    
    probability = len(zeros) / len(results) * 100
    print("In a row of %d there are a %.2f%% probability of zero" % (rounds, probability))
    finish_time = datetime.datetime.now()
    working_time = finish_time - start_time
    seconds = divmod(working_time.total_seconds(), 60)
    print("Calculated in %.0f m %.2f s." % (seconds))


if __name__ == "__main__":
    main()
