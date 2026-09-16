+ [Read a large log file, without memory issues and find errors ](#read-a-large-log-file-without-memory-issues-and-find-errors)
+ [String parsing and Data cleansing and data extraction from a log ](#string-parsing-and-data-cleansing-and-data-extraction-from-a-log)

## Read a large log file, without memory issues and find errors
Write a generator function read_large_file(file_path, chunk_size=100) that streams a large file line-by-line, yielding a list (chunk) of lines of size chunk_size at a time. Demonstrate how you would iterate through this generator to process data without overloading RAM, and extract errors

[Read a large log file, without memory issues and find errors](https://github.com/ravigitrepo123/python-learning/blob/main/practical_questions/scripts/read_large_file_memry_eff.py)


## String parsing and Data cleansing and data extraction from a log
Question 1: String Parsing & Data Cleaning (Foundational)\
You receive raw, messy server log strings in this format:\
log_line = **"2026-09-14 10:15:30 [INFO] UserID:10294 Action:PURCHASE Amount:250.50"**\
Task: Write a Python function parse_log(log_line) that extracts and returns a dictionary containing:\
timestamp (as string)\
user_id (as integer)\
action (as string)\
amount (as float)\
[String_Parsing_and_Data_Cleaning.py](https://github.com/ravigitrepo123/python-learning/blob/main/practical_questions/scripts/String_Parsing_and_Data_Cleaning.py)
