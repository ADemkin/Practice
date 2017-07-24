import itertools

i = [i for i in range(10)]

#print(i)


t = itertools.tee(i, 2)

for p in t:





def main():
    pass


if __name__ == "__main__":
    main()
