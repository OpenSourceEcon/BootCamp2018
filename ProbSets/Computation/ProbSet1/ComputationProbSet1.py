'''
Computational Section Problem Set 1
Zeshun Zong
OSM Lab 2018

Please note that, unless otherwise specified, function definitions for problems are listed below.
Executable calls are provided, comment them if needed
'''

import numpy as np
import calculator
import itertools
import sys, os, random, time
import box
import math
from random import choice


'''
Part 1: Intro to Numpy lab
'''
# Problem 1
def return_product():
    A = np.array([[3, -1, 4], [1, 5, -9]])
    B = np.array([[2, 6, -5, 3], [5, -8, 9, 7], [9, -3, -2, -3]])
    return np.dot(A, B)
print(return_product())

#Problem 2
def get_result():
    A = np.array([[3, 1, 4], [1, 5, 9], [-5, 3, 1]])
    result = np.dot(np.dot(A, A), A)*(-1) + 9*np.dot(A, A) - 15*A
    return result
print(get_result())

#Problem 3
def matrix_def_and_product():
     A = np.triu(np.ones((7,7)))
     #print(A)

     B_lower = np.tril(np.full_like(A, -1))
     B_uppper = np.triu(np.full_like(A, 5)) - np.diag([5,5,5,5,5,5,5])
     B = B_lower + B_uppper
     #print(B)

     return np.dot(np.dot(A,B),A)
print(matrix_def_and_product())

#Problem 4
def change_negative_to_zero(arr):
    myarr = np.copy(arr)
    negative_positions = myarr < 0
    myarr[negative_positions] = 0
    return myarr
arr = np.array([[-1,1,-1],[-1,1,-1]])
print(change_negative_to_zero(arr))

#Problem 5
def combine_matrix():
    A = np.arange(6)
    A = A.reshape((3,2))
    A = A.T

    B = np.full((3,3), 3)
    B = np.tril(B)

    C = np.diag([-2, -2, -2])

    left_column = np.vstack((np.zeros((3,3)), A, B))
    mid_column = np.vstack((A.T, np.zeros((left_column.shape[0]-3, 2))))
    right_column = np.vstack((np.eye(3), np.zeros((2,3)), C))

    result = np.hstack((left_column, mid_column, right_column))

    return result
print(combine_matrix())

#Problem 6
def convert_to_stochatic_matrix(matrix):
    row_sum =(matrix.sum(axis = 1)).reshape((-1,1))
    result = matrix / row_sum
    return result

A = np.array([[1,2,2],[3,4,5]])
print(convert_to_stochatic_matrix(A))

#Problem 7
def max_adjacent_product():
    grid = np.load("grid.npy")

    row_product = grid[:, 0:-3] * grid[:, 1:-2] * grid[:, 2:-1] * grid[:, 3:]
    row_max = np.max(row_product)

    column_product = grid[0:-3,:] * grid[1:-2,:] * grid[2:-1,:] * grid[3:,:]
    column_max = np.max(column_product)

    diag_product = grid[0:-3, 0:-3] * grid[1:-2, 1:-2] * grid[2:-1, 2:-1] * grid[3:, 3:]
    diag_max = np.max(diag_product)

    return np.max([row_max, column_max, diag_max])
print(max_adjacent_product())

'''
Part 2: Standard Library lab
'''
#Problem 1
def returnMinMaxAvg(L):
    return min(L), max(L), sum(L)/len(L)
print(returnMinMaxAvg([1,2,3]))

#Problem 2
def test_immutable():
    integer = 3
    integer_prime = integer
    integer_prime +=1
    print(integer, integer_prime)
    #int is immutable

    string = "abc"
    string_prime = string
    string_prime += "d"
    print(string, string_prime)
    #str is immutable

    list1 = [1,2,3]
    list2 = list1
    list2.append(4)
    print(list1, list2)
    #list is mutable

    tuple1 = (1,2,3)
    tuple2 =  tuple1
    tuple2 += (1,)
    print(tuple1, tuple2)
    #tuple is immutable

    set1 = {1,2,3}
    set2 = set1
    set2.add(4)
    print(set1, set2)
    #set is mutable

    print("int is immutable \nstr is immutable \nlist is mutable")
    print("tuple is immutable \nset is mutable")

