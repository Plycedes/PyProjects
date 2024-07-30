import matplotlib.pyplot as plt

# Read data from the file
with open("data.txt", "r") as file:
    data = file.readlines()

# Extract x and y values from the data
x_values = []
y_values = []
for line in data:
    x, y = map(float, line.split())  # Assuming data is formatted as "x y"
    x_values.append(x)
    y_values.append(y)

# Create a line plot
plt.plot(x_values, y_values)
plt.xlabel("X Axis Label")
plt.ylabel("Y Axis Label")
plt.title("Data Visualization")
plt.grid(True)
plt.show()
