'''
This scripts calculates maximum chain length for a red, black or zero in a roulette game
'''

from random import randint
import datetime

results = []
rounds = 10 ** 6
start_time = datetime.datetime.now()
target = -1


def main():
    for i in range(0, rounds):
        # generate roulette
        current = randint(0, 37)
        # interpretate values:
        if current == 0:
            results.append(0)
        if current > 0 and current < 19:
            results.append(-1)
        else:
            results.append(0)
    
    # print(results) # working
    # reds = list(filter(lambda x:(x == -1), results))  # FUCKING REMEMBER HOW TO WRITE THIS STUFF, NOOB!!!
    # print("%d / %d" % (len(reds), len(results)))  # working
    chain_length = 0
    max_chain_length = 0
    
    for i in range(0, len(results)):
        for j in range(i, len(results)):
            if results[j] == target:
                chain_length += 1
            else:
                break
        if chain_length > max_chain_length:
            max_chain_length = chain_length
        chain_length = 0
    
    # replace target with interpretation
    if target == -1:
        target_name = 'reds'
    elif target == 1:
        target_name = 'blacks'
    else:
        target_name = 'zero'
    
    print("Maximum chain length of %s in set of %d is %d." % (target_name, len(results), max_chain_length))
    
    # Calculate working time
    finish_time = datetime.datetime.now()
    working_time = finish_time - start_time
    seconds = divmod(working_time.total_seconds(), 60)
    print("Calculated in %.0f m %.2f s." % (seconds))


if __name__ == "__main__":
    main()