test_immutable()

#Problem 3
def get_hypotenuse(a, b):
    a_sq = calculator.get_product(a,a)
    b_sq = calculator.get_product(b,b)
    h_sq = calculator.get_sum(a_sq, b_sq)
    return calculator.sqrt(h_sq)

print(get_hypotenuse(3,4))

#Probem 4
def get_power_set(A):
    num_of_element = len(A)
    power_set = [{}]
    #\emptyset is always in the power set
    #find the full combinations consisting of elements from 1 to all elements
    for i in range(1,num_of_element+1):
        temp = list(itertools.combinations(A, i))
        #temp is a list of tuples, where each tuple has i elements
        for t in temp:
            power_set.append(set(t))
        #convert each tuple to a set
    return power_set

print(get_power_set({1,2,3}))
print("We cannot have a set of set, because mutable objects cannot be put into a set, as they are not hashable.")

'''
Problem 5 in Standard Library Lab must be executed from the terminal.
Please see separate script in the folder.
'''


'''
Problems in Part 3 Unit Test Lab are written in separate files: solutions.py and test_solutions.py
They are included in the folder.
Please execute using pytest in the terminal
'''

'''
Part 4 OOP Lab
'''
#Problem 1
class Backpack:

    """A Backpack object class. Has a name and a list of contents.
    Attributes:
        name (str): the name of the backpack's owner.
        contents (list): the contents of the backpack.
        color (str): color of backpack
        max_size (int): the maximum capacity of the backpack
    """
    def __init__(self, name, color, max_size =5):           # This function is the constructor.
        """Set the name and initialize an empty list of contents.
        Parameters:
            name (str): the name of the backpack's owner.
            color (str): color
            max_size (int): default 5
        """
        self.name = name                # Initialize some attributes.
        self.contents = []
        self.color = color
        self.max_size = max_size

    def put(self, item):
        """Add 'item' to the backpack's list of contents.
            if the size of the backpack is full, do not add and print a message
        """

        if len(self.contents) == self.max_size:
            print("No room!")
        else:
            self.contents.append(item)  # Use 'self.contents', not just 'contents'.

    def take(self, item):
        """Remove 'item' from the backpack's list of contents."""
        self.contents.remove(item)

    def dump(self):
        """Set contents to an empty list"""
        self.contents=[]

    def __eq__(self, other):
        if (self.name == other.name) and (self.color == other.color) and (len(self.contents) == len(other.contents)):
            return True
        return False
    def __str__(self):
        s1 = "Owner:     " + str(self.name)
        s2 = "Color:     " + str(self.color)
        s3 = "Size:      " + str(len(self.contents))
        s4 = "Max Size:  " + str(self.max_size)
        s5 = "Contents:  " + str(self.contents)
        return s1 + "\n" + s2 + "\n" + s3 + "\n" + s4 + "\n" + s5



def test_backpack():
    testpack = Backpack("Barry", "black")       # Instantiate the object.
    if testpack.name != "Barry":                # Test an attribute.
        print("Backpack.name assigned incorrectly")
    for item in ["pencil", "pen", "paper", "computer"]:
        testpack.put(item)                      # Test a method.
    print("Contents:", testpack.contents)
    testpack.put("apple")
    testpack.put("pear") #should not be able to do so
    testpack.dump()
    print("Contents:", testpack.contents) #should be empty

test_backpack()

#Problem 2
class Jetpack(Backpack):
    """A Jetpack object class.
    Attributes:
        name (str): the name of the backpack's owner.
        contents (list): the contents of the backpack.
        color (str): color of backpack
        max_size (int): the maximum capacity of the backpack
        fuel (int): amout of fuel left
    """
    def __init__(self, name, color, fuel = 10, max_size = 2):           # This function is the constructor.
        """Set the name and initialize an empty list of contents.
        Parameters:
            name (str): the name of the backpack's owner.
            color (str): color
            max_size (int): default 2
            fuel (int): default 10
        """
        Backpack.__init__(self, name, color, max_size)
        self.fuel = fuel

    def fly(self, fuel_needed):
        """Decrease certain amount of fuel from the tank, if there is enough fuel
        Parameters:
            fuel_needed (int): the amount of fuel to be decreased
        """
        if fuel_needed > self.fuel:
            print("Not enough fuel!")
        else:
            self.fuel = self.fuel - fuel_needed

    def dump():
        """Override, dump both contents and fuel
        """
        self.contents = []
        self.fuel = 0

