# Input: Read an integer 'n' from the user.
n = int(input())

# Calculate the number of groups of 4 that can be formed from the sequence 1 to n-1.
group = n // 4

# Calculate the sum of all groups of 4 and store it in 'bags'.
# This is essentially the sum of (1+2+3+...+(group-1)) multiplied by 4.
bags = ((group - 1) * group // 2) * 4

# Add 4 to the 'bags' value.
result = bags + 4

# Print the final result.
print(result)
