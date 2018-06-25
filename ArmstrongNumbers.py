import math
import time

startTime = time.time()

AMOUNT_OF_SIMPLE_DIGITS = 10  # from 0 to 9
MAX_NUMBER = 2147483647


def digits_amount(number):
    return int(math.log10(number)) + 1


# create 2D array not to use pow(i, j) for each iteration
arrayOfPowers = [[pow(i, j) for j in range(0, digits_amount(MAX_NUMBER) + 2)] for i in range(0, AMOUNT_OF_SIMPLE_DIGITS)]

assert pow(9, 4) == 6561
assert arrayOfPowers[9][4] == 6561
assert pow(0, 0) == 1
assert arrayOfPowers[0][0] == 1
assert arrayOfPowers[2][2] == 4


def get_next_number(number):
    tmp_number = number
    if is_growing_number(tmp_number):
        return tmp_number + 1

    # here we have numbers which end in zero: 10, 20, ..., 100, 110, 5000, 1000000 and so on.
    last_number = 1
    while tmp_number % 10 == 0:
        tmp_number //= 10
        last_number = last_number * 10
    last_non_zero_digit = tmp_number % 10
    return number + last_non_zero_digit * last_number // 10


#  135 returns true:  1 < 3 < 5
#  153 returns false: 1 < 5 > 3
def is_growing_number(number):
    return (number + 1) % 10 != 1


def get_sum_of_powers(number):
    current_number = number
    power = digits_amount(current_number)
    current_sum = 0
    while current_number > 0:
        # get powers from array by indexes and then the sum.
        current_sum = current_sum + arrayOfPowers[current_number % 10][power]
        current_number //= 10

    return current_sum


def is_armstrong_number(number):
    return number == get_sum_of_powers(number)


armstrong = set()
n = 1
while n < MAX_NUMBER:
    sum_of_powers = get_sum_of_powers(n)
    if is_armstrong_number(sum_of_powers):
        armstrong.add(sum_of_powers)
    n = get_next_number(n)

for n in sorted(armstrong):
    print(n)

print("Execution time: %.3f seconds" % (time.time() - startTime))