"""
Please note that problem 3 asks to add magic methods to Backpack class.
This has be imposed in the class definitions. See above.
"""
p1 = Backpack("Simon", "Red")
p1.put("A")
p1.put("B")
p2 = Backpack("Simon", "Red")
p2.put("C")
print(p1 == p2) #expect FALSE
p2.put("D")
print(p1 == p2) #expect TRUE
print(p1)

#Problem 4
class ComplexNumber:
    """ an object representation of complex number a + bi
    Attributes:
        real (float): Re(z)
        imag (float): Im(z)
    """
    def __init__(self, re, im):
        """ constructor
        Parameters:
            re (float): Re(z)
            im (float): Im(z)
        """
        self.real = re
        self.imag = im

    def conjugate(self):
        """change z to conj(z)"""
        return ComplexNumber(self.real, -self.imag)

    def __str__(self):
        """return string representation"""
        if (self.imag >= 0):
            return "(" + str(self.real) + "+" + str(abs(self.imag)) + "j" + ")"
        else:
            return "(" + str(self.real) + "-" + str(abs(self.imag)) + "j" + ")"

    def __abs__(self):
        """return |z|"""
        return math.sqrt(self.real**2 + self.imag**2)

    def __eq__(self, other):
        return (self.real == other.real) and (self.imag == other.imag)

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        newRe = self.real * other.real - self.imag * other.imag
        newIm = self.imag * other.real + self.real * other.imag
        return ComplexNumber(newRe, newIm)

    def __truediv__(self, other):
        if (other.real == 0 and other.imag == 0):
            raise ZeroDivisionError
        else:
            newRe = (self.real * other.real + self.imag * other.imag) / (abs(other)**2)
            newIm = (self.imag * other.real - self.real * other.imag) / (abs(other)**2)
            return ComplexNumber(newRe, newIm)


def test_ComplexNumber(a, b):
    py_cnum, my_cnum = complex(a, b), ComplexNumber(a, b)
    # Validate the constructor.
    if my_cnum.real != a or my_cnum.imag != b:
        print("__init__() set self.real and self.imag incorrectly")
    # Validate conjugate() by checking the new number's imag attribute.
    if py_cnum.conjugate().imag != my_cnum.conjugate().imag:
        print("conjugate() failed for", py_cnum)
    # Validate __str__().
    if str(py_cnum) != str(my_cnum):
        print("__str__() failed for", py_cnum)

    py_cnum2 = complex(3,4)
    my_cnum2 = ComplexNumber(3, 4)
    #validate add
    system_add = py_cnum + py_cnum2
    my_add = my_cnum + my_cnum2
    if system_add.real != my_add.real or system_add.imag != my_add.imag:
        print("__add__() incorrectly")

    #validate __sub__
    system_sub = py_cnum - py_cnum2
    my_sub = my_cnum - my_cnum2
    if system_sub.real != my_sub.real or system_sub.imag != my_sub.imag:
        print("__sub__() incorrectly")

    #validate __mul__
    system_mul = py_cnum * py_cnum2
    my_mul = my_cnum * my_cnum2
    if system_mul.real != my_mul.real or system_mul.imag != my_mul.imag:
        print("__mul__() incorrectly")

    #validate __truediv__
    system_div = py_cnum / py_cnum2
    my_div = my_cnum / my_cnum2
    if system_div.real != my_div.real or system_div.imag != my_div.imag:
        print("__add__() incorrectly")

test_ComplexNumber(1,2)

"""
Part 5 Exception, File IO
"""

