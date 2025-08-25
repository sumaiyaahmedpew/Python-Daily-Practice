# 🐍 Python Daily Practice

This repository contains my daily Python practice problems from the **Telusko YouTube tutorial series** and other sources.

---

## 📌 Note
- Problems **1 → 13** are available in my previous repository:  
  👉 [AssignmentAB1](https://github.com/sumaiyaahmedpew/AssignmentAB1)  
- Problems in this repository start from **Problem 14 onwards**.

---

## 📅 Topics Covered (21-08-2025)
- Variables, Data Types, Operators  
- For Loops, Break/Continue/Pass, For-Else  
- Pattern Printing  
- Prime Numbers  
- Arrays & User Input  
- Number System Conversion  
- Bitwise Operators  
- Math Functions  
- Swapping Variables  

---

## 📅 Topics Covered (23-08-2025)
- NumPy Basics (Why NumPy, Installing in PyCharm)  
- Creating Arrays with NumPy  
- Copying Arrays (shallow vs deep copy)  
- Working with Matrix in Python  
- Functions in Python  
- Function Arguments & Types of Arguments  
- Global vs Local Variables  
- Passing List/Array to Functions  

---

## 📅 Topics Covered (25-08-2025)
- Fibonacci Sequence  
- Factorial  
- Recursion  
- Factorial using Recursion  
- Anonymous Functions (Lambda)  
- Filter, Map, Reduce  
- Decorators  


## 📂 Problems List

### 🔹 Problem 14 – Pattern Printing Dashboard
Menu-driven pattern printer (Right-angle, Pyramid, Diamond).  
Uses: for loop, nested loops, break, continue.  

### 🔹 Problem 15 – Prime Analyzer
Finds all primes up to N using for-else.  
Stores in an array and prints count, smallest, largest.  
Checks if N itself is prime.  

### 🔹 Problem 16 – Student Marks with Arrays
Input marks of students, stored in an array.  
Prints average, highest, lowest.  
Stops if any student fails (<40) using break.  
Pass used if no student is added.  

### 🔹 Problem 17 – Number Pattern with Conditions
Input N.  
Skip even numbers using continue.  
Stop if divisible by 13 using break.  
Otherwise print star pattern.  

### 🔹 Problem 18 – Password Strength Checker
Checks if password contains digit, uppercase, lowercase, special char.  
If all present → Strong, else Weak.  
Empty password handled with pass.  

### 🔹 Problem 19 – Fibonacci Prime Filter
Generates first N Fibonacci numbers.  
Uses for-else to find primes among them.  
Stores primes in an array.  

### 🔹 Problem 20 – Library Book Borrow System
Menu-driven program.  
Options: Show books, Search, Borrow, Exit.  
Uses loops, break, continue.  

### 🔹 Problem 21 – Multiplication Table Manager
Prints multiplication table using for loop.  
Negative input → exit (break).  
Zero input → skip (pass).  

### 🔹 Problem 22 – Array Statistics Dashboard
Menu options: Show all, Odd/Even, Prime numbers, Reverse, Exit.  
Uses arrays, for-else, break/continue.  

### 🔹 Problem 23 – Student Result Analyzer (NumPy + Functions)
Stores marks of students in NumPy array.  
Functions: subject-wise average, highest, lowest.  
Student totals, averages, topper detection.  
Demonstrates positional, keyword, and default arguments.  

### 🔹 Problem 24 – Image Filter Simulator (Matrix with NumPy)
3×3 NumPy matrix as grayscale image.  
Functions: Brighten, Darken, Transpose.  
Demonstrates array manipulation inside functions.  

### 🔹 Problem 25 – Array Copy & Independence Check
Creates shallow and deep copies of NumPy arrays.  
Shows how shallow copy changes with original, but deep copy remains independent.  
Wrapped in function `check_copy_behavior()`.  

### 🔹 Problem 26 – Bank Account Manager (Global vs Local)
Global balance variable with deposit, withdraw, check.  
Demonstrates global keyword and local shadowing.  

### 🔹 Problem 27 – Polynomial Calculator (NumPy + Functions)
Takes two polynomials as NumPy arrays.  
Functions for addition, subtraction, multiplication (using `np.poly*`).  
Pretty print in polynomial form (e.g., `3x² + 2x + 1`).  

### 🔹 Problem 28 – Recursive Math Utility
Implements three recursive functions:  
- Factorial of a number  
- Nth Fibonacci term  
- Sum of digits of a number  
Handles negative inputs gracefully.  


### 🔹 Problem 29 – Prime & Fibonacci Analyzer with Lambda + FMR
- Generates first N Fibonacci numbers.  
- Uses **filter + lambda** to extract prime Fibonacci numbers.  
- Uses **map + lambda** to square all Fibonacci numbers.  
- Uses **reduce** to calculate sum of all Fibonacci numbers.  

### 🔹 Problem 30 – Student Grade System with Decorators
- Function `calculate_grade(marks)` returns grade.  
- Decorator `@logger` logs every function call (arguments + result).  
- Demonstrates decorator usage with student grade calculation.  


### 🔹 Problem 31 – Factorial Performance Comparison
- Two factorial implementations:  
  1. Recursive factorial  
  2. Lambda + reduce factorial  
- Uses `time` module to compare execution speed.  
- Runs performance test for N = 10, 50, 100.  


### 🔹 Problem 32 – Custom Pipeline using Map/Filter/Reduce
- Takes list of numbers.  
- Pipeline:  
  - **map** → double each number  
  - **filter** → keep only odd numbers  
  - **reduce** → product of remaining numbers  
- Implemented in reusable function `process_numbers(lst)`.  



