n = int(input())  # Read the number of knights

knights = []

# Read and store information for each knight, including health, attack, and knight number
for i in range(n):
    cur = input().split()
    knights.append([int(cur[0]), int(cur[1]), i + 1])

# Initialize the winner as None
winner = None

for i in range(n - 1):  # Iterate up to n-1
    knight1_attack = knights[i][1]
    knight2_attack = knights[i + 1][1]

    while True:
        # Try to hit knight 2, if they cannot take the hit, progress knight 1 to the next battle by swapping
        if knights[i + 1][0] - knight1_attack < 1:
            winner = knights[i]
            knights[i], knights[i + 1] = knights[i + 1], knights[i]
            break
        knights[i + 1][0] -= knight1_attack
        # Try to hit knight 1, if they cannot take it, progress knight two to the next battle (no need to swap)
        if knights[i][0] - knight2_attack < 1:
            winner = knights[i + 1]
            break
        knights[i][0] -= knight2_attack

# The last remaining knight is the winner
if winner is None:
    winner = knights[-1]

# Print the knight number of the winner
print(winner[2])
