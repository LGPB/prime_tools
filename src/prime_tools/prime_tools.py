import math


def is_prime(num: int) -> bool:
    """returns True if num is prime, False otherwise

    The reason why numbers below 2 raise an error rather than returning false, is so this
    function can also function as a is_composite

    Args:
        num (int): number to check:

    Returns:
        bool: True if num is prime, False otherwise

    Raises:
        TypeError: if num is not an integer:
        ValueError: if num is below 2
    """
    if not isinstance(num, int):
        raise TypeError("number must be an int")
    if num < 2:
        raise ValueError("primes must be greater than 1")

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for divisor in range(3, math.ceil(math.sqrt(num)) + 1, 2):
        if num % divisor == 0:
            return False

    return True


def prime_range(start: int, end: int) -> list:
    """
    Returns a list of prime numbers that are >= start and < end

    Args:
        start(int): first number (inclusive):
        end(int): last number:

    Returns:
        list: list of prime numbers that are >= start and < end
    """
    primes = []

    for number in range(start, end):
        try:
            if is_prime(number):
                primes.append(number)

        except ValueError:
            continue

    return primes


def prime_list(length: int, start: int = 0) -> list:
    """
    Returns a list of primes of len(length) with the first prime >= start
    Args:
        length(int): size of list
        start(int): first number (inclusive):

    Returns:
        list: list of prime numbers of len(length) with the first prime >= start
    """
    if not isinstance(length, int):
        raise TypeError("length must be an int, but was {}".format(type(length)))
    if not isinstance(start, int):
        raise TypeError("start must be an int, but was {}".format(type(start)))
    if length < 0:
        raise ValueError("length must be positive, but was {}".format(length))

    primes = []

    while len(primes) < length:
        if is_prime(start):
            primes.append(start)

        start += 1

    return primes


def nearest_prime(start: int, skips: int = 0, ascending: bool = True) -> int | None:
    """
    Returns the nearest prime number to the given start.

    skips are used to search for the nth closest prime number.
    ascending is for searching for primes bigger or smaller than start.
    Args:
        start(int):
        skips(int):
        ascending(bool):

    Returns:
        int: the nth prime number
        None: if it doesn't exist, E.g the nearest prime number smaller than 2

    Raises:
        TypeError: if start, int, and bool are not their correct types
        ValueError: if skips is less than 0
        ValueError: if skips is less than 0
    """
    if not isinstance(start, int):
        raise TypeError("start must be int, but was {}".format(type(start)))
    if not isinstance(skips, int):
        raise TypeError("skips must be int, but was {}".format(type(skips)))
    if not isinstance(ascending, bool):
        raise TypeError("ascending must be bool, but was {}".format(type(ascending)))
    if skips < 0:
        raise ValueError("skips must be >= 0")


    if ascending:
        while True:
            start += 1
            if is_prime(start) and skips <= 0:
                return start

            elif is_prime(start):
                skips -= 1

    else:
        while start > 2:
            start -= 1
            if is_prime(start) and skips <= 0:
                return start

            elif is_prime(start):
                skips -= 1

    return None
