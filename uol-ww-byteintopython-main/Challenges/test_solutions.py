# Tests to check your solutions to the challenges work.
#

import solutions


def test_longest_word():
    sentence = "a short sentence"
    assert 8 == solutions.find_longest_word(sentence)
    
    sentence = "Byte into Python at Lincoln"
    assert 7 == solutions.find_longest_word(sentence)
    
    sentence = "hello computer science and games computing students"
    assert 9 == solutions.find_longest_word(sentence)
    
#-------- 
    
def test_move_capitals_to_front():
    word = "eHllo"
    assert "Hello" == solutions.move_capitals_to_front(word)
    
    word = "AeHllo"
    assert "AHello" == solutions.move_capitals_to_front(word)
    
    word = "otherWoRds"
    assert "WRotherods" == solutions.move_capitals_to_front(word)
    
#-------- 

    
def test_fizzbuzz():
    result = [1, 2, "Fizz", 4, "Buzz"]
    assert result == solutions.fizzbuzz(5)
    result = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16]
    assert result == solutions.fizzbuzz(16)
 
#-------- 

def test_number_of_open_doors():
    assert 10 == solutions.number_of_open_doors(100)
    assert 9 == solutions.number_of_open_doors(99)
    assert 7 == solutions.number_of_open_doors(50)
    assert 3 == solutions.number_of_open_doors(10)

#-------- 

def test_distribute_chocolates():
    assert 2 == solutions.distribute_chocolates(3, [4, 10, 3, 1, 2, 8])
    assert 2 == solutions.distribute_chocolates(3, [4, 10, 3, 1, 2, 8, 10])
    assert 0 == solutions.distribute_chocolates(2, [4, 10, 3, 1, 2, 8, 10, 11])
    assert 7 == solutions.distribute_chocolates(5, [4, 10, 3, 1, 2, 8, 10, 11])
   
#-------- 

def test_change_options():
    assert 1 == solutions.change_options(10, [5]) 
    assert 2 == solutions.change_options(9, [3, 6, 4]) 
    assert 7 == solutions.change_options(10, [3, 1, 5]) 
 
#-------- 
 
def test_knapsack():
    capacity = 10
    weights = [3, 6, 10]
    values = [50, 60, 100]
    assert 110 == solutions.knapsack(capacity, weights, values, len(values))
    
    capacity = 10
    weights = [10, 10, 10]
    values = [50, 60, 100]
    assert 100 == solutions.knapsack(capacity, weights, values, len(values))
    
    capacity = 20
    weights = [10, 15, 10, 1, 5]
    values = [50, 60, 100, 50, 40]
    assert 190 == solutions.knapsack(capacity, weights, values, len(values))


