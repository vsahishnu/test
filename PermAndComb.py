# nCr = n! / r!(n-r)!
# nPr = n! / (n-r)!

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


def permutation(n, r):
    return ((factorial(n)) / (factorial(n-r)))


def combination(n, r):
    return (factorial(n) / ((factorial(r)) * (factorial(n-r))))


n = int(input("what is n = "))
r = int(input("what is r = "))

print("permutation (nPr) = ", int(permutation(n, r)))
print("combination (nCr) = ", int(combination(n, r)))
