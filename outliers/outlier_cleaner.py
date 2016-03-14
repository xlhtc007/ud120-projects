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
    for i in range(90):
        cleaned_data.insert(i, (ages[i], net_worths[i], (predictions[i]-net_worths[i])**2))

    cleaned_data = sorted(cleaned_data, key=lambda t: t[2])
    cleaned_data = cleaned_data[0:81]
    print len(cleaned_data)

    return cleaned_data

