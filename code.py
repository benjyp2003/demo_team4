def is_prime(number):
    return not (False in [False if number % num == 0 else True for num in range(2,number//2 +1)])
