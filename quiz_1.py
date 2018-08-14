# Written by *** and Eric Martin for COMP9021
#quiz1

#Generates a natural number and a list of natural numbers and outputs a number of their properties.


import sys
from random import seed, randrange
#5.2 requared
#from collections import Counter



try:
    arg_for_seed = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
x = randrange(10 ** 10)
sum_of_digits_in_x = 0
L = [randrange(10 ** 8) for _ in range(10)]
first_digit_greater_than_last = 0
same_first_and_last_digits = 0
last_digit_greater_than_first = 0
distinct_digits = [0] * 9
min_gap = 10
max_gap = -1
first_and_last = set()

# REPLACE THIS COMMENT WITH YOUR CODE
# 1
sum_of_digits_in_x = sum(int(i) for i in str(x))
# 2
for nums in L:
    if str(nums)[0] > str(nums)[-1]:
        first_digit_greater_than_last += 1
    elif str(nums)[0] < str(nums)[-1]:
        last_digit_greater_than_first +=1
    elif str(nums)[0] == str(nums)[-1]:
        same_first_and_last_digits += 1


# 3
for nums in L:
    set_num = set(str(nums))
    distinct_digits[len(set_num)] += 1

# 4
gap = [0] * 10
for i,nums1 in enumerate(L):
    gap[i] = abs(int(str(nums1)[0]) - int(str(nums1)[-1]))
min_gap = min(gap)
max_gap = max(gap)


# 5
list_pair = [0] * 10
# 5.1
list_max  = [0] * 10
counter   = 0
for i,nums2 in enumerate(L):
    list_pair[i] = (int(str(nums2)[0]),int(str(nums2)[-1]))

for num3 in list_pair:
    if list_pair.count(num3) > counter:
        counter = list_pair.count(num3)
        list_max.clear()
        list_max.append(num3)
    elif list_pair.count(num3) == counter:
        list_max.append(num3)

first_and_last = set(list_max)
# 5.2
"""
first_and_last_list_max = Counter(list_pair).most_common(1)
first_and_last_dic_max = dict(first_and_last_list_max)
max_value ， = first_and_last_dic_max.values()
if max_value == 1:
    first_and_last = list_pair
else:
    first_and_last_list = Counter(list_pair).most_common(10)
    first_and_last_dic = dict(first_and_last_list)
    first_and_last_dic_copy = dict(first_and_last_list)
    for key in first_and_last_dic_copy :
        if first_and_last_dic_copy[key] != max_value :
           del first_and_last_dic[key]

    first_and_last = list(first_and_last_dic)
"""









print()
print('x is:', x)
print('L is:', L)
print()
print(f'The sum of all digits in x is equal to {sum_of_digits_in_x}.')
print()
print(f'There are {first_digit_greater_than_last}, {same_first_and_last_digits} '
      f'and {last_digit_greater_than_first} elements in L with a first digit that is\n'
      '  greater than the last digit, equal to the last digit,\n'
      '  and smaller than the last digit, respectively.'
     )
print()
for i in range(1, 9):
    if distinct_digits[i]:
        print(f'The number of members of L with {i} distinct digits is {distinct_digits[i]}.')
print()
print('The minimal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {min_gap}.'



#quiz2

# Written by *** and Eric Martin for COMP9021
#Generates a nonempty list L of pairs natural numbers and outputs a number of properties of fractions built from members of L.


import sys
from random import seed, randint
from math import gcd


try:
    arg_for_seed, length, max_value = input('Enter three strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 1 or length < 1 or max_value < 1:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(1, max_value) for _ in range(length)]
print('Here is L:')
print(L)
print()

size_of_simplest_fraction = None
simplest_fractions = []
size_of_most_complex_fraction = None
most_complex_fractions = []
multiplicity_of_largest_prime_factor = 0
largest_prime_factors = []

# REPLACE THIS COMMENT WITH YOUR CODE


def transform_fraction(num1, num2):
    if num1 == 0:
        return 0,1
    return num1//gcd(num1, num2), num2//gcd(num1, num2)

list_fractions= []
for i in L:
    for j in L:
        if i <= j :
            list_fractions.append(transform_fraction(i,j))


list_fractions_norepeat = list(set(list_fractions))
list_fractions_norepeat.sort(key = lambda x:(len(str(x[0]))+len(str(x[1]))))

size_of_simplest_fraction = len(str(list_fractions_norepeat[0][0])+str(list_fractions_norepeat[0][1]))
size_of_most_complex_fraction = len(str(list_fractions_norepeat[-1][0])+str(list_fractions_norepeat[-1][1]))


simplest_fractions_orgin =[x for x in list_fractions_norepeat if (len(str(x[0]))+len(str(x[1]))) == size_of_simplest_fraction]
most_complex_fractions_orgin=[x for x in list_fractions_norepeat if (len(str(x[0]))+len(str(x[1]))) == size_of_most_complex_fraction]

simplest_fractions = sorted(simplest_fractions_orgin, key= lambda x:(x[0]/x[1]))
most_complex_fractions = sorted(most_complex_fractions_orgin, key = lambda x:(x[0]/x[1]), reverse = True)

dir_primefactors={}
def f(n):
    n=int(n)
    for i in range(2,n+1):
        if n%i==0:
            try:
                dir_primefactors[i] += 1
            except KeyError:
                dir_primefactors[i] = 1
            return f(n/i)


temp = 1
largest_prime_factors_org = []
for x in most_complex_fractions:
    f(x[1])
    if dir_primefactors == {}:
        temp = 0
    else:
        max_key = dir_primefactors[max(dir_primefactors, key = lambda k : dir_primefactors[k])]
        for key in dir_primefactors:
            if dir_primefactors[key] == max_key and max_key == temp :
                largest_prime_factors_org.append(key)
            elif dir_primefactors[key] == max_key and max_key > temp :
                largest_prime_factors_org.clear()
                largest_prime_factors_org.append(key)
                temp = max_key
        dir_primefactors.clear()

largest_prime_factors = sorted(list(set(largest_prime_factors_org)))
multiplicity_of_largest_prime_factor = temp


print('The size of the simplest fraction <= 1 built from members of L is:',
      size_of_simplest_fraction
     )
print('From smallest to largest, those simplest fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in simplest_fractions))
print('The size of the most complex fraction <= 1 built from members of L is:',
      size_of_most_complex_fraction
     )
print('From largest to smallest, those most complex fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in most_complex_fractions))
print("The highest multiplicity of prime factors of the latter's denominators is:",
      multiplicity_of_largest_prime_factor
     )
print('These prime factors of highest multiplicity are, from smallest to largest:')
print('   ', largest_prime_factors)

     )
print('The maximal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {max_gap}.')
print()
print('The number of pairs (f, l) such that f and l are the first and last digits\n'
      f'of members of L is maximal for (f, l) one of {sorted(first_and_last)}.'
     )
