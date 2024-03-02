#  This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.


def simple_multiplication(number) :
    if number % 2 == 0:
        sum = number * 8
    else:
        sum = number * 9
    return sum

print(simple_multiplication(11))