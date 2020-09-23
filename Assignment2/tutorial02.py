# All decimal 3 places

# Function to compute sum. You cant use Python functions
def summation(first_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0

    mean_value = 0
    for _ in first_list:
        mean_value += _

    return summation_value

def sorting(first_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0

    for i in range(0, len(first_list)):
        min_index = i
        for j in range(i+1, len(first_list)):
            if(first_list[min_index] > first_list[j]):
                min_index = j
        first_list[i], first_list[min_index] = first_list[min_index], first_list[i]

    sorted_list = first_list
    return sorted_list


# Function to compute mean
def mean(first_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0

    mean_value = summation(first_list)/len(first_list)

    return mean_value


# Function to compute median. You cant use Python functions
def median(first_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0
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
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0
    u = mean(first_list)
    standard_deviation_value = sqrt((summation([(x-u) ** 2 for x in first_list]))/len(first_list))
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0
    variance_value = (summation([(x-u) ** 2 for x in first_list])/(len(first_list)-1))
    return variance_value

# Function to compute mse. You cant use Python functions
def mse(first_list = [], second_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0
    if(not any(isinstance(x, (int, float)) for x in second_list)): return 0
    if(len(first_list) != len(second_list)): return 0

    mse_value = summation([(x-y) ** 2 for x, y in zip(first_list, second_list)])/len(first_list)

    return mse_value

# Function to compute RMSE. You cant use Python functions
def rmse(first_list = [], second_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0
    if(not any(isinstance(x, (int, float)) for x in second_list)): return 0

    return rmse_value

# Function to compute mae. You cant use Python functions
def mae(first_list = [], second_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0
    if(not any(isinstance(x, (int, float)) for x in second_list)): return 0

    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list = [], second_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0
    if(not any(isinstance(x, (int, float)) for x in second_list)): return 0

    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list = [], second_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0
    if(not any(isinstance(x, (int, float)) for x in second_list)): return 0

    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0

    return skewness_value
    

# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0

    return kurtosis_value
