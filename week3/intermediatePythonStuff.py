def add_numbers (a , b ):
    """
    Adds two numbers together .
    Parameters :
    a (int or float ): The first number .
    b (int or float ): The second number .
    Returns :
    int or float : The sum of a and b.
    """
    return a + b
# Example usage :
result = add_numbers (5 , 3 )
print ("The sum is:", result )

# Dictionary of student grades
student_grades = {"Alice": 85 , "Bob": 90 , "Charlie": 78}
print(student_grades["Alice"])

student_grades ["David"] = 92 # Adds a new key - value pair
student_grades ["Alice"] = 88 # Updates Alice ’s value

# Looping through keys ( student names )
print ("Student names : ")
for name in student_grades . keys ():
    print(name)
    # Looping through values ( grades )
print ("\nStudent grades: ")
for grade in student_grades . values ():
    print ( grade )
