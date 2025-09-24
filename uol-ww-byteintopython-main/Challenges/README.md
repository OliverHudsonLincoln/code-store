# :zap: Challenges

Have a go at the challenges listed below. You don't have to do them in order. Help each other and make sure everyone in the team has a go at typing an answer. 

After you have completed a challenge, add your solution to ```solutions.py```. Commit and push your changes -- did the test for that challenge pass?

To test offline: open a terminal window, change to the directory your solutions.py file is in and enter ```pytest test_solutions.py::<name of test method>```, replacing ```<name of test method>``` with the name of the test method e.g., ```pytest test_solutions.py::test_change_options```.

Try to solve the challenges without looking at the solution online (you can of course search for Python functions and syntax -- but try not to just look-up the complete solution :smiley_cat:). 

## Challenge 1: Find the longest word  

Write a function that takes in a sentence and returns the length of the longest word in that sentence. 
The function must be called ```find_longest_word``` and it must have a single parameter (i.e. the string/sentence). 

For example, when provided the string "My name is Sabrina and I am Derek's cat.", your function should return 7. 


## Challenge 2 – Move Capital Letters to the Front  

Write a function that takes in a word (a string) and moves all the capital letters to the start of that string. 
The function must be called ```move_capitals_to_front``` and it must have a single parameter (i.e. the string).

For example, when provided the string "eHllo" the function should return "Hello". 

(Hint: python strings have a isupper function.) 

## Challenge 3 – :tropical_drink: FizzBuzz 

In FizzBuzz, players count up from 1 to n. Multiples of 3 are replaced by "Fizz"; multiples of 5 are replaced by "Buzz", and multiple of both 3 and 5 are replaced by "FuzzBuzz". 
Write a ```fizzbuzz``` function that takes n as input and outputs an array. 

For example, ```fizzbuzz(16)``` should output ```[1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16]```
 

## Challenge 4 – :door: Open Doors 

Consider a long alley with a number of doors (N doors) on one side. All the doors are closed initially. You move to and fro in the alley changing the states of the doors as follows: you open a door that is already closed and you close a door that is already opened. You start at one end go on altering the state of the doors till you reach the other end and then you come back and start altering the states of the doors again.

In the first go, you alter the states of doors numbered 1, 2, 3... \
In the second go, you alter the states of doors numbered 2, 4, 6... \
In the third go, you alter the states of doors numbered 3, 6, 9... \
You continue this till the Nth go in which you alter the state of the door numbered N.

How many doors are left open after executing the above procedure?

Write a function called ```number_of_open_doors``` that executes the above procedure. It should take in a single value (i.e., N -- the number of doors).


## Challenge 5 – :chocolate_bar: Chocolates 

You have a collection of packets of chocolates. The packets have a variable number of chocolates (e.g. packet 1 contains 4 chocolates, packet 2 contains 3 chocolates). You must distribute chocolate packets among students such that:

1) Each student gets exactly one packet.
2) The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is as low as possible.  

The packets of chocolates can be represented as an array, where each value represents the number of chocolates in the packet (e.g. ```packets = [4, 10, 3, 1]```). The students can be represented as an integer (e.g. ```number_of_students = 2```). \
You must output the difference between maximum chocolates and minimum chocolates in packets assigned to the students. In the example, the packets assigned to the two students could be ```[3,4]```, thus the output is 1.  

Write a function called ```distribute_chocolates``` that takes two parameters: 1) the number of students and 2) the array of packets, and returns a single value. 
 


## Challenge 6 – :money_with_wings: ATM Change [Very Hard] 

Imagine you are building an ATM. You need to figure out how many different ways a given amount of money can be broken into coins. For example, if the amount is 9 and you have the coins valued at ```[3,4,5,10]``` the answer would be 2 as there are two was of making up that amount:

4 + 5 \
3 + 3 + 3

Note, you have unlimitted amounts coins for each of the given values. 

Write a function called ```change_options``` that takes two paramters: 1) the amount needed and 2) the values of the coins in the ATM. This function returns a single value (i.e. the number of ways to make up that amount). 


__Finding this one too hard?__ Ask copilot for the solution and test out that solution. Get copilot to explain the solution to you.
 

## Challenge 7 – :cop: Knapsack [Very Hard] 

Imagine you are a thief who has just broken into someone's house. There is a limitted amount of weight you can carry, and you want to make the most money possible. You need to decide which items to steal. 

Write a function called ```knapsack``` that takes three parameters: 1) the maximum weight you can carry, 2) a list containing the weight of the items in the house and 3) a list containing the value of the items in the house (for both lists the items are in the same order). You need to return the total value of the items you will take from the house. 

For example, if the capacity is 10, the item weights are [3, 6, 10] and the item values [50, 60, 100], then the output would be 110 (as the thief would steal the first item and the second items). 


__Finding this one too hard?__ Ask copilot for the solution and test out that solution. Get copilot to explain the solution to you.





