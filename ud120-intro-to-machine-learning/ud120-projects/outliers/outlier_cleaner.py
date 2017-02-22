#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    tupleView = zip(ages, net_worths, predictions)
    pointsOrderedByError = sorted(tupleView, key=lambda (age, net_worth, prediction): prediction - net_worth)
    cleaned_data = pointsOrderedByError[:int(round(0.9*len(pointsOrderedByError)))]

    print "Cleaned data has:", len(cleaned_data), " data points."
    
    return cleaned_data

