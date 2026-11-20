
grid_size = 5

for row in range(grid_size):
    for col in range(grid_size):
        if row == 0 or row == grid_size - 1 or col == 0 or col == grid_size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()     