def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
    # Find the greatest commom divisor first (GCD)
            
    
    if a > b:
        R = a % b
        D = b
    else:
        R = b % a
        D = a
    while R > 0:
            R1 = D % R
            D = R
            R = R1
    GCD = D
    LM = a * b // GCD
    return LM
            
        
        
    
def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for k in range(0,10):
        if str(k) in str(n):
            count += 1
        else:
            continue
    return count

        
            
                

