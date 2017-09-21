def average(array):
    uniques = set(array)
    total = sum(uniques)
    average = total/len(uniques)
    return average
