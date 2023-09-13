#!/usr/bin/python3
def weight_average(my_list):
    # Check if the list is empty
    if not my_list:
        return 0

    weighted_sum = 0
    total_weight = 0

    # Calculate the weighted sum and total weight
    for (value, weight) in my_list:
        weighted_sum += value * weight
        total_weight += weight

    # Calculate and return the weighted average
    if total_weight == 0:
        return 0
    else:
        return weighted_sum / total_weight
