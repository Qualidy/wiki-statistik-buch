# testcases are on a seperate file for better structure

def modal_value(data_list: list):
    keys = set(data_list)
    absolute_distribution = [(key, data_list.count(key)) for key in keys]
    return max(absolute_distribution, key=lambda x: x[1])[1]


def mean_value(data_list: list):
    return sum(data_list) / len(data_list)


def median_value(data_list: list):
    data_list = sorted(data_list)
    length = len(data_list)
    mid = length // 2
    return data_list[mid] if length & 1 else sum(data_list[mid-1:mid+1]) / 2


def geom_mean_value(data_list: list):
    product = 1
    for value in data_list:
        product *= value
    return product ** (1 / len(data_list))


def harmonic_mean_value(data_list: list):
    return len(data_list) / sum([1 / value for value in data_list])
