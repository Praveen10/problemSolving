# Create a system for a cinema to return the price of the ticket for a movie. The initial price for the movie is 200, 
# if the movie is a comedy it's an additional 30, if it's an action movie is an additional 40, and if it's a horror 
# it is an additional 20. Next, if you get a small popcorn (S) it's an additional 100, a medium (M) an additional 150, 
# and a large (L) an additional 200 and finally, if you pay with a card you get a 10% discount


# Challenge

# Easy
# Write the program to calculate the total price for 3 tickets, in the first row the type of movie will be specified (string), 
# in the following the size of popcorn will be specified (char), in the next row the number of people getting a ticket and popcorn will be given, 
# followed by a 1 if it's paid with a card, or a 0 otherwise. Output the total price

# Input
# comedy
# S
# 4
# 1

# Output
# 1188

# Explanation
# 4 people are buying 230 worth of tickets, and 100 worth of popcorn, 330 * 4 = 1320, 
# and a 10% discount for paying with a card is a total of 1188

movie_type = input().strip()
popcorn_size = input().strip()
num_people = int(input())
card_payment = int(input())
base_price = 200
movie_additional = {"comedy": 30, "action": 40, "horror": 20}
popcorn_prices = {"S": 100, "M": 150, "L": 200}

ticket_price = base_price + movie_additional.get(movie_type, 0)
popcorn_price = popcorn_prices.get(popcorn_size, 0)
total_price = (ticket_price + popcorn_price) * num_people

if card_payment == 1:
    total_price *= 0.9

print(f"${int(total_price)}") 
