
def greet():
    print("ni hao")

def cook():
    print("We are making dumplings")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__': #this is called guarding
    print("prime numbers")
    print(is_prime(5))
    print(is_prime(7))
    print(is_prime(19))
    print(is_prime(101))

    print("not prime numbers")
    print(is_prime(6))
    print(is_prime(9))
    print(is_prime(25))
    print(is_prime(201))
