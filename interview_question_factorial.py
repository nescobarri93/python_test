import math
'''print(f'the factorial of 5 is {math.factorial(5)}')'''

#2. Write a function that calculates the factorial of a number
def compute_factorial(number):
    # Compute the factorial of "number" using Python's built-in factorial function from the math module.
    return math.factorial(number)

#3. Test your function
# Define our test function
def test_compute_factorial():
    # Set the input variable, for example, 5
    input_number = 5
    # Call the compute_factorial function, passing the input variable as an argument
    compute_factorial(input_number)
    result = compute_factorial(input_number)
    # Write an assertion statement to verify if the function calculates the factorial correctly
    assert result == 120
    # Add a print statement, for user-friendly output
    print(f' the factorial of {input_number} is {compute_factorial(5)}')











