'''
this script will be used as decorator function to measure runtime of decorated function.
'''


from Fibanacci import fibanacci_recursive as slow_function
import datetime


def timebench():
    def covered(function):
        start_time = datetime.datetime.now()
        function()
        end_time = datetime.datetime.now()
        timedelta = end_time - start_time
        print("Run time: %s ms" % str(timedelta))
    return covered



def makelist(sizeof=1000):
    i = [i for i in range(sizeof+1)]
    return i






def main():
    @timebench()
    makelist()


if __name__ == "__main__":
    main()