#Problem 1
def arithmagic():
    step_1 = input("Enter a 3-digit number where the first and last "
                                           "digits differ by 2 or more: ")

    x1 = int(step_1)
    if x1 not in range(100, 1000):
        raise ValueError("The first number is not a three digit number")

    first_digit_x1 = x1 // 100
    last_digit_x1 = x1 % 10
    if (last_digit_x1 - first_digit_x1) < 2:
        raise ValueError("The first number’s first and last digits differ by less than 2.")

    step_2 = input("Enter the reverse of the first number, obtained "
                                              "by reading it backwards: ")
    if (step_1[0] != step_2[2]) or (step_1[1] != step_2[1]) or (step_1[2] != step_2[0]):
        raise ValueError("The second number is not the reverse of the first number")
    step_3 = input("Enter the positive difference of these numbers: ")
    x2 = int(step_2)
    x3 = int(step_3)
    diff = abs(x2 - x1)



    if x3 !=  diff:
        raise ValueError("The third number is not the positive difference of the first two numbers.")

    step_4 = input("Enter the reverse of the previous result: ")
    if (step_3[0] != step_4[2]) or (step_3[1] != step_4[1]) or (step_3[2] != step_4[0]):
        raise ValueError("The second number is not the reverse of the first number")
    print(str(step_3), "+", str(step_4), "= 1089 (ta-da!)")

#arithmagic()

#Problem 2
def random_walk(max_iters=1e12):
    try:
        walk = 0
        directions = [1, -1]
        for i in range(int(max_iters)):
            walk += choice(directions)

    except KeyboardInterrupt as e:
        print("Process interrupted at iteration ", i)
        raise

    else:
        print("process completed.")
    finally:
        return walk

#w = random_walk()
#print(w)

"""
Problem 3 and 4 are written together. Change file name and contents to test functionsself.
"""
class ContentFilter:
    def __init__(self, fileName):
        flag = False
        while flag == False:
            try:
                f1 = open(fileName, "r")
            except FileNotFoundError as e1:
                fileName = input("Enter a valid file name: ")
            except TypeError as e2:
                fileName = input("Enter a valid file name: ")
            except OSError as e3:
                fileName = input("Enter a valid file name: ")
            else:
                flag = True
                #print("File has been opened")

        self.name = fileName
        self.contents = f1.read()
        f1.close()
        #print("File has been closed")

    def uniform(self, outfile, mode="w", case = "upper"):
        if mode not in ["w", "x", "a"]:
            raise ValueError("File access mode incorrect")

        if case == "upper":
            tobewritten = (self.contents).upper()

        elif case == "lower":
            tobewritten = (self.contents).lower()
        else:
            raise ValueError("Letter case incorrect")

        nf = open(outfile, mode)
        nf.write(tobewritten)
        print("contents successfully written to ", outfile)

    def reverse(self, outfile, mode = "w", unit = "line"):
        nf = open(outfile, mode)
        if mode not in ["w", "x", "a"]:
            raise ValueError("File access mode incorrect")
        if unit == "line":
            listOfLines = (self.contents).split("\n")
            listOfLines.reverse()
            for line in listOfLines:
                nf.write(line + "\n")
        elif unit == "word":
            listOfLines = (self.contents).split("\n")
            for line in listOfLines:
                sublistOfWords = line.split()
                sublistOfWords.reverse()
                for word in sublistOfWords:
                    nf.write(word+" ")
                nf.write("\n")

        else:
            raise ValueError("unit incorrect")

    def transpose(self, outfile, mode = "w"):
        nf = open(outfile, mode)
        if mode not in ["w", "x", "a"]:
            raise ValueError("File access mode incorrect")
        #assume equal number of words in each line
        listOfLines = (self.contents).split("\n")
        matrix = []
        for line in listOfLines:
            sublistOfWords = line.split()
            matrix.append(sublistOfWords)

        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                nf.write(matrix[j][i] + " ")
            nf.write("\n")

f = ContentFilter("testForFileIO.txt")
#f.uniform("newfile.txt", case = "lower")
#f.reverse("newfile.txt", unit = "word")
f.transpose("newfile.txt")
