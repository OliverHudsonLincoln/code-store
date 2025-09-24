print("hello")
def sum_two_values(a, b):
    return a + b
first = 2 
second = 3
# call our sum function and store the result in "result":
result = sum_two_values(first, second)
# print the result to the console:
print (result)
def sum_all(values):
    total = 0
    # loop through all values, and add them to total
    for value in values:
        total = total + value
    return total
    
values = [3,4,5]
print(sum_all(values))