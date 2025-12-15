# We will first create a dictionary and then loop through it:
python_terms = {"Variable": "A named storage location in the computer's memory that holds a value, which can be retrieved and used later in the program.",
                "Data Type": "A classification that specifies which type of value a variable can hold. Common built-in types include int (integers), float (decimal numbers), str (text strings), and bool (Boolean, i.e. true or false).",
                "List": "An ordered collection of items that can be of different data types and whose values can be changed after creation (mutable). Lists are created using square brackets, e.g., [1, hello, 3.0].",
                "Tuple": "Similar to a list, but its values cannot be changed after creation (immutable). Tuples are created using parentheses, e.g., (1, hello, 3.0).",
                "Function": "A reusable block of organized code that performs a specific, related action. Functions are defined using the def keyworkd in Python.",
                "Module": "A Python file containing code (functions, classes, variables, etc) that can be imported and reused in other Python programs.",
                "Loop": "A control flow statement that allows a block of code to be executed repeadedly, either a specific number of times (for loop) or until a certain condition is met (while loop).",
                "Conditional Statement": "Statements (if, elif, and else) that control the flow of a program's execution based on whether a condition is true or false.",
                "Object": "Everything in Python is an object, which is an instance of a class. It is a self-contained entity with specific properties (attributes) and behaviors (methods).",
                "Identation": "The use of whitespace to define the structure and scope of code blocks in Python (e.g., within loops of functions), which is a core part of Python's syntax.",
                }
# Now we will loop through the keys and their values in the dictionary:
for key, value in python_terms.items():
    print(f"Key: {key}")
    print(f"Value: {value}")
    print("-" * 20)
# Line break:
print()
# Now we will print the terms:
for key in python_terms:
    print(f"Key: {key}")
# Obligatory line break:
print()
# Now we will print the definitions
for value in python_terms:
    print(f"Value: {value}")