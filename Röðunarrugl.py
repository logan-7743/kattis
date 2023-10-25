# Description: This code calculates the number of steps required to rearrange a list of items to a desired order.
# It iterates through the list and moves items to their correct positions, counting each step taken.

# Read an integer 'n' from the user.
n = int(input())

# Read a list of integers 'items' from the user, representing the current order of items.
items = list(map(int, input().split()))

set_out = []  # Initialize a list to store the items moved out of position
steps = 0     # Initialize a variable to count the steps taken

# Iterate through the list from 1 to 'n'
for i in range(1, n + 1):
    # Check if the current item is not in its desired position
    if items[i - 1] != i:
        cur = items[i - 1]  # Store the current item
        set_out.append(cur)  # Add the current item to the 'set_out' list
        items[i - 1] = i    # Move the current item to its desired position
        steps += 2          # Increment the step count by 2 (one move and one swap)

        # Continue moving items until the current item is in its desired location
        while cur != i:
            next_item = items[cur - 1]
            set_out.append(next_item)  # Add the next item to 'set_out'
            items[cur - 1] = cur     # Move the next item to its desired position
            steps += 1               # Increment the step count by 1
            cur = next_item

# Print the total number of steps taken to rearrange the items.
print(steps)
