import sys

if len(sys.argv) != 2:
    print("Error: Please provide the name of the file to read.")
    sys.exit(1)

file_name = sys.argv[1]

try:
    with open(file_name, 'r') as file:
        for line in file:
            try:
                values = line.split()

                if len(values) != 2:
                    print(
                        "Error: Invalid line, expected two float values, got " + str(len(values)) + ": " + line.strip())
                    continue

                num1 = float(values[0])
                num2 = float(values[1])
                print("Sum: " + str(num1 + num2))

            except ValueError:
                print("Error: Invalid values on line: " + line.strip())

except FileNotFoundError:
    print("Error: The file '" + file_name + "' could not be opened.")
    sys.exit(1)
