# For two numbers we say that they are anagrams if the digits of the first number can be rearranged, 
# so that we get the second number. For ex. 123 is an anagram of 231, because they are the same digit in a different order. 

 

# Write a program that gets a natural number N from input. In the next N lines you have two numbers, A and B. 
# Output how many of those pairs of numbers are anagrams

N = int(input())
counter = 0
for i in range(1, N + 1):
    A, B = map(int, input().split())
    if sorted(str(A)) == sorted(str(B)):
        counter += 1 
print(counter)