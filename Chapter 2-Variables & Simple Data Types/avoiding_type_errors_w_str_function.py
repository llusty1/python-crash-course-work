# This goes over various type errors 
# age = 23
# message = "Happy " + age + "rd Birthday!"
# print(message) # When first run we get a type error
# message = "Happy " + age + "rd Birthday!"
#              ~~~~~~~~~^~~~~
# TypeError: can only concatenate str (not "int") to str
# The reason for this error is the variable is an integer and Python doesn't know how to interpret the value.
# It could very well be 23 or 2 3. 

# The correct code is below
age = 23
message = "Happy " + str(age) + "rd Birthday!" # Wrapping the variable in a string defines the integer. 

print(message)