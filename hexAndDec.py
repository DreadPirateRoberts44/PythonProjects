# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:46:58 2020

@author: Mike Yamokoski
"""

#This program converts decimal to hexidecimal and vice versa

def decToHex(num):
    hexVal = ""
    #loop until the quotient is zero
    while num / 16 > 0:
        
        #get the hex digit for the current place
        remainder = num % 16
        
        if remainder < 10:
            hexVal = str(remainder) + hexVal
        elif remainder == 10: 
            hexVal = "A" + hexVal
        elif remainder == 11: 
            hexVal = "B" + hexVal
        elif remainder == 12: 
            hexVal = "C" + hexVal
        elif remainder == 13: 
            hexVal = "D" + hexVal
        elif remainder == 14: 
            hexVal = "E" + hexVal
        else: 
            hexVal = "F" + hexVal
        
        num //= 16
        
    return hexVal

def hexToDec(hexVal):
    num = 0
    print(hexVal)
    i = 0
    #loop through each character
    while i < len(hexVal): 
        
        char = hexVal[i]
        #print(char)
        #assign current char to its respective hex value
        if char.isdigit():
            currDig = int(char)
        else:
            char.upper()
            if char == "A":
                currDig = 10
            elif char == "B":
                currDig = 11
            elif char == "C":
                currDig = 12
            elif char == "D":
                currDig = 13
            elif char == "E":
                currDig = 14
            else: 
                currDig = 15
        
        
        #muliply the current digit by 16 raised to one less than the current
        #position and add it to the num
        num += currDig * (16 ** (len(hexVal) - i - 1))
        i += 1
    return num

response = 0
#loop until user wants to quit
while response != 2:
    answer = input("Are you converting from dec(0), hex(1), or do you want to quit(2)?")
    #convert response to an int
    response = int(answer)
    if response == 0:
           initial = int(input("Enter a number: "))
           
           hexVal = decToHex(initial)
           print("Your hex value is: " + hexVal)
           
    elif response == 1:
        initial = (input("Enter a hexidecimal value: "))
        
        num = hexToDec(initial)
        print("Your number is : " + str(num))