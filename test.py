# Define a variable outside the function
outside_variable = 10

def use_outside_variable(some_variable):
    # Use the outside_variable within the function
    result = some_variable + outside_variable
    return result

# Call the function and pass the outside_variable as an argument
output = use_outside_variable(5)

print("Output:", output)
