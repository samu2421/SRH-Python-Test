"""# Big Data Programming: Pyhton Module Test
# Instructions ...
# Please consider good style & naming while developing the code when necessary,
#  such as Docstring, linting, etc. it is considered in the grading process!
# Use this file for the solution only. Jupyter notebook(.ipynb) not acceptable!
# Push the solution to a remote repo of name "SRH-Python-Test", and send me the link of the repo as DM
#  on Ms Teams for assessment.
# The duration of this test is 1 hour.

# Q1: What is the main difference between the list and Tuple?
# In python, objects in list as iterable, while objects in tupple are unique and cannot be repeated twice.


# Q2: why should list indexing be used Python?
# Indexing objects in list help a developer to assign a unique value to every object within the list and also help to easily retrieve it."""


# Q3: You have two lists (string_list, values_list) below. Write a function of
#  a name count_car. The function returns a dictionary.
#  The expected return of the function should print out this dictionary:
#  {'Audi_Q5': 2, 'Honda_civic': 4, 'Mercedes_200E': 5, 'BMW_720': 7, 'VW_passat': 2}

string_list = ['Audi_Q5', 'Honda_civic', 'Mercedes_200E', 'Honda_civic',
               'BMW_720', 'VW_passat']

value_list = [2, 4, 5, 7, 2]

# Your code here ...
def car_count(string_list, value_list):
    car_count = {}      #dictionary to store the count of the cars
    
    for car, value in zip(string_list, value_list):
        if car in car_count:
            car_count[car] += value
        else:
            car_count[car] = value
    
    return car_count

#Print the result
output = car_count(string_list, value_list)
print(output)


# Q4: Write a function of a name double_even_numbers. The function squares the
#  even numbers only. Also, the function leaves the first element of the input
#  as is without getting squared regardless being even or odd number.
#  The function has one argument which is a numpy array of 100 elements of
#  integer type between 0-10.
#  The function returns an array. Use list comprehension in your answer.

# Your code here ...
import numpy as np

def double_even_numbers(arr):
    result = np.array([arr[0]] + [x**2 if x % 2 == 0 else x for x in arr[1:]])
    return result

np.random.seed(42)
arr = np.random.randint(0, 11, 100)  
result = double_even_numbers(arr)
print(result)


# Q5: Read "movies.csv" file, a file is provided. Create a function
#  returns only table of elements before 2000 with score 7 and above, then save
#  the elements in a new csv file with a name "dest_csv". 

# Your code here ...
import pandas as pd

def filter_movies(input_csv, output_csv):
    movies = pd.read_csv(input_csv)
    filtered_movies = movies[(movies['year'] < 2000) & (movies['score'] >= 7)]
    
    filtered_movies.to_csv(output_csv, index=False)

filter_movies("movies.csv", "dest_csv.csv")



# Q6: Write a function of a name div_func. It returns the divsion of elements
#  in a list in reversed order. The function should pass the two lists below
#  without errors.

import random
random.seed(42)
short_list = [1, 0, 2, 2, 20]
long_list = [random.randrange(0, 10, 1) for i in range(15)]

# Your code here ...

