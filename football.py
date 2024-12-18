# In the games of football, the winner is awarded 3 points, the loser is not awarded any points and 
# if the match is a draw, both teams get 1 point each. 

 

# Write a program that gets a natural number N from input. In the next N lines there are three numbers W, D, L representing the wins, 
# draws and loses of the specific team respectively. Output the number of points that the team with most points has.

def calculate_points(wins, draws, losses):
    return 3 * wins + draws

N = int(input())

max_points = 0

for _ in range(N):
    W, D, L = map(int, input().split())
    points = calculate_points(W, D, L)
    max_points = max(max_points, points)

print(max_points)