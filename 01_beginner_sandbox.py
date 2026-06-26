#INTRODUCTION
#to run the file type [python beginner_sandbox.py] into the Command Prompt in VS code

#different types of data 
age = 25                  # Integer (whole number)
price = 19.99             # Float (decimal number)
name = "Alex"             # String (text)
#beware, '10' is a string, so is "5.6", but 10 and 5.6 are integers and floats respectively.
#str(10) makes 10 into "10" and int('10') makes a string into a integer
#Likewise for float()

is_active = True          # Boolean (True or False value)


# A list of items
fruits = ["apple", "banana", "cherry"] # square brackets

# A dictionary storing a user's details
# {key: values}
user_profile = {"username": "coder123", "level": 5} # curly brackets

## Tuples are Immutable - which means you can't edit them once made.
coordinates = (40.7128, -74.0060) # round brackets

# Mixed data types (tuple) - you can have multiple data types in a tuple
user_profile = ("Alice", 30, True)

# Single-item tuple (CRITICAL: Requires a trailing comma!)
single_item = ("apple",) 


print("Hello World!")     # Outputs a text message

user_age = input("Enter age: ") # Captures user typing (always reads as a string)

print(user_age) 


# put a hashtag in front of a line of code to comment it out so it doesn't run!
