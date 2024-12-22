# Create a program where you manage what a cash register does.
# You will receive three receipt inputs each with an amount (int) and tax percentage (int) 
# calculate how much from the amount paid is tax. 



# Write a program that reads 4 receipts from standard input first inputting a number then a character.

# A - 18% Tax
# B - 10% Tax
# C - 7% Tax
# Output what the total amount of tax paid is

# Input
# 10000 A
# 7500 B
# 18000 C
# 11500 B

# Output
# Total VAT paid: 4960

N = 4
total = 0
for i in range(N):
    num, chara = map(str, input().split())
    if chara == 'A':
        a = (int(num) * 18) // 100
        total += a
    elif chara == 'B':
        a = (int(num) * 10) // 100
        total += a
    elif chara == 'C':
        a = (int(num) * 7) // 100
        total += a
        
print('Total VAT paid:', total)