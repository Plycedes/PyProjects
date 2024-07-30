# Open the input file for reading
with open("input.txt", "r") as input_file:
    # Read data from the input file
    data = input_file.read()

# Split the data by commas to get individual items
items = data.split(",")

# Open the output file for writing
with open("output.txt", "w") as output_file:
    # Write each item to the output file on a separate line
    for item in items:
        output_file.write(item.strip() + "\n")

print("")
print("Data has been written to output.txt in a different format.")
print("")
