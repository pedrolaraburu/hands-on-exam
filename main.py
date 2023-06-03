from exercises.ex1 import fibonnaci
from exercises.ex2 import isPalindrome
from exercises.ex3 import isPrime
if __name__ == '__main__':
    print(fibonnaci(7))

    t1 = isPalindrome('nurses run')
    print(t1)

    t2 = isPalindrome('madam')
    print(t2)

    t3 = isPalindrome(121.121)
    print(t3)

    print(isPrime(17))