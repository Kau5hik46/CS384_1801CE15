# All decimal 3 places

# Function to compute mean
def mean(first_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0

    return round(mean_value, 3)


# Function to compute median. You cant use Python functions
def median(first_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0

    return round(median_value, 3)


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0

    return round(standard_deviation_value, 3)


# Function to compute variance. You cant use Python functions
def variance(first_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0

    return round(variance_value, 3)


# Function to compute RMSE. You cant use Python functions
def rmse(first_list = [], second_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0
    if(not any(isinstance(x, (int, float)) for x in second_list)): return 0

    return round(rmse_value, 3)


# Function to compute mse. You cant use Python functions
def mse(first_list = [], second_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0
    if(not any(isinstance(x, (int, float)) for x in second_list)): return 0

    return round(mse_value, 3)


# Function to compute mae. You cant use Python functions
def mae(first_list = [], second_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0
    if(not any(isinstance(x, (int, float)) for x in second_list)): return 0

    return round(mae_value, 3)


# Function to compute NSE. You cant use Python functions
def nse(first_list = [], second_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0
    if(not any(isinstance(x, (int, float)) for x in second_list)): return 0

    return round(nse_value, 3)


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list = [], second_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0
    if(not any(isinstance(x, (int, float)) for x in second_list)): return 0

    return round(pcc_value, 3)


# Function to compute Skewness. You cant use Python functions
def skewness(first_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0

    return round(skewness_value, 3)
    
def sorting(first_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0

    return [round(num, 3) for num in sorted_list]


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0

    return round(kurtosis_value, 3)


# Function to compute sum. You cant use Python functions
def summation(first_list = []):
    if(not any(isinstance(x, (int, float)) for x in first_list)): return 0

    return round(summation_value, 3)
