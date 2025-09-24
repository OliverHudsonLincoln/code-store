# SOLUTIONS
# enter your solutions into this file

def fizzbuzz(n):
    output=[]
    for x in range(1,n+1):
        if x%3==0 and not x%5==0:
            output.append("Fizz")
        if x%5==0 and not x%3==0:
            output.append("Buzz")
        if x%3==0 and x%5==0:
            output.append("FizzBuzz")
        else:
            output.append(x)
    return output

def number_of_open_doors(n):
    #0 = closed
    #1 = open
    arr=[]
    for x in range(0,n):
        arr.append(0)
    add=0
    while add != n:
        add+=1
        skip = add
        while skip <= n:
            if arr[skip-1]==0:
                arr[skip-1]=1
            elif arr[skip-1]==1:
                arr[skip-1]=0
            skip+=add          
    return arr.count(1)
            


