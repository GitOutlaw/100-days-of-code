row1 = ["🌳", "⛰️", "🏖️"]
row2 = ["🛏️", "🌴", "🏦"]
row3 = ["⛪", "🏰", "💰"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where do you want to put the treasure? "))

if position == 11:
    map[0][0] = "X"

elif position == 12:
    map[0][1] = "X"

elif position == 13:
    map[0][2] = "X"

if position == 21:
    map[1][0] = "X"

elif position == 22:
    map[1][1] = "X"

elif position == 23:
    map[1][2] = "X"

elif position == 31:
    map[2][0] = "X"

elif position == 32:
    map[2][1] = "X"

elif position == 33:
    map[2][2] = "X"

print(f"{row1}\n{row2}\n{row3}")
