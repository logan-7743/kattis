# Input:
x = input().split()  # Read space-separated input values
n_burg = int(x[1]) + 1  # Extract and increment the number of burgers needed
time_list = input().split()  # Read a list of time values for each burger

lo = 1  # Initialize the lower bound for binary search
hi = 10**18  # Initialize the upper bound for binary search

while lo < hi:
    mid = (lo + hi) // 2  # Calculate the middle time value
    cur = 0  # Initialize the current number of burgers prepared

    # Calculate the number of burgers that can be prepared in 'mid' time
    for i in range(len(time_list)):
        cur += mid // int(time_list[i])

    if cur < n_burg:
        lo = mid + 1  # If the current number of prepared burgers is less than needed, increase the lower bound
    else:
        hi = mid  # If the current number of prepared burgers is sufficient or more, update the upper bound

print(hi)  # Print the minimum time needed to prepare the required number of burgers
