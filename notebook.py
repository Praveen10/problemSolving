
# Your teacher wrote three numbers A, B and C in your notebook. Put mathematical symbols 
# so the operation between the first two numbers equals the third number.

# Write a program that gets three natural numbers A, B and C from input. 
# Output the wanted equation to the screen. (Use +, -, *, / and =)


A, B, C = map(int, input().split())

if A + B == C:
    print(f"{A}+{B}={C}") 
elif A - B == C:
    print(f"{A}-{B}={C}") 
elif A * B == C:
    print(f"{A}*{B}={C}") 
elif A / B == C:
    print(f"{A}/{B}={C}") 
else:
    print("") 