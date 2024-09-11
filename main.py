def main(): 
    print("hello world")

    # Declare variables
    age = 17
    teacher = "Ms. Navab"
    is_fav_class = True 
    my_grade = 99.99 
    x = 42
    y = 3/4
    z = int('7')
    a = float(5)
    name = "Nina"
    
    # Check the type of a variable
    type_of_age = type(age)
    print(type_of_age)

    type_of_x = type(x)
    print(type_of_x)

    type_of_y = type(y)
    print(type_of_y)

    type_of_z = type(z)
    print(type_of_z)

    type_of_a = type(a)
    print(type_of_a)

    type_of_name = type(name)
    print(type_of_name)


    # String formatting with f-strings 
    # f"String literal {variable}"
    print(f"The type of the variable age is: {type_of_age}")
    print("String literal",teacher)
    print(f"My age in 10 years: {age + 10}")

def bake_cookie(ingredients, instructions, temperature):
    # Print the list of ingredients 

    # Print the oven temperature setting
     

    # Print the instructions
    print(instructions)

if __name__ == "__main__":
    main()

# errors are called exceptions in Python 