def sub(num1, num2):
    """
    -------------------------------------------------------
    Takes two numbers and subtracts them
    -------------------------------------------------------
    Parameters:
        num1 - first number from user  (int)
        num2 - second number from user (int)
    Returns:
        answer - value of the result of num1 and num2 being subtracted (int)
    -------------------------------------------------------
    """
    answer = num1 - num2  
    return answer  

num1 = int(input("Number 1: "))  
num2 = int(input("Number 2: "))  
print("Result:", sub(num1, num2))  
