'''
I have learned that two good ways of evaluating central tendencies of an array of values are
using the mean and standard deviation or the median and inter-quartile-range. This script 
takes in a list of values and displays the mean, standard deviation, median, and IQR.
'''

import sys
import math

if len(sys.argv) < 2:
    print("Incorrect usage: please include a comma separated list of numbers as an argument.")

def clean_arg(arg):
    arg = arg.split(',')
    result = []
    for i in range(0,len(arg)):
        stripped = arg[i].strip()
        try:
            stripped = int(stripped)
            result.append(stripped)
        except:
            pass
    return result

def get_values():
    values = []
    for i in range(1, len(sys.argv)):
        cleaned_argument = clean_arg(sys.argv[i])
        for i in cleaned_argument:
            values.append(int(i))
    return values

def calculate_mean(dataset):
    result = 0
    for i in dataset:
        result += i
    result /= len(dataset)
    return result

def calculate_variance(dataset):
    result = 0
    mean = calculate_mean(dataset=dataset)
    for i in dataset:
        result += (i - mean) ** 2
    result /= len(dataset)
    return result

def calculate_standard_deviation(dataset):
    variance = calculate_variance(dataset=dataset)
    standard_deviation = math.sqrt(variance)
    return standard_deviation

def calculate_median(dataset):
    dataset.sort()
    is_even = True if len(dataset) % 2 == 0 else False
    middle_index = len(dataset) // 2
    result = dataset[middle_index]
    if is_even:
        result += dataset[middle_index - 1]
        result /= 2
    return result

def calculate_IQR(dataset):
    dataset.sort()
    is_even = True if len(dataset) % 2 == 0 else False
    middle_index = len(dataset) // 2
    first_half = dataset[0:middle_index]
    second_half = []
    if is_even:
        second_half = dataset[middle_index:]
    else:
        second_half = dataset[middle_index + 1:]
    return abs(calculate_median(dataset=first_half) - calculate_median(dataset=second_half))

values = get_values()
mean = calculate_mean(dataset=values)
standard_deviation = calculate_standard_deviation(dataset=values)
median = calculate_median(dataset=values)
IQR = calculate_IQR(dataset=values)
print(f"\n\n\nMean: {mean}\nStandard deviation: {standard_deviation}\n\n")
print(f"\n\n\Median: {median}\nIQR: {IQR}\n\n")