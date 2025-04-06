#7. WAP to input three-digit number & display sum of its digit using while loop? 

number = int(input("Enter a 3-digit number: "))

if 100 <= number <= 999:

    hundreds = number // 100 
    tens = (number // 10) % 10  
    units = number % 10  
   
    digit_sum = hundreds + tens + units
    
    print("The sum of the digits :",digit_sum)
else:
    print("Please enter a valid 3-digit number!")
