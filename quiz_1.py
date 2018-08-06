# Written by *** and Eric Martin for COMP9021



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
     )
print('The maximal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {max_gap}.')
print()
print('The number of pairs (f, l) such that f and l are the first and last digits\n'
      f'of members of L is maximal for (f, l) one of {sorted(first_and_last)}.'
     )
