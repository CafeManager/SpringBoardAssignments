def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1Current = 0
    num2Current = 0

    possibleInts = "1234567890"
    strNum1 = str(num1)
    strNum2 = str(num2)

    for num in possibleInts:
        if strNum1.count(num) != strNum2.count(num):
            return False

    return True 