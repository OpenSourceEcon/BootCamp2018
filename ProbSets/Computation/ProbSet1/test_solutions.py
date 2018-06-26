# test_solutions.py
"""Volume 1B: Testing.
<Zeshun Zong>
<OSM lab>
<June 2018>
"""

import solutions as soln
import pytest

# Problem 1: Test the smallest_factor function from solutions.py
'''
After the test we can see that the function fails when the for loop could not execute.
This happens when int(n**0.5) < 2.
To correct it, we should change (int(n**0.5)) to (int(math.sqrt(n)+1))
'''
def test_smallest_factor():
    assert soln.smallest_factor(1)==1, "when n = 1"
    assert soln.smallest_factor(2)==2, "when n = 2"
    assert soln.smallest_factor(3)==3, "when n = 3"
    assert soln.smallest_factor(4)==2, "when n = 4"
    assert soln.smallest_factor(6)==2, "when n = 6"

# Problem 2: test month_length()
def test_month_length():
    assert soln.month_length("January") == 31, "in Jan"
    assert soln.month_length("February", True) == 29, "in Feb, leap year"
    assert soln.month_length("February", False) == 28, "in Feb, not leap year"
    assert soln.month_length("April") == 30, "in April"
    assert soln.month_length("AAAA") == None, "when invalid input"

# Problem 3: Test the operate() function from solutions.py
def test_operate():
    #test good cases
    assert soln.operate(2,1, "+") == 3, "plus"
    assert soln.operate(2,1, "-") == 1, "minus"
    assert soln.operate(2,1, "*") == 2, "multiply"
    assert soln.operate(2,1, "/") == 2, "divide"
    #test exceptions
    with pytest.raises(ZeroDivisionError) as excinfo:
        soln.operate(4, 0, "/")
    assert excinfo.value.args[0] == "division by zero is undefined"

    with pytest.raises(TypeError) as excinfo:
        soln.operate(4, 0, 1)
    assert excinfo.value.args[0] == "oper must be a string"

    with pytest.raises(ValueError) as excinfo:
        soln.operate(4, 0, "!")
    assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"


# Problem 4, test fraction class
@pytest.fixture
def set_up_fractions():
    frac_1_1 = soln.Fraction(1, 1)
    frac_1_3 = soln.Fraction(1, 3)
    frac_1_2 = soln.Fraction(1, 2)
    frac_n2_3 = soln.Fraction(-2, 3)
    return frac_1_1, frac_1_3, frac_1_2, frac_n2_3
def test_fraction_init(set_up_fractions):
    frac_1_1, frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_3.numer == 1
    assert frac_1_2.denom == 2
    assert frac_n2_3.numer == -2
    frac = soln.Fraction(30, 42)
    assert frac.numer == 5
    assert frac.denom == 7

    with pytest.raises(ZeroDivisionError) as excinfo:
        soln.Fraction(4, 0)
    assert excinfo.value.args[0] == "denominator cannot be zero"

    with pytest.raises(TypeError) as excinfo:
        soln.Fraction(2.1, 2)
    assert excinfo.value.args[0] == "numerator and denominator must be integers"

def test_fraction_str(set_up_fractions):
    frac_1_1, frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert str(frac_1_3) == "1 / 3"
    assert str(frac_1_2) == "1 / 2"
    assert str(frac_n2_3) == "-2 / 3"
    assert str(frac_1_1) == "1"
def test_fraction_float(set_up_fractions):
    frac_1_1, frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert float(frac_1_3) == 1 / 3.
    assert float(frac_1_2) == .5
    assert float(frac_n2_3) == -2 / 3.

def test_fraction_eq(set_up_fractions):
    frac_1_1, frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 == soln.Fraction(1, 2)
    assert frac_1_3 == soln.Fraction(2, 6)
    assert frac_n2_3 == soln.Fraction(8, -12)
    assert frac_1_1 == 1


'''The expression in the function ADD is wrong, I have changed it'''
def test_fraction__add(set_up_fractions):
    frac_1_1, frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert soln.Fraction(1, 2) + soln.Fraction(1, 2) == 1
    assert frac_1_3 + frac_n2_3 == soln.Fraction(-1, 3)

'''The expression in the function SUB is wrong, I have changed it'''
def test_fraction__sub(set_up_fractions):
    frac_1_1, frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_1 - frac_1_2 == frac_1_2
    assert frac_1_1 - frac_n2_3 == soln.Fraction(5, 3)

def test_fraction__mul(set_up_fractions):
    frac_1_1, frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_1 * frac_1_3 == frac_1_3
    assert frac_1_2 * frac_n2_3 == soln.Fraction(-1, 3)

def test_fraction_true_div():
    with pytest.raises(ZeroDivisionError) as excinfo:
        soln.Fraction(1, 1) / soln.Fraction(0, 1)
    assert excinfo.value.args[0] == "cannot divide by zero"

    assert soln.Fraction(1, 1) / soln.Fraction(1, 2) == 2




# Problem 5 & 6 the SET
def test_is_set():
    assert soln.is_set("1022", "1122", "1020") == False
    assert soln.is_set("0000", "1111", "2222") == True
    assert soln.is_set("0102", "0102", "0102") == True

def test_count_sets():
    hand1 = ["1022", "1122", "0100", "2021",
         "0010", "2201", "2111", "0020",
         "1102", "0210", "2110", "1020"]
    hand2 = ["1022", "1122", "0100", "2021",
         "0010", "2201", "2111", "0020",
         "1102", "0210", "2110"] #only 11 elements
    hand3 = ["1022", "1122", "0100", "2021",
         "0010", "2201", "2111", "0020",
         "1102", "0210", "2110", "102"] #one has 3 digits
    hand4 = ["1022", "1122", "0100", "2021",
         "0010", "2201", "2111", "0020",
         "1102", "0210", "2110", "1030"] #one has char !012

    with pytest.raises(ValueError) as excinfo:
        soln.count_sets(hand2)
    assert excinfo.value.args[0] == "must have exactly 12 cards"

    with pytest.raises(ValueError) as excinfo:
        soln.count_sets(hand3)
    assert excinfo.value.args[0] == "each card should have exactly 4 digits"

    with pytest.raises(ValueError) as excinfo:
        soln.count_sets(hand4)
    assert excinfo.value.args[0] == "character can only be 0 1 2"
    assert soln.count_sets(hand1) == 6
