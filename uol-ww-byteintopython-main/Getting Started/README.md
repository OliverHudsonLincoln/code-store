# Introduction to Python and Github classroom

This activity gets you to write your first lines of Python (if you haven't written Python before) and allows you to learn how to use github classroom. 

1. Open up the hello_world.py file and try running it.
2. Copy the following block of code into hello_world.py:
    ```
    # We use "def" to define a function.
    # This sum function takes two parameters, a and b. 
    def sum_two_values(a, b):
        return a + b
    
    # create two variables and assign integer values to them: 
    first = 2 
    second = 3
    # call our sum function and store the result in "result":
    result = sum_two_values(first, second)
    # print the result to the console:
    print (result)
    ```
3. Try running this code.
4. Copy in and run the following code:
    ```
    def sum_all(values):
        total = 0
        # loop through all values, and add them to total
        for value in values:
            total = total + value
        return total
        
    values = [3,4,5]
    # Call the sum_all function, pass it "values".
    # Print the result
    ```
5. Commit your code to git and push it to github.
6. Check your tests passed!
