#This is how you add a tab \t
print("Python")
print("\tPython")

#To add a newline \n
print("Languages:\nPython\nC\nJavaScript")

#Now combine \n and \t to start your code with a newline and a tab to boot!
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Now let's learn how to strip whitespace in this next example:
favorite_language = 'python '
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)

#Avoiding Syntax Errors with Strings
message = "One of Python's strengths is its diverse community."
print(message)
#The above printed out just fine
#Now let's see what happens when we use single quotes.
#message = 'One of Python's strengths is its diverse community.'
#print(message)
#The code above contained a syntax error in line 22 because of the use of single quotes