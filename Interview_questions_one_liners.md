# Interview Questions — One Liners

## Table of Contents

- [Difference between / and //](#difference-between-and-)
- [Different ways of print](#different-ways-of-print)
- [List out all the keywords of python using a program](#list-out-all-the-keywords-of-python-using-a-program)
- [string and slicing](#string-and-slicing)
- [convert integer to hexa decimal](#convert-integer-to-hexa-decimal)
- [List out all the methods applicable for list ?](#list-out-all-the-methods-applicable-for-list-)
- [Difference between append and extend on lists](#difference-between-append-and-extend-on-lists)
- [difference between  == , is and =](#difference-between-is-and-)
- [What are *args and **kwargs?](#what-are-args-and-kwargs)
- [What is lambda?](#what-is-lambda)
- [filter](#filter)
- [reduce](#reduce)
- [List Comprehension , Dictionary Comprehension](#list-comprehension-dictionary-comprehension)
- [Exception handling](#exception-handling)
- [Difference between deep copy and shallow copy](#difference-between-deep-copy-and-shallow-copy)
- [What is a Generator?](#what-is-a-generator)
- [Decorator](#decorator)
- [Difference between break, continue, and pass](#difference-between-break-continue-and-pass)
- [Reverse a string.](#reverse-a-string)
- [convert a string or line to a list , each character, each word,  separated by delimiter](#convert-a-string-or-line-to-a-list-each-character-each-word-separated-by-delimiter)
- [package vs sub package vs module vs class vs method](#package-vs-sub-package-vs-module-vs-class-vs-method)
- [Check palindrome.](#check-palindrome)
- [Find factorial.](#find-factorial)
- [Fibonacci series.](#fibonacci-series)
- [Find duplicates in a list.](#find-duplicates-in-a-list)
- [Remove duplicates.](#remove-duplicates)
- [Count character frequency.](#count-character-frequency)
- [Find second largest number.](#find-second-largest-number)
- [Find missing number.](#find-missing-number)
- [Check if two strings are anagrams.](#check-if-two-strings-are-anagrams)
- [Merge two dictionaries.](#merge-two-dictionaries)
- [Sort a dictionary by value.](#sort-a-dictionary-by-value)
- [Count vowels.](#count-vowels)
- [Find the first non-repeating character.](#find-the-first-non-repeating-character)
- [Flatten a nested list.](#flatten-a-nested-list)
- [Find common elements in two lists.](#find-common-elements-in-two-lists)
- [Rotate a list.](#rotate-a-list)
- [Swap two numbers without a third variable.](#swap-two-numbers-without-a-third-variable)
- [Count words in a sentence.](#count-words-in-a-sentence)
- [How do you flatten a 2Dimnesional list aeg:](#how-do-you-flatten-a-2dimnesional-list-aeg)
- [3-sum problem in a list](#3-sum-problem-in-a-list)
- [nlp in AI and its python libraries](#nlp-and-its-modules)
---

## Difference between / and //

**Answer:**

```text
/ is float division
// is integer division
print(18/10)
1.8
print(18//10)
1
Integer division removes the decimal not rounds off.
```

[Back to Table of Contents](#table-of-contents)

## Different ways of print

**Answer:**

```text
print can take any number of arguments

print(1,2,3,'test')
1 2 3 test

with a delimiter , below sep is not a keyword
print("A", "B", "C", sep="-")
A-B-C

print("Hello")
print("world!")
print('test')
Hello
world!
test

print("Hello", end=";")
print("world!")
print('test')
Hello;world!
test

f strings
name = "Alice"
age = 30
print(f"{name} is {age} years old.")
Alice is 30 years old.

format

name = "Alice"
age = 30
print("{} is {} years old.".format(name, age))
```

[Back to Table of Contents](#table-of-contents)

## List out all the keywords of python using a program

**Answer:**

```text
import keyword

print(keyword.kwlist)
print(f"Total keywords: {len(keyword.kwlist)}")

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
Total keywords: 35

=== Code Execution Successful ===
```

[Back to Table of Contents](#table-of-contents)

## string and slicing

**Answer:**

```text
nm = "Ravikumar"
nm[::] same as nm
nn[::-1] reverse
nm[1:3] -> av
nm[:6:2] Rvk

methods for strings
print(dir(str))
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

=== Code Execution Successful ===

examples :

s = "Ravi, kumar"
s.upper()
s.find('a')
s.split()
s.split(',')
```

[Back to Table of Contents](#table-of-contents)

## convert integer to hexa decimal

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## List out all the methods applicable for list ?

**Answer:**

```text
print(dir(list))
is below some contains __ and some dont
__..__ are python in built methods
others are normal methods which develpers can use
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append',
'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

[Back to Table of Contents](#table-of-contents)

## Difference between append and extend on lists

**Answer:**

```text
append accepts both list and  any object. Extend accepts only  list.
l=[1,2]

l.append([3,4])
# [1,2,[3,4]]
print(l)

l.append(5)
[1, 2, [3, 4], 5]
print(l)

l=[1,2]
l.extend([3,4])
print(l)

l.extend(5)
# Error  int objct is not iterable
print(l)

List vs set vs tuple vs dictionary
create a table with below parameters
Ordered, indexed
mutable
duplicates allowed or not
format
```

[Back to Table of Contents](#table-of-contents)

## difference between  == , is and =

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## What are *args and **kwargs?

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## What is lambda?

**Answer:**

```text
Anonymous function.
square=lambda x:x*x

print(square(5))
```

[Back to Table of Contents](#table-of-contents)

## filter

**Answer:**

```text

syntax : filter(function, iterable)

example : filter(fnc_even,l1)
fnc_even logic should give true for even  input value, false for output value. 

filter keyword filters data in l1 by applying function fnc_even to list l1

filter returns filter object not list, we must convert it to list 

using lambda

numbers=[1,2,3,4]

result=list(filter(lambda x:x%2==0,numbers))
 do with a function also
```

[Back to Table of Contents](#table-of-contents)

## reduce

**Answer:**

```text
from functools import reduce

reduce(lambda x,y:x+y,[1,2,3,4])
```

[Back to Table of Contents](#table-of-contents)

## List Comprehension , Dictionary Comprehension

**Answer:**

```text
squares=[x*x for x in range(5)]
d={x:x*x for x in range(5)}
```

[Back to Table of Contents](#table-of-contents)

## Exception handling

**Answer:**


Exception handling in Python manages runtime errors gracefully using **try, except, else, and finally** blocks, preventing your program from crashing unexpectedly.
```text
try:
    # Code that might raise an exception
    file = open("data.txt", "r")
    value = int(file.readline())
except FileNotFoundError:
    # Runs ONLY if FileNotFoundError occurs
    print("Error: The specified file could not be found.")
except ValueError:
    # Runs ONLY if int conversion fails
    print("Error: Could not convert file content to an integer.")
else:
    # Runs ONLY if NO exceptions were raised in try
    print(f"Successfully read value: {value}")
finally:
    # ALWAYS runs, regardless of whether an exception occurred
    print("Execution complete. Cleaning up resources...")
    try:
        file.close()
    except NameError:
        pass

Catch Specific Exceptions: Always catch specific error types (ValueError, KeyError, TypeError) instead of a bare except: block. A broad except: catches unintended errors (like KeyboardInterrupt or SystemExit) and hides bugs.
```

**Catching Multiple Exceptions**  Catch multiple error types in one block by passing them as a tuple:
```text
except (ValueError, TypeError) as error:
    print(f"Invalid input: {error}")
```
**Raise exception**
```text
if age < 0:
    raise ValueError("Age cannot be a negative number.")
```
**custom exception**
```text
class InsufficientFundsError(Exception):
    """Raised when account balance is lower than withdrawal amount."""
    pass


class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance

    def withdraw(self, amount: float):
        if amount > self.balance:
            # Raise the custom exception with a descriptive error message
            raise InsufficientFundsError(
                f"Cannot withdraw ${amount:.2f}. Available balance: ${self.balance:.2f}"
            )
        
        self.balance -= amount
        print(f"Successfully withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")


Demonstration & Exception Handling
account = BankAccount(balance=100.00)

try:
    account.withdraw(150.00)  # This will trigger the exception
except InsufficientFundsError as e:
    print(f"Transaction Failed -> {e}")
```

Common Python Built-in Exceptions

| Exception                         | Exception Category | Primary Cause                                                                     | Example Trigger                                   |
| :-------------------------------- | :----------------- | :-------------------------------------------------------------------------------- | :------------------------------------------------ |
| **`SyntaxError`**         | Parser             | Invalid Python syntax that cannot be parsed.                                      | `if True` (missing colon)                       |
| **`IndentationError`**    | Parser             | Incorrect or inconsistent indentation.                                            | Mixing spaces and tabs or wrong spacing.          |
| **`NameError`**           | Scope              | Accessing a variable or function name before it is defined.                       | `print(x)` when `x` isn't assigned            |
| **`TypeError`**           | Type/Operation     | Applying an operation or function to an object of an inappropriate type.          | `"hello" + 5`                                   |
| **`ValueError`**          | Data/Arguments     | A function receives an argument with the right type but an invalid value.         | `int("abc")`                                    |
| **`AttributeError`**      | Object Access      | Attempting to access an attribute or method that an object doesn't possess.       | `"string".append("x")`                          |
| **`IndexError`**          | Sequence           | Attempting to access a list, tuple, or sequence with an out-of-bounds index.      | `lst = [1, 2]; lst[5]`                          |
| **`KeyError`**            | Mapping            | Attempting to access a dictionary key that does not exist.                        | `d = {"a": 1}; d["b"]`                          |
| **`ZeroDivisionError`**   | Arithmetic         | Attempting to divide or modulo a number by zero.                                  | `10 / 0`                                        |
| **`OverflowError`**       | Arithmetic         | Calculation result exceeds the maximum limit for a numeric type.                  | `math.exp(1000)`                                |
| **`FileNotFoundError`**   | I/O & OS           | Attempting to access or open a file path that does not exist on disk.             | `open("missing.txt", "r")`                      |
| **`PermissionError`**     | I/O & OS           | Attempting an OS action without adequate permissions.                             | Writing to a read-only or restricted system file. |
| **`FileExistsError`**     | I/O & OS           | Attempting to create a directory or file that already exists.                     | `os.mkdir("existing_folder")`                   |
| **`ImportError`**         | System             | Module or package import fails.                                                   | `import nonexistent_module`                     |
| **`ModuleNotFoundError`** | System             | Subclass of`ImportError`; raised when a module cannot be found in `sys.path`. | `import missing_lib`                            |
| **`StopIteration`**       | Iteration          | Signal raised by`next()` to indicate an iterator has no further items.          | `next(iter([]))`                                |
| **`RecursionError`**      | Runtime            | Maximum recursion depth exceeded (e.g., infinite recursion).                      | `def f(): f(); f()`                             |
| **`KeyboardInterrupt`**   | User Input         | User interrupts program execution (typically by pressing`Ctrl+C`).              | Pressing`Ctrl+C` in terminal                    |
| **`MemoryError`**         | Resource           | System runs out of RAM during an operation.                                       | Creating an impossibly massive list in RAM        |

```text

BaseException
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    └── ZeroDivisionError
      │    └── OverflowError
      ├── AttributeException -> AttributeError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── OSError
      │    ├── FileNotFoundError
      │    ├── PermissionError
      │    └── FileExistsError
      ├── TypeError
      └── ValueError

```

[Back to Table of Contents](#table-of-contents)

## Difference between deep copy and shallow copy

**Answer:**

```text
Shallow copy copies references for nested objects.

Deep copy creates completely independent copies.

import copy

a=[[1,2],[3,4]]

b=copy.copy(a)

c=copy.deepcopy(a)
```

[Back to Table of Contents](#table-of-contents)

## What is a Generator?

**Answer:**

```text
Uses yield.

def gen():
    for i in range(5):
        yield i

Benefit : Memory efficient, used in reading very large files in chunks
```

[Back to Table of Contents](#table-of-contents)

## Decorator

**Answer:**

```text
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling function")
        result = func(*args, **kwargs)
        print("After calling function")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")

Before calling function
Hello, Alice!
After calling function
```

[Back to Table of Contents](#table-of-contents)

## Difference between break, continue, and pass

**Answer:**

```text
break: Exit loop.
continue: Skip current iteration.
pass: Do nothing.
```

[Back to Table of Contents](#table-of-contents)

## Reverse a string.

**Answer:**

```text
l = "ravi"
print(l[::-1])
ivar

Reverse a list.
l = [ 1,2,3]
print(l[::-1])
[3, 2, 1]
```

[Back to Table of Contents](#table-of-contents)

## convert a string or line to a list , each character, each word,  separated by delimiter

**Answer:**

```text
by character
s = "Python"
result = list(s)

print(result)

['P', 'y', 't', 'h', 'o', 'n']

by word or space delimiter
s = "I love Python"
result = s.split()

print(result)

['I', 'love', 'Python']

by a specific delimiter
s = "apple,banana,orange"
result = s.split(",")

print(result)

['apple', 'banana', 'orange']
```

[Back to Table of Contents](#table-of-contents)

## package vs sub package vs module vs class vs method

**Answer:**

```text
method is a function, reused by calling it.generally it lies inside class but not mandatory.

class contains set of functions,  variables.
example :

module is a single Python file saved as module_name.py it can contain set of classes , functions..
example : math , random,

package is a folder contains set of modules or .py scripts in it
exampe : pyspark , numpy , pandas


sub packages are folders inside another folder or package


from pyspark.sql import SparkSession
here pyspark is pkg
sql is subpackage
session is a module (session.py)
Sparksession is a class.
SparkSession class is reexported in sql subpackage __init__.py file
so
from pyspark.sql.session import SparkSession
and
from pyspark.sql import SparkSession
both points to same class
```

[Back to Table of Contents](#table-of-contents)

## Check palindrome.

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## Find factorial.

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## Fibonacci series.

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## Find duplicates in a list.

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## Remove duplicates.

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## Count character frequency.

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## Find second largest number.

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## Find missing number.

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## Check if two strings are anagrams.

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## Merge two dictionaries.

**Answer:**

```text
# pipe method
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 20, "c": 3}

merged = dict1 | dict2

print(merged)

# update method
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 20, "c": 3}

dict1.update(dict2)

print(dict1)

# Dictionary unmask (**) method

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 20, "c": 3}

merged = {**dict1, **dict2}

print(merged)

{'a': 1, 'b': 20, 'c': 3}
{'a': 1, 'b': 20, 'c': 3}
{'a': 1, 'b': 20, 'c': 3}

=== Code Execution Successful ===
```

[Back to Table of Contents](#table-of-contents)

## Sort a dictionary by value.

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## Count vowels.

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## Find the first non-repeating character.

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## Flatten a nested list.

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## Find common elements in two lists.

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## Rotate a list.

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## Swap two numbers without a third variable.

**Answer:**

_No answer provided._

[Back to Table of Contents](#table-of-contents)

## Count words in a sentence.

**Answer:**

```text
sntc = "Ravi kumar goud is  me"
print(len(sntc.split(" ")))
#gives 6 becuase there is a double space

sntc = "Ravi kumar goud is  me"
l = sntc.strip().split(" ")
count = 0
for i in l:
    if i != "":
        count += 1
print(count)
```

[Back to Table of Contents](#table-of-contents)

## How do you flatten a 2Dimnesional list aeg:

**Answer:**

```text
nested = [[1, 2], [3, 4], [5, 6]]

flat = [item for sublist in nested for item in sublist]

print(flat)
[1, 2, 3, 4, 5, 6]

nested = [[1, 2], [3, 4], [5, 6]]
new_list = []
for i in nested:
    for j in i:
        new_list.append(j)
print(new_list)  # Output: [1, 2, 3, 4, 5, 6]
```

[Back to Table of Contents](#table-of-contents)

## 3-sum problem in a list

**Answer:**

```text
Python code: Given a list something [-2, 0, 1, 1, -1] write a program that gives unique number such as a + b + c = 0, where a, b, and c are numbers from the above list."
This is a variation of the 3-sum problem, where you find all unique triplets in the list that sum up to zero.

Here’s a Python solution:

def three_sum(nums):
    nums.sort()
    result = set()
    n = len(nums)

    for i in range(n):
        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return list(result)

# Example usage
nums = [-2, 0, 1, 1, -1]
triplets = three_sum(nums)
print("Unique triplets with sum 0:", triplets)

Output:

Unique triplets with sum 0: [(-2, 1, 1), (-1, 0, 1)]

Explanation:

It sorts the list to handle duplicates efficiently.

Uses a 2-pointer technique to find combinations that sum to 0.

The result is stored as a set to avoid duplicate triplets.
```

[Back to Table of Contents](#table-of-contents)

## NLP and its modules

**Answer:**

https://chatgpt.com/share/6ab24692-a0d0-83e8-a384-fe648dbb072b

[Back to Table of Contents](#table-of-contents)
