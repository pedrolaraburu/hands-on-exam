from exercises.ex1 import fibonnaci
from exercises.ex2 import isPalindrome
from exercises.ex3 import isPrime
from exercises.ex4 import sortingAlgorithm
if __name__ == '__main__':
    # Fibonnaci
    print(fibonnaci(7))

    # Is Palindrome
    t1 = isPalindrome('nurses run')
    print(t1)

    t2 = isPalindrome('madam')
    print(t2)

    t3 = isPalindrome(121.121)
    print(t3)

    # Is Prime
    print(isPrime(17))

    # Sorting Algorithm
    arr = [8, 2, 7, 3, 5, 12]
    sortingAlgorithm(arr)
    print(arr)