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

    # Initialize args (arguments) for function
    ingredients_list = ["- chocolate chips", "- cinnamon", "- flour", "- sugar", "- butter", "- eggs"]
    snickerdoodle_instructions = "* Instructions: Gently beat the butter and eggs together. Seperately mix the flour, cinnamon and sugar. Next, combine the two mixtures and add chocolate chip cookies. Form into balls and place onto a baking tray. Put cookies into oven (with gloves ofc)"
    temp = 300

    # Call a function 
    bake_cookie(ingredients_list, snickerdoodle_instructions, temp)

    # Call a function with an optional argument
    bake_cookie(ingredients_list, snickerdoodle_instructions, temp, cookie_cutter="teddybear")

    # Reviweing optional keyword arguments
    print("***Calculations***")
    print(calculate_numbers(2, 3)) # goes with default, "add"
    # The next two lines both result in -1
    print(calculate_numbers(2, 3, "subtract")) 
    print(calculate_numbers(2, 3, operation = "subtract")) # if you specify keyword (specifiy which argument it is representing) the order wont matter

    print()
    
    # Demonstrate modifying values while iterating
    print("***List Iterations***")
    numbers = [5, 5, 6, 5.5, 7, 42, 70, "hi"]
    # Note that you can mix different data types in the same list
    list_iteration(numbers) 

    print("")

    # Test different container types
    list_demo()
    tuple_demo()
    set_demo()
    dict_demo()


def list_demo():
    print("***LIST DEMO***")
    my_list = ["h","e", "l", "l", "o"] # you can use either "" (double quotes) or '' (single quotes) - as long as you are consistent
   
    # Add an item to the list
    my_list.append("!")
    print(my_list) # Prints the entire list, exactly how it is written in code (except it prints single quotes instead of double quotes (what we used))
                                         
    # Get the number of items
    print(len(my_list)) # len function gives the NUMBER of items

    # Use index to access specific item
    print(my_list[0]) # Prints h --> the item at index 0
    print(my_list[4:6]) # Prints ['o', '!'] --> item at index 4 INCLUSIVE to 6 NON-INCLUSIVE
    print(my_list[4:]) # Prints ['o', '!'] --> item at index 4 INCLUSIVE to last index
    # NEGATIVE INDEX is located from the end, back number of spots
    print(my_list[-2:]) # Prints ['o', '!'] --> item at 4 until the end

    # Remove the first 'l'
    my_list.remove("l") # removes the first time it sees the character 'l'
    # Insert an item at a index
    my_list.insert(1, "l")
    print(my_list) # Prints ['h', 'l', 'e', 'l', 'o', '!']

    # Check if a certain value exists in a list
    # x in sequence - boolean expression
    print("!" in my_list) # Prints True

    # Sort our list in reverse order
    # Sorts the list in "alphabetical" order backwards
    # Symbol comes before the letter alphabet
    my_list.sort(reverse = True)
    print(my_list)


# Note: Function that comes as a obj.function is a funciton ASSOCIATED with that object


def tuple_demo():   
    print()                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    print("***TUPLE DEMO****")
    # Tuples are IMMUTABLE
    person = ('Courtney', 17, 'Brooklyn, NY')
    name, age, hometown = person
    print(name)
    print(age)
    print(hometown)
     # Create multiple variables in one line


def set_demo():
    print()
    print("***SET DEMO***")
    my_set = set()
    my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    # SETS are MUTABLE
    my_set.add(0) # will insert in ORDER! (SETS are ordered from least go greatest)
    my_set.remove(4)
    print(my_set)
    # Sets can Only contain UNIQUE values
    my_set.add(8)
    print(my_set) # doesn't brake the program but ignores it

    other_set = {2, 4, 6, 8, 10}
    # Useful math operations between two sets
    print(my_set.union(other_set)) 
    print(my_set.intersection(other_set)) # prints what they HAVE in common
    print(my_set.difference(other_set)) #pritns what they DONT have in common

def dict_demo():
    print("***DICTIONARY DEMP***")


 # Optional requirments have to come AFTER the required requirments
def bake_cookie(ingredients, instructions, temperature, cookie_cutter="snowman"): 
    print()
    print("***Snickerdoodle Recipie****")
    # Print the list of ingredients 
    print("* List of Ingredients:")
    for ingred in ingredients:
        print(ingred)

    # Print the oven temperature setting/
    print(f"* Set the oven to {temperature} degrees Kelvin.")

    # Print the instructions
    print(instructions)

    # Tell them which cookie cutter to use
    print(f"* Now cut your cookies with a {cookie_cutter} cookie cutter", end="\n\n")


def calculate_numbers(x, y, operation="add"):  
    # x and y are positional arguments and the order matters.
    # operation="add" is a keyword argument and is optional.
    if operation == "add":
        return x + y
    elif operation == "subtract": # elif means else if
        return x - y

# Different ways to modify values while iterating 
def list_iteration(input_list): 
    # 1. Create a new list as you loop
    new_list = []
    for item in input_list: 
        # append means add to a list
        new_list.append(item * 2)
    print(new_list)

    # 2. LIST COMPREHENSION
    input_list = [item * 2 for item in input_list]
    print(input_list)


if __name__ == "__main__":
    main()

# errors are called exceptions in Python 