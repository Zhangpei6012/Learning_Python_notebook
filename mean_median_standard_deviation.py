# Written by Eric Martin for COMP9021


'''
Prompts the user for a strictly positive integer, nb_of_elements,
generates a list of nb_of_elements random integers between -50 and 50, prints out the list,
computes the mean, the median and the standard deviation in two ways,
that is, using or not the functions from the statistics module, and prints them out.
'''


from random import seed, randint
from math import sqrt
from statistics import mean, median, pstdev
import sys

try:
    arg_for_seed = int(input('Input a seed for the random number generator: '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
try:
    nb_of_elements = int(input('How many elements do you want to generate? '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()


seed(arg_for_seed)
L = [randint(-50, 50) for _ in range(nb_of_elements)]
print('\nThe list is:' , L)
print()

#calculate mean
num_mean = sum(L) / nb_of_elements
print(f'The mean is {num_mean:.2f}.')

#calculate median
sort_L = sorted(L)
if (nb_of_elements % 2) == 0:
	num_median = (sort_L[nb_of_elements//2] + sort_L[nb_of_elements//2 - 1])/2
else:
	num_median = sort_L[nb_of_elements//2]
print(f'The median is {num_median:.2f}.')

#calculate sd
num_sd= sqrt(sum([(x - num_mean)**2 for x in L]) / nb_of_elements)
#num_sd = sqrt(num_sum_square / nb_of_elements)
print(f'The standard deviation is {num_sd:.2f}.')
print()
print('Confirming with functions from the statistics module:')
print(f'The mean is {mean(L):.2f}.')
print(f'The median is {median(L):.2f}.')
print(f'The standard deviation is {pstdev(L):.2f}.')

