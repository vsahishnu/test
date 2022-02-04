from collections import Counter
from statistics import variance


def mergeSort(arr, b, e):
    if (b+1 >= e):
        return arr

    mid = (b+e)//2
    mergeSort(arr, b, mid)
    mergeSort(arr, mid, e)

    merger(arr, b, e)
    return arr


def merger(arr, b, e):
    mid = (b+e)//2
    left = arr[b:mid]
    right = arr[mid:e]

    l, r, o = 0, 0, b

    while(l < len(left) and r < len(right)):
        if (left[l] < right[r]):
            arr[o] = left[l]
            l += 1
            o += 1
        elif (left[l] > right[r]):
            arr[o] = right[r]
            r += 1
            o += 1
        else:
            arr[o] = left[l]
            l += 1
            o += 1
            arr[o] = right[r]
            r += 1
            o += 1

    while(l < len(left)):
        arr[o] = left[l]
        l += 1
        o += 1
    while(r < len(right)):
        arr[o] = right[r]
        r += 1
        o += 1


def AM(arr):
    return sum(arr)/len(arr)


def GM(arr):
    prod = 1
    for i in arr:
        prod *= i

    return prod ** (1/len(arr))


def HM(arr):
    denomSum = 0
    for i in arr:
        denomSum += (1/i)

    return len(arr)/denomSum


def mode(arr):
    ctr = Counter(arr)
    return [key for key, val in ctr.items() if val == ctr.most_common(1)[0][1]]


def median(arr):
    temp = mergeSort(arr, 0, len(arr))

    if len(arr) % 2 != 0:
        # arr value so no need to do +1 to the index
        return temp[len(arr)//2]

    else:
        m = temp[int((len(arr)/2) - 1)]
        n = temp[int(len(arr)/2)]
        return (m+n)/2


def ranger(arr):
    mini = arr[0]
    maxi = arr[0]
    for i in arr:
        if i < mini:
            mini = i
        if i > maxi:
            maxi = i

    return maxi - mini


def quartileDeviation(arr):
    temp = mergeSort(arr, 0, len(arr))

    q1 = median(temp[:len(temp)//2])
    q3 = median(temp[len(temp)//2:])

    return (q3 - q1)/2


def meanDeviation(arr):
    mean = AM(arr)
    return AM([abs(i-mean) for i in arr])


def standardDeviation(arr):
    mean = AM(arr)
    sumOfThingy = 0
    for i in arr:
        sumOfThingy += (i - mean)**2

    print(sumOfThingy)
    variance = sumOfThingy/len(arr)
    return variance**(1/2)


def main():
    print("Enter the numbers seperated by space: ")
    arr = list(map(int, input().split()))

    print("\nMeasures of central tendency:")
    print("AM: ", AM(arr))
    print("Median: ", median(arr))
    print("Mode: ", mode(arr))
    print("GM: ", GM(arr))
    print("HM: ", HM(arr))

    # variance is feeling left out
    print("\nMeasures of dispersion:")
    print("Range: ", ranger(arr))
    print("Quartile deviation: ", quartileDeviation(arr))
    print("MeanDeviation: ", meanDeviation(arr))
    print("StandardDeviation: ", standardDeviation(arr))


if __name__ == "__main__":
    main()
