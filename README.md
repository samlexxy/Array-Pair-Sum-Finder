# Array Pair Sum Finder

## Overview
This is a simple Python program that Given an unsorted array A[]. The task is to print all unique pairs in the unsorted array with equal sum. 
It also includes tests to ensure the program works correctly.

---

## How It Works
1. The program takes an array of numbers as input.
2. It calculates the sum of all possible pairs in the array.
3. If multiple pairs have the same sum, it groups them together(sorted) and displays the results in a readable format.

---

## Example
### Input:
```python
arr = [6, 4, 12, 10, 22, 54, 32, 42, 21, 11]
```

### Output:
```
Results:
Pairs : ( 4, 12) ( 6, 10) have sum : 16
Pairs : ( 10, 22) ( 21, 11) have sum : 32
Pairs : ( 12, 21) ( 22, 11) have sum : 33
Pairs : ( 22, 21) ( 32, 11) have sum : 43
Pairs : ( 32, 21) ( 42, 11) have sum : 53
Pairs : ( 12, 42) ( 22, 32) have sum : 54
Pairs : ( 10, 54) ( 22, 42) have sum : 64
```

---

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/samlexxy/Array-Pair-Sum-Finder.git
   cd Array-Pair-Sum-Finder
   ```

2. **Run the program**:
   ```bash
   python main.py
   ```

3. **Run the tests**:
   ```bash
   python test_take_home.py
   ```
