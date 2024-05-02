# Author: Jovane Cano
# GitHub Username: jovanecano
# Date: 05/01/2024
# Description:
'''Contains a recursive function that takes two positive integers as parameters and returns the
the product of those two numbers'''

def multiply(num1, num2):
    '''this function will continue to add num1 to itself as long as num2 - 1 does not equal 0'''
    if num1 == 0 or num2 == 0: # base case
        return 0
    # print(multiply(12,0))
    else:
        return num1 + multiply(num1, num2-1)


print(multiply(12,6))