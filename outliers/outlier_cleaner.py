#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    for i in range(len(predictions)):
        cleaned_data.append((ages[i][0], net_worths[i][0], abs(net_worths[i][0] - predictions[i][0])))

    sorted_by_error = sorted(cleaned_data, key=lambda tup: tup[2], reverse=True)

    for i in range(len(ages) / 10):
        print sorted_by_error[0]
        del sorted_by_error[0]

    return sorted_by_error

