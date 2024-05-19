def process_file(input_file_path, output_file_path):
    # Dictionary to store unique integers
    unique_integers = {}

    # Read input file
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            try:
                number = int(line.strip())
                if -1023 <= number <= 1023:
                    unique_integers[number] = True
            except ValueError:
                # Skip non-integer lines
                pass

    # Convert dictionary keys to list
    integers_list = list(unique_integers.keys())

    # Bubble sort implementation
    n = len(integers_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if integers_list[j] > integers_list[j + 1]:
                # Swap if the element found is greater than the next element
                integers_list[j], integers_list[j + 1] = integers_list[j + 1], integers_list[j]

    print(integers_list)
    # Write to output file
    with open(output_file_path, 'w') as output_file:
        for number in integers_list:
            output_file.write(str(number) + '\n')

    print("Unique integers written to", output_file_path)

# Example usage
process_file("sample_input_for_students/sample_01.txt", "results_for_sample_inputs/sample_01.txt_result.txt")
