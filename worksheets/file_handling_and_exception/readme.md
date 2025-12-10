# **Problem 1 — Simple File Reader**

**Scenario:**
A company publishes daily announcements in a text file named `announcement.txt`. Your task is to build a simple utility that reads and displays the announcement.

---

## **Task 1 — Basic Reader Function**

Write a function named `read_announcement()` that:

1. Opens the file `announcement.txt`
2. Reads its entire content
3. Prints the announcement to the screen

This version assumes the file exists.

---

## **Task 2 — Add Error Handling and User Input**

Modify the function so that:

1. It asks the user to enter the file name (e.g., `"announcement.txt"`).
2. It attempts to open and read the file.
3. If the file does not exist, it prints a clear, user-friendly error message instead of crashing.

Example message:

```
The file you entered was not found. Please check the name and try again.
```

---

**use these:**

* `open()`
* `read()`
* Exception handling (`try` / `except`)
* `FileNotFoundError`

---

# **Problem 2 — Line-by-Line Reader**

**Scenario:** A school stores student names in `students.csv`.

## **Task 1 — Open and Read Entire File**
Write a function `read_file()` that:
1. Opens students.csv
2. Reads the entire file using .read()
3. Prints the full content exactly as it appears

**use these:**

* open()
* .read()
* basic file operations

## **Task 2 — Read Only the First Line (Header)**
Write a function `read_header()` that:
1. Opens students.csv
2. Reads only the first line using .readline()
3. Prints the header

**use these:**

* .readline()
* file pointer starts at beginning

## **Task 3 — Read All Lines Into a List Using readlines()**
Write a function `load_lines()` that:
1. Opens students.csv
2. Use .readlines() to read all rows into a list
3. Prints:
    - the list
    - the number of lines loaded

**use these:**

* .readlines()
* list of lines
* counting items

## **Task 4 — Read File Line-by-Line Using a Loop**
Write a function `process_lines()` that:
1. Opens students.csv
2. Use a for loop directly on the file object:
3. Prints each line
**use these:**

* .readlines()
* list of lines
* counting items

## **Task 5 — Store All Student Names in a List**
Write a function `extract_names()` that:
1. Opens students.csv
2. Skips the header
3. Reads each remaining line
4. Extracts the student name (the second column)
5. Stores names in a list
6. Prints the final list
**use these:**
* splitting lines using .split(',')
* ignoring the header
* storing values in a list

## **Task 6 — Store Full Student Records as Tuples (No Dictionaries Yet)**
Write a function `load_students()` that:
1. Opens students.csv
2. Skips the header
3. For each line:
4. splits columns
    - splits columns
    - trims whitespace
    - stores row as a tuple:
5. Appends each tuple to a list
6. Prints the resulting list of tuples

**use these:**
* splitting lines using .split(',')
* ignoring the header
* storing values in a list
---

# **Problem 3 — Writing to a New File**

**Scenario:** A travel agency wants to generate a **package summary** file.

**Task:**
Write a function:

```python
def write_summary(package_name, price, days):
```

which writes the following to `summary.txt`:

```
Package: <package_name>
Price: <price>
Duration: <days> days
```

**Concepts:** write(), overwriting vs append.

---

# **Problem 4 — Append Log Entries**

**Scenario:** A clinic keeps a log of visitors in `visitors.log`.

**Task:**
Write a function:

```python
def log_visitor(name):
```

* Opens `visitors.log` in append mode
* Writes: `"<name> visited at <timestamp>"`
* One entry per line

**Concepts:** append mode, timestamps using `datetime`.

---

# **Problem 5 — Counting Words in a File**

**Scenario:** A journalist wants a tool to analyze text files.

**Task:**
Write a function `count_words(file_path)` that:

* Reads the file
* Splits by whitespace
* Returns the total number of words

**Concepts:** reading text, splitting, error handling.

---

# **Problem 6 — Copy File Content**

**Scenario:** A backup script should copy a file into another.

**Task:**
Implement:

```python
def copy_file(src, dest):
```

Rules:

* If src doesn’t exist, print an error
* Otherwise copy line by line

**Concepts:** reading & writing safely, loops.

---

# **Problem 7 — List All Files in a Folder**

**Scenario:** A photo app wants to scan a directory for images.

**Task:**
Write:

```python
def list_files(folder_path):
```

* Print all files and subfolders
* Count how many are `.jpg` or `.png`

**Concepts:** os.listdir(), path checking.

---

# **Problem 8 — Read CSV Without Using csv Module**

**Scenario:** A bank exports transactions as CSV.

Example file:

```
2025-01-12,Deposit,5000
2025-01-13,Withdrawal,200
2025-01-13,Deposit,1500
```

**Task:**
Write:

```python
def load_transactions(file_path):
```

* Open file
* Split each line by comma
* Convert amount to integer
* Return a list of `(date, type, amount)` tuples

**Concepts:** manual parsing, converting types.

---

# **Problem 9 — Safe File Writing Using With-Statement**

**Scenario:** A note-taking app saves draft notes.

**Task:**
Write:

```python
def save_note(title, content):
```

File name: `<title>.txt`.

Inside:

```
Title: <title>

<content>
```

Use `with open(...) as f:` style.

---

# **Problem 10 — Count Frequency of Each Line (No Dictionaries)**

**Scenario:** A server log may contain repeated error messages.

**Task:**
In `server.log`, count how many times each unique line appears.

Output file `error_summary.txt` example:

```
Error 404: 3 times
Database timeout: 2 times
Error 500: 1 time
```

**Restriction:**
No dictionaries.
Use lists of tuples such as:

```
[("Error 404", 3), ("Database timeout", 2), ...]
```

---

# **Problem 11 — Split a File into Multiple Files**

**Scenario:** A telecom company wants to split a large SMS archive into chunks of 100 lines.

**Task:**
Write:

```python
def split_file(file_path, lines_per_file):
```

Create:

```
sms_part1.txt
sms_part2.txt
sms_part3.txt
...
```

**Concepts:** loops, counters, dynamic file creation.

---

# **Problem 12 — Merge Multiple Files Into One**

**Scenario:** Departmental reports are stored as:

```
report_sales.txt
report_hr.txt
report_finance.txt
```

**Task:**
Write:

```python
def merge_reports(folder, output_file):
```

* Read all files beginning with `"report_"`
* Append to `output_file`

---

# **Problem 13 — JSON-Like Format Without JSON Module**

**Scenario:** A program exports data in a simplified JSON-like format:

```
name: John Doe
age: 29
active: true
```

**Task:**
Write a parser:

```python
def parse_simple_file(path):
```

Return values as tuples:

```
[("name", "John Doe"), ("age", "29"), ("active", "true")]
```

---

# **Problem 14 — Detect and Replace Words in a File**

**Scenario:** HR needs to anonymize files by removing employee names.

Example replace list:

```
"John" → "[NAME]"
"Laura" → "[NAME]"
```

**Task:**
Write:

```python
def anonymize(src, dest, words):
```

Where `words` is a list like: `["John", "Laura"]`.

Replace every occurrence and save output.

---

# **Problem 15 — Mini Project: Student Record Manager**

**Scenario:** A small private school keeps records in text files.

Each record line:

```
id;name;grade;section
```

### Tasks:

1. **Load records** into a list of tuples
2. **Search by grade**
3. **Search by section**
4. **Append new student record**
5. **Save all records back to file**

No dictionaries required.

---

