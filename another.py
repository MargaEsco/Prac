#Write a program that takes a list of numbers and calculates

#The total sum of the numbers.
#The average of the numbers.
#Count how many numbers are above the average.

numbers = [10, 20, 30, 40, 50, 60]

# Initialize variables
total = 0
count = len(numbers)  # Get the number of items in the list

# Calculate the total sum
for number in numbers:  # This is a for loop
    total += number  # Add each number to the total

# Calculate the average
average = total / count

# Count how many numbers are above the average
above_average_count = 0
for number in numbers:  # Another for loop
    if number > average:  # Check if the number is above average
        above_average_count += 1  # Increment count

# Print results
print("Total Sum:", total)
print("Average:", average)
print("Count of numbers above average:", above_average_count)