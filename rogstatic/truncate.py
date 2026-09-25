
def truncate(num):
    '''
    (float) -> float
    truncate the float to a maximum
    of two decimal places.
    
    >>> truncate(123.012345)
    >>> 123.01
    '''

    integer = num // 1
    temp_1 = num % 1 * 100.0001
    decimal = (temp_1 // 1) /100
    
    return integer + decimal
    

print(truncate( 1234.992345 ))






