
# **Exception Handling Problem Set**

## **Problem 1 — Handling Division Errors**

**Scenario:** A grading system divides total points by number of questions to compute the score per question.

**Task:**
Write a function `score_per_question(total_points, num_questions)` that:

1. Attempts to divide the two numbers.
2. Catches `ZeroDivisionError` if `num_questions` is 0 and prints:
   `"Error: number of questions cannot be zero."`
3. Prints the result if successful.

**Concepts:** `try`, `except ZeroDivisionError`, safe arithmetic.

---

## **Problem 2 — Catching Multiple Exceptions**

**Scenario:** A teacher enters scores manually into the system.

**Task:**
Write a function `convert_score(value)` that:

1. Converts the input to integer.
2. Catches:

   * `ValueError` → print `"Invalid score format. Enter numbers only."`
   * `TypeError` → print `"Unexpected input type."`
3. Returns the converted integer if valid.

**Concepts:** multiple `except` blocks, input validation.

---

## **Problem 3 — Safe File Reader**

**Scenario:** The school stores student emails in `emails.txt`.

**Task:**
Write a function `load_emails()` that:

1. Attempts to open the file.
2. Catches:

   * `FileNotFoundError` → print `"File not found. Please check the filename."`
   * `PermissionError` → print `"Cannot open file due to permission issues."`
3. If successful, reads and prints each email.

**Concepts:** file exceptions, multiple specific errors.

---

## **Problem 4 — Catch-All Handler**

**Scenario:** The school IT system processes unknown data formats sent from external systems.

**Task:**
Write a function `process_data(data)` that:

1. Tries to convert the data to an integer.
2. If any error occurs, catches it using a generic `except Exception:` block and prints `"Unexpected error occurred."`
3. Prints `"Processing complete"` regardless of success or failure.

**Concepts:** `Exception`, general-purpose catching.

---

## **Problem 5 — Using `finally`**

**Scenario:** The system logs student login attempts to a file.

**Task:**
Write a function `log_attempt(student_id)` that:

1. Attempts to write `student_id` to `log.txt`
2. If writing fails, catch the error and print `"Cannot write to log."`
3. Use `finally` to print `"Attempt logged (or tried)."`, regardless of outcome.

**Concepts:** `finally`, guaranteed code execution.

---

## **Problem 6 — Re-raising Exceptions**

**Scenario:** Data validation is done by a helper function, but the main system must also handle errors.

**Task:**
Write a function `validate_gpa(gpa)` that:

1. Converts `gpa` to float.
2. If conversion fails, print `"Invalid GPA format."` and **re-raise** the exception.
3. In the main block, catch any raised exception and print `"System halted due to invalid GPA."`

**Concepts:** `raise`, exception propagation.

---





