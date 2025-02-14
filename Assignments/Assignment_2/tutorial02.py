# All decimal 3 places

from math import sqrt

# Function to compute sum. You cant use Python functions
def summation(first_list = []):
    if(not all(isinstance(x, (int, float)) for x in first_list)): return 0

    summation_value = 0
    for _ in first_list:
        summation_value += _

    return summation_value

def sorting(first_list = []):
    if(not all(isinstance(x, (int, float)) for x in first_list)): return 0
    sorted_list = first_list[:]
    for i in range(0, len(sorted_list)):
        min_index = i
        for j in range(i+1, len(sorted_list)):
            if(sorted_list[min_index] > sorted_list[j]):
                min_index = j
        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]

    return sorted_list


# Function to compute mean
def mean(first_list = []):
    if(not all(isinstance(x, (int, float)) for x in first_list)): return 0

    mean_value = summation(first_list)/len(first_list)

    return mean_value


# Function to compute median. You cant use Python functions
def median(first_list = []):
    if(not all(isinstance(x, (int, float)) for x in first_list)): return 0
    sorted_list = sorting(first_list)
    median_value = 0
    num_of_elems = len(sorted_list)
    if(num_of_elems % 2 == 1):
        median_value = sorted_list[num_of_elems//2]
    else:
        median_value = (sorted_list[(num_of_elems//2) - 1] + sorted_list[(num_of_elems//2)]) / 2
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list = []):
    if(not all(isinstance(x, (int, float)) for x in first_list)): return 0
    u = mean(first_list)
    standard_deviation_value = sqrt((summation([(x-u) ** 2 for x in first_list]))/len(first_list))
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list = []):
    if(not all(isinstance(x, (int, float)) for x in first_list)): return 0
    u = mean(first_list)
    variance_value = standard_deviation(first_list) ** 2
    return variance_value

# Function to compute mse. You cant use Python functions
def mse(first_list = [], second_list = []):
    if(not all(isinstance(x, (int, float)) for x in first_list)): return 0
    if(not all(isinstance(x, (int, float)) for x in second_list)): return 0
    if(len(first_list) != len(second_list)): return 0

    mse_value = summation([(x-y) ** 2 for x, y in zip(first_list, second_list)])/len(first_list)

    return mse_value

# Function to compute RMSE. You cant use Python functions
def rmse(first_list = [], second_list = []):
    if(not all(isinstance(x, (int, float)) for x in first_list)): return 0
    if(not all(isinstance(x, (int, float)) for x in second_list)): return 0
    if(len(first_list) != len(second_list)): return 0

    rmse_value = sqrt(mse(first_list, second_list))

    return rmse_value

# Function to compute mae. You cant use Python functions
def mae(first_list = [], second_list = []):
    if(not all(isinstance(x, (int, float)) for x in first_list)): return 0
    if(not all(isinstance(x, (int, float)) for x in second_list)): return 0
    if(len(first_list) != len(second_list)): return 0

    mae_value = summation([ abs(x-y) for x, y in zip(first_list, second_list)]) / len(first_list)

    return mae_value

# Function to compute NSE. You cant use Python functions
def nse(first_list = [], second_list = []):
    if(not all(isinstance(x, (int, float)) for x in first_list)): return 0
    if(not all(isinstance(x, (int, float)) for x in second_list)): return 0
    if(len(first_list) != len(second_list)): return 0

    nse_value = 1 - (mse(first_list, second_list) / (standard_deviation(first_list) ** 2))

    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list = [], second_list = []):
    if(not all(isinstance(x, (int, float)) for x in first_list)): return 0
    if(not all(isinstance(x, (int, float)) for x in second_list)): return 0
    if(len(first_list) != len(second_list)): return 0

    _x = mean(first_list)
    _y = mean(second_list)

    numerator = summation([(x-_x)*(y-_y) for x, y in zip(first_list, second_list)])
    denominator = sqrt(summation([(x-_x) ** 2 for x in first_list])) * sqrt(summation([(y-_y) ** 2 for y in second_list]))
    
    pcc_value = numerator/ denominator

    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list = []):
    if(not all(isinstance(x, (int, float)) for x in first_list)): return 0

    _x = mean(first_list)
    std = standard_deviation(first_list)
    n = len(first_list)

    skewness_value = summation( [((x-_x)/std) ** 3 for x in first_list] )/n

    return skewness_value
    

# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list = []):
    if(not all(isinstance(x, (int, float)) for x in first_list)): return 0

    _x = mean(first_list)
    std = standard_deviation(first_list)
    n = len(first_list)

    kurtosis_value = summation( [((x-_x)/std) ** 4 for x in first_list] )/n

    return kurtosis_value




