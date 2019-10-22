"""
Sum Squared Digits Function
Originally located here: https://csumb.kattis.com/problems/sumsquareddigits

Below is the description for a stretch problem. Part of this problem lies in understanding the prompt. Try to focus on the input, and the sample code you've been given, which should give you a hint.


The Sum Squared Digits function, SSD(b,n) of a positive integer n, in base b is defined by representing n in base b as in:

n=a0+a1∗b+a2∗b2+ … n=a0+a1∗b+a2∗b2+…

then:
SSD(b,n)=a2^0+a2^1+a2^+…SSD(b,n)=a0^2+a1^2+a2^2+…
is the sum of squares of the digits of the representation.
Write a program to compute the Sum Squared Digits function of an input positive number.

In English:
The goal of this problem is to convert the base-10 number, n, into base b, and then sum the square of those digits.


Input
The first line of input contains a single decimal integer P, (1≤P≤1000), which is the number of data sets that follow. Each data set should be processed identically and independently.

Each data set consists of a single line of input. 
It contains the data set number, K, 
followed by the base, b (3≤b≤16) as a decimal integer, 
followed by the positive integer, n (as a decimal integer) for which the Sum Squared Digits function is to be computed with respect to the base b. n will fit in a 32 bit unsigned integer. The data set number K starts at 1 and is incremented by 1 for each data set.


Output

For each data set there is a single line of output.
The single line of output consists of the data set number, K, 
followed by a single space followed by the value of SSD(b,n) as a decimal integer.

"""

def sum_of_squares(k, b, n):
    while n != 0:
        remainder = n % b
        n = int(n / b)
        print(remainder)


# read first line
number_of_lines = int(input())

# read all remaining lines
for i in range(number_of_lines):
    line = input()
    args = line.split()
    k = int(args[0])
    b = int(args[1])
    n = int(args[2])

    sum_of_squares(k, b, n)
