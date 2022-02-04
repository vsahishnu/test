def AM(arr):
    return sum(arr)/len(arr)


def standardDeviation(arr):
    mean = AM(arr)
    sumOfThingy = 0
    for i in arr:
        sumOfThingy += (i - mean)**2

    variance = sumOfThingy/len(arr)
    return variance**(1/2)


def covari(arr, arr2):
    meanX = AM(arr)
    meanY = AM(arr2)
    sumOfThingy = 0
    for i in range(len(arr)):
        sumOfThingy += (arr[i] - meanX) * (arr2[i] - meanY)

    return sumOfThingy/len(arr)


def main():
    print("Enter the numbers seperated by space for x series: ")
    arr = list(map(int, input().split()))

    print("Enter the numbers seperated by space for y series: ")
    arr2 = list(map(int, input().split()))

    print()
    print("The standard deviation of x series is: ", standardDeviation(arr))
    print("The standard deviation of y series is: ", standardDeviation(arr2))

    print()
    print("The covariance is: ", covari(arr, arr2))
    print("The correlation is : ", covari(arr, arr2) /
          (standardDeviation(arr)*standardDeviation(arr2)))


if __name__ == "__main__":
    main()
