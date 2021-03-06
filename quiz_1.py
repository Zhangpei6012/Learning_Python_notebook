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


#quiz3

# Uses Global Temperature Time Series, avalaible at
# http://data.okfn.org/data/core/global-temp, stored in the file monthly_csv.csv,
# assumed to be stored in the working directory.
# Prompts the user for the source, a year or a range of years, and a month.
# - The source is either GCAG or GISTEMP.
# - The range of years is of the form xxxx -- xxxx (with any number of spaces,
#   possibly none, around --) and both years can be the same,
#   or the first year can be anterior to the second year,
#   or the first year can be posterior to the first year.
# We assume that the input is correct and the data for the requested month
# exist for all years in the requested range.
# Then outputs:
# - The average of the values for that source, for this month, for those years.
# - The list of years (in increasing order) for which the value is larger than that average.
#
# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv
import datetime
from collections import defaultdict


filename = 'monthly_csv.csv'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

source = input('Enter the source (GCAG or GISTEMP): ')
year_or_range_of_years = input('Enter a year or a range of years in the form XXXX -- XXXX: ')
month = input('Enter a month: ')
average = 0
years_above_average = []

# REPLACE THIS COMMENT WITH YOUR CODE
time_list = []
def nums_to_english(time):
    try:
        time_format = datetime.datetime.strptime(time, '%Y/%m/%d')
    except ValueError:
        time_format = datetime.datetime.strptime(time, '%Y-%m-%d')
    time_format = time_format.strftime('%Y/%B/%d')
    return time_format

year_or_range_of_years = ''.join(year_or_range_of_years.split()) #del space
year_or_range_of_years = [int(x) for x in year_or_range_of_years.split('--',1)]
#year_or_range_of_years.sort()

dir_year_nums = defaultdict(list)

with open('monthly_csv.csv') as file:
    csv_file = csv.reader(file)
    for source_name, date_time, mean_nums in csv_file:
        if str(source_name) == source:
            time_format = nums_to_english(str(date_time))
            time_list = [x for x in time_format.split('/')]
            if time_list[1] == str(month):
                if min(year_or_range_of_years)<= int(time_list[0]) <= max(year_or_range_of_years)
                    dir_year_nums[int(time_list[0])].append(float(mean_nums))
                    time_list.clear()
"""
                if len(year_or_range_of_years) == 1 and int(time_list[0])== year_or_range_of_years[0]:
                    dir_year_nums[int(time_list[0])].append(float(mean_nums))
                    time_list.clear()
                elif len(year_or_range_of_years) == 2 and year_or_range_of_years[1]>= int(time_list[0]) >= year_or_range_of_years[0]:
                    dir_year_nums[int(time_list[0])].append(float(mean_nums))
                    time_list.clear()
"""
sum_mean = sum(dir_year_nums[key][0] for key in dir_year_nums)
average = sum_mean / len(dir_year_nums)
years_above_average = [key for key in dir_year_nums if dir_year_nums[key][0] > average]
years_above_average.sort()

print(f'The average anomaly for {month} in this range of years is: {average:.2f}.')
print('The list of years when the temperature anomaly was above average is:')
print(years_above_average)


##quiz4
# Randomly fills an array of size 10x10 with True and False, and outputs the number of blocks
# in the largest block construction, determined by rows of True's that can be stacked
# on top of each other.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end = '')
        print(' '.join(f'{int(e)}' for e in grid[i]))
    print()

def construction_size(i, j1, j2):
    block1 = 0
    for m in range(j1, j2 + 1):
        for n in reversed(range(0,i)):
            if not grid[n][m]:
                break
            else:
                block1 += 1
    return (block1)


def size_of_largest_construction():
    largest_size = 0
    for i in range(len(grid))[::-1]:
        for j1 in range(len(grid[i])):
            for j2 in range(j1, len(grid[i])):
                if all(grid[i][j1:j2+1]):
                    temp_size = j2 - j1 + 1 + (construction_size(i, j1, j2))
                    largest_size = max(temp_size, largest_size)
                    temp_size = 0
    return (largest_size)
# If j1 <= j2 and the grid has a 1 at the intersection of row i and column j
# for all j in {j1, ..., j2}, then returns the number of blocks in the construction
# built over this line of blocks.






try:
    for_seed, n = input('Enter two integers, the second one being strictly positive: ').split()
    for_seed = int(for_seed)
    n = int(n)
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[bool(randrange(n)) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_construction()
if not size:
    print(f'The largest block construction has no block.')
elif size == 1:
    print(f'The largest block construction has 1 block.')
else:
    print(f'The largest block construction has {size_of_largest_construction()} blocks.')

##quiz5
 # Prompts the user for a nonnegative integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived nonnegative number that codes the set of running sums
# of the members of S when those are listed in increasing order.
#
# Computes the ordered list of members of a coded set.
#
# Written by *** and Eric Martin for COMP9021


import sys

try:
    encoded_set = int(input('Input a nonnegative integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

def display(L):
    print('{', end = '')
    print(', '.join(str(e) for e in L), end = '')
    print('}')

def decode(encoded_set):
    i = 0
    list1 = []
    while i <= len(bin(encoded_set)):
        if bin(encoded_set|1 << i) == bin(encoded_set):
            if i % 2 == 0:
                list1.append(int(i/2))
            else:
                list1.append(int(-(i+1)/2))
        i += 1
    list1.sort()
    return list1

def code_derived_set(encoded_set):
    i = 0
    list2 = decode(encoded_set)
    list3 = []
    nums = 0
    if len(list2) != 0:
        while i <= len(list2):
            list3.append(sum(list2[:i+1]))
            i += 1
        list3 = sorted(set(list3))
        for x in list3:
            if x >= 0 :
                nums = nums|1 << (x * 2)
            else:
                nums = nums|1 << abs(x) * 2 - 1
    return nums
print('The encoded set is: ', end = '')
display(decode(encoded_set))
code_of_derived_set = code_derived_set(encoded_set)
print('The derived set is encoded as:', code_of_derived_set)
print('It is: ', end = '')
display(decode(code_of_derived_set))


###quiz6

# Randomly fills an array of size 10x10 True and False, displayed as 1 and 0,
# and outputs the number chess knights needed to jump from 1s to 1s
# and visit all 1s (they can jump back to locations previously visited).
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end = '')
        print(' '.join(grid[i][j] and '1' or '0' for j in range(dim)))
    print()

direction = [[-2 ,-1],[-2 , 1],[-1, 2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]

def explore_board(x,y):
    global name
    if not (0 <= x < 10 and 0 <= y < 10 ):
        return
    if grid[x][y] != 1:
        return
    grid[x][y] = 0
    for i in range(8):
        explore_board(x+direction[i][0],y+direction[i][1])
    grid[x][y] = name

try:
    for_seed, n = (int(i) for i in input('Enter two integers: ').split())
    if not n:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
if n > 0:
    grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
else:
    grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

name = 2
for i in range(10):
    for j in range(10):
        if grid[i][j] == 1:
            explore_board(i,j)
            name += 1

nb_of_knights = name - 2
if not nb_of_knights:
    print('No chess knight has explored this board.')
elif nb_of_knights == 1:
    print(f'At least 1 chess knight has explored this board.')
else:
    print(f'At least {nb_of_knights} chess knights have explored this board')
