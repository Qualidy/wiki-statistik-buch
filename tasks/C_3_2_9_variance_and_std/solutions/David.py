# as usual, tests are within their own test-file for better structuring

def variance(data_list: list):
    length = len(data_list)

    if not length:
        raise ValueError('The given list must have at least 1 element in it')

    if any([not isinstance(value, (int, float)) for value in data_list]):
        raise ValueError('Only lists containing integers or floats are allowed')

    mean = sum(data_list) / length
    return sum([(value - mean)**2 for value in data_list]) / length


def deviation(data_list: list):
    return variance(data_list) ** 0.5
