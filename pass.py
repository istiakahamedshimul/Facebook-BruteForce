def generate_and_save_numbers(num_digits, output_file):
    start_range = 10 ** (num_digits - 1)
    end_range = 10 ** num_digits - 1

    with open(output_file, 'w') as file:
        for number in range(start_range, end_range + 1):
            file.write(str(number) + '\n')

# Take input for the number of digits
num_digits = int(input("Enter the number of digits (e.g., 6): "))

# Specify the output file name
output_file = 'number_list.txt'

# Generate and save numbers to the file
generate_and_save_numbers(num_digits, output_file)

print(f"{10 ** (num_digits - 1)} to {10 ** num_digits - 1} generated and saved in {output_file}")
