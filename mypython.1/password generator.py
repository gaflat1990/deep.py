import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                     'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                     'Z'] 
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
          '*', '(', ')', '<'] 
print("Welcome to the pypassword generator")
need_letter = int(input("How many letters you need for your passowrd\n"))
need_numbers = int(input("How many numbers you need for your passowrd\n"))
need_symbols = int(input("How many symbols you need for your passowrd\n"))
password = ""
for char in range(1, need_letter +1):
    password += random.choice(letters)
for char in range(1, need_numbers +1):
    password += random.choice(numbers)
for char in range(1, need_symbols+1):
    password += random.choice(symbols)
print

