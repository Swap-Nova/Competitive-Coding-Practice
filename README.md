# Competitive-Coding-Practice

## Fibonacci sequence
The Fibonacci sequence is a set of numbers that starts with a one or a zero, followed by a one, and proceeds based on the rule that each number (called a Fibonacci number) is equal to the sum of the preceding two numbers.
The code written through Python Language uses the concept of loops & functions.
```bash 
def recur_fibonacci(n):
    if(n<=1):
        return n
    else:
        return(recur_fibonacci(n-1)+recur_fibonacci(n-2))
```
The code uses the concept of functions & loops.
We have created the if-else loops two times because the user might input a negative number & we know that the Fibonacci number does not contain any negative numbers.
In the end, we perform a for-loop operation that prints the numbers till the user desires.

## Switch Case Enumerations
A switch statement allows a variable test for equality against a list of values. Each value is called a case, and the variable an operation switched on checks for each case.
Once a match is made, all the code in the switch case, including and following that match will be executed until we hit a break statement.
 Enum or enumeration is a data type consisting of named values like elements, members, etc., that represent integral constants. 
In this the enumerations are the directions in a map-  west, east, north, south.
```bash
enum Direction{
        west, east, north, south
};
```

## Using Recursion to the add the sum of digits:
### The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called as recursive function.
### Logic to approach this problem:
#### 
* Firstly, find the last number using modular division by 10.
  * Adding the last digit found above to the 'sum' variable. <br>
  * Remove last digit from given number by dividing it by 10.
```bash
if(n==0)
    return 0;  
return ((n%10) + sum_of_digits(n/10));
```
