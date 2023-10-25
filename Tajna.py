msg = input()  # Read the input message
N = len(msg)  # Get the length of the message
R = 1
C = N

# Calculate the number of rows (R) and columns (C) for the grid
for i in range(int(N/2)):
    i += 1
    if N % i == 0:
        if N / i > R:
            C = int(N / i)
            R = int(N / C)

# Ensure that the number of columns (C) is not greater than the number of rows (R)
if C > R:
    R, C = C, R

# Create a grid filled with 'None' values
grid = [[None]*C for r in range(R)]

# Fill the grid with characters from the input message
for i in range(R):
    for j in range(C):
        grid[i][j] = msg[0]
        msg = msg[1:]

result = ""

# Read the grid column by column and construct the final message
for i in range(C):
    for j in range(R):
        result += grid[j][i]

print(result)  # Print the final message
