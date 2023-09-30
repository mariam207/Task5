# Question 1
name = input("*Enter your name: ")
age = input("*Enter your age: ")
street = input("*Enter your street: ")
city = input("*Enter your city: ")
country = input("*Enter your country: ")

# Question 2
print(f"\n\"Name: {name}\"")
print(f"\"Age: {age}\"")
print(f"\"Address: {street}, {city}, {country}\"")

# Question 3
print(f"\n\"Hello {name} Your age is {age} Years Old, Your Address is {street}, {city}, {country}.\"")

# Question 4
print('\n', type(name), type(age), '\n', type(street), type(city), '\n', type(country))

# Question 5
print(f"\n\"Hello {name}, How Are You? \\ \"\"\" Your Age Is \"{age}\"\"\" + And Your Country Is: {country}")

# Question 6
print(f"\n \"Hello {name}, How Are You? \\ \n \"\"\" Your Age Is \"{age}\"\"\" + And \n Your Country Is: {country}")

# Question 7
print("\n")
name = 'ITF Gsg Python'
print(f"First Letter Is \"{name[0]}\"")
print(f"Third Letter Is \"{name[2]}\"")
print(f"Last Letter Is \"{name[-1]}\"")

# Question 8
print('\n', name[11:])
print('', name[:3])
print('', name[:7:2])
print('', name[13:7:-1])

# Question 9
print("\n")
name = "$&$&Mohammed$&$&"
print(name.strip("$&"))

# Question 10
print("\n")
msg = "I %7 Python And Although I %7 GSG with Mariam"
print(msg.replace("%7", "Love"))

# Question 11 & 12
print("\n")
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num6)

# Question 13
print("\n")
  #title : it capitalizes the first letter of Each Word and converts all other letters into lowercase.
txt = "python is FUN"
print(txt.title())
  #capitalize : it capitalizes only The First Letter Of The String and converts all other letters to lowercase.
txt = "python is FUN"
print(txt.capitalize())

# Question 14
first_name = "Mariam"
print("\n***********" + first_name)
print("***********" + first_name + "***********")
print(first_name + "***********")

# Question 15
name_one = "SaMER"
name_two = "Abed"
print("\n")
print(name_one[0].lower() + name_one[1:].upper())
print(name_two[0].lower() + name_two[1:].upper())
print( name_one.lower())
print(name_two.upper())

# Question 16
print("\n")
if name_one.isupper():
    print("name one contains only uppercase letters.")
else:
    print("name one does not contain only uppercase letters.")
if name_two.islower():
    print("name two contains only lowercase letters.")
else:
    print("name two does not contain only lowercase letters.")

# +2 Question 17
print("\n")
starts_with_s = name_one.lower().startswith("s")
ends_with_hd = name_two.lower().endswith("hd")
if starts_with_s:
    print("name one starts with (S)")
else:
    print("name one does not start with (S)")
if ends_with_hd:
    print("name two ends with (HD)")
else:
    print("name two does not end with (HD)")

# +2 Question 18
print("\n")
msg = "I Love Python And Although I Love GSG with Mariam"
print("Number of <Love> is: ", msg.count("Love"))
print("Number of <t> is: ", msg.count("t"))

# +2 Question 19
print("\n")
msg = "I %7 Python And Although I %7 GSG with Mariam"
print(msg.replace("%7", "Love", 1))

# +2 Question 20
## i could not solve it and i did not want to cheat (: hehehe