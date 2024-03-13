

def purelin(n):
    """
    Calculate purelin value for given number.

    Parameters:
    n (float): The number for which purelin value needs to be calculated.

    Returns:
    float: The purelin value of the input number.

    """
    a=n
    return a

## poslin
def poslin(n):
    """
    --- poslin ---

    Parameters:
    - n: The number to be processed.

    Description:
    This function takes a number as input and returns the value of the number if it's greater than or equal to 0, otherwise it returns 0.

    Example Usage:
    n = 5
    result = poslin(n)
    print(result)
    # Output: 5

    n = -5
    result = poslin(n)
    print(result)
    # Output: 0

    """
    if n<0:
        a=0
    else:
        a=n
    return a

## hardlims
def hardlims(n):
    """

    """
    if n<0:
        a=-1
    else:
        a=1
    return a

## hardlim
def hardlim(n):
    """
    Applies the hardlimit activation function to the input.

    Parameters:
    n (float): The input value.

    Returns:
    float: The result of applying the hardlimit activation function to the input.
    """
    if n<0:
        a=0
    else:
        a=1
    return a

## satlins
def satlins(n):
    """
    Implements the Satlins activation function.

    Parameters:
    n (float): The input value.

    Returns:
    float: The output value after applying the Satlins function.

    Notes:
    - The Satlins function returns -1 for input values less than -1, 1 for input values greater than 1, and the input value itself for values between -1 and 1.

    Examples:
    >>> satlins(-5)
    -1.0
    >>> satlins(3)
    1.0
    >>> satlins(0.5)
    0.5
    """
    if n<-1:
        a=-1
    elif n>1:
        a=1
    else:
        a=n
    return a
def bound(x,b,w):
    """
    Calculate the boundary for a given point.

    Parameters:
    - x: The x-coordinate of the point.

    Returns:
    - The y-coordinate of the boundary line, calculated as (-b - w[0]*x) / w[1].

    """
    return (-b-w[0]*x)/w[1]