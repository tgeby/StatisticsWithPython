import math
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

dataset = [21,24,24,27,29]
# What is the standard deviation?
print(round(calculate_standard_deviation(dataset=dataset), 2))
