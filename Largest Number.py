def find_largest_number(numbers):
    if not numbers:
        return None

    largest_number = numbers[0]
    for number in numbers:
        if number > largest_number:
            largest_number = number

    return largest_number

# Example usage
my_list = [4, 8, 2, 10, 6]
largest_num = find_largest_number(my_list)
print("The largest number is:", largest_num)
