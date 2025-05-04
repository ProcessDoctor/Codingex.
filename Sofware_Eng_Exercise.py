# Question: Find the most repeated character in the text below
from pprint import pprint
text = "You are so awesome and there iiiis nothiiing iiiimpossible for you"
# Solution
# First how many times are each character repeated
# Then find the most repeated character
# We can use a dictionary that stores key pair values

num_char = {}
for char in text:
    if char in num_char:
        num_char[char] += 1
    else:
        num_char[char] = 1


num_char_sorted = sorted(
    num_char.items(),
    key=lambda kv: kv[1],
    reverse=False)

print(num_char_sorted[-1])
