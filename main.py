#Password Generator Projec
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#declaring password as an empty string so that we can use store the password in future 
password=" "
for i in range(0,nr_letters):
  l=random.choice(letters)
  password=password+l
for i in range(0,nr_symbols):
  s=random.choice(symbols) 
  password=password+s
for i in range(0,nr_numbers):
  a=random.choice(numbers)  
  password=password+a
print("this password will be in sequential order"+password)
newpassword=" "
for i in password:
  new=random.choice(password)
  newpassword=newpassword+new
print("this password is in unordered"+ newpassword)