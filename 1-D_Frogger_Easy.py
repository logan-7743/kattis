# Input:
n, p, magic = map(int, input().split())  # Read 'n', 'p', and 'magic' from user input
vals = list(map(int, input().split()))  # Read a list of 'n' integers from user input

index = p - 1  # Initialize the current index to 'p - 1'

for i in range(len(vals)):
    if index < 0:
        print("left\n", i)  # If the index goes below 0, print "left" and the number of steps 'i'
        break
    if index >= len(vals):
        print("right\n", i)  # If the index goes beyond the list length, print "right" and 'i'
        break
    if vals[index] == "been":
        print("cycle\n", i)  # If the value at the current index is "been," print "cycle" and 'i'
        break
    if vals[index] == magic:
        print("magic\n", i)  # If the value at the current index is equal to 'magic', print "magic" and 'i'
        break

    temp = vals[index]  # Store the current value in 'temp'
    vals[index] = "been"  # Mark the current index as "been"
    index += temp  # Update the index by adding the value 'temp' from the list
