# Creates rows of squares
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]

# Add each row to another list
board = [row1, row2, row3]

# Print each row on a new line to form the board
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Convert user input to integer and use the first digit for the row and the second for the column
row = int(position[0])
col = int(position[1])

# Subtract 1 to get the current index position to place the 'X'
board[row - 1][col - 1] = 'X'

# Print board where 'X' marks the spot
print(f"{row1}\n{row2}\n{row3}")
