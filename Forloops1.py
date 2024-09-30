#Write a program that loops through the numbers from 1 to 30. The program should print out only the numbers that are divisible by both 2 and 3.

for i in range(1, 31):  # Loop from 1 to 30
    if i % 2 == 0 and i % 3 == 0:  # Check if divisible by both 2 and 3
        print(i)  # Print the number if it is divisible by 2 and 3



#Problem Statement: Write a program that takes a list of ages and categorizes each age into one of the following groups:

Ages = [0-12, 13-19, 20-64, 65]

#Child: Age 0-12
#Teenager: Age 13-19
#Adult: Age 20-64
#Senior: Age 65 and above

Ages = [5, 13, 25, 67, 18, 32, 12, 75, 40]  # Example list of ages

for number in Ages:  # Loop through each age in the list
    if number <= 12:

        print(f"Age {number}: Child")  # Print category for children
    elif number <= 19:
        
        print(f"Age {number}: Teenager")  # Corrected condition for teenagers

    elif number <= 64:
        print(f"Age {number}: Adult")  # Correct condition for adults
        
    else:
        print(f"Age {number}: Senior")  # Senior category for ages 65 and above
   