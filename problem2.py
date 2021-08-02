def findMinMax(arr):
    # super lazy way
    #return {"min": min(arr), "max": max(arr)}

    largest = -999999
    smallest = 999999

    # finding the lowest value in an array
    for i in arr:
        if i < smallest:
            smallest = i

    for i in arr:
        if i > largest:
            largest = i

    
    return {"smallest": smallest, "largest": largest}


if __name__ == "__main__":
    arr = [1, 2, 3, 23, 1234,420, 123]

    minmax = findMinMax(arr)

    print(minmax)