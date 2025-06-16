# Text File Analysis Assessment

## Overview

Welcome! This assessment challenges you to build a simple text analysis tool in Python. You will complete a script that reads a text file, processes its contents, and calculates some basic statistics like word count, word frequency, and the longest word.

This will test your skills in:
- File I/O (reading files)
- Error handling (`try...except`)
- String manipulation (`lower`, `replace`, `split`)
- List processing and iteration
- Creating and using functions

---

## Files Provided

-   `assessment.py`: **This is the file you need to edit.** It contains function stubs with `TODO` comments guiding you on what to implement.
-   `sample_text.txt`: The default text file your program will analyze.
-   `test_assessment.py`: A unit test suite to check your work. **Do not modify this file.**
-   `reset_assessment.py`: A script to wipe your changes from `assessment.py` and start over.

---

## How to Complete the Assessment

1.  **Implement the Functions**: Open `assessment.py` and complete the code for each function marked with a `TODO`. Read the docstrings carefully to understand the requirements for each function.

2.  **Run the Program**: You can run your script from the terminal to see it in action. It will prompt you for a filename or use `sample_text.txt` by default.
    ```bash
    python assessment.py
    ```

3.  **Test Your Code**: Use the provided unit test file to check if your functions are correct. Run this command in your terminal:
    ```bash
    python -m unittest test_assessment.py
    ```
    The tests will tell you which parts are working and which still need fixing.

4.  **Reset (If Needed)**: If you want to start again from the beginning, run the reset script:
    ```bash
    python reset_assessment.py
    ```

---

## Function Requirements

You must implement the following functions in `assessment.py`:

-   `get_filename(user_input)`: Determines whether to use the user's filename or the default.
-   `read_text_file(filename)`: Reads a file and handles `FileNotFoundError`.
-   `clean_and_tokenize_text(text)`: Converts text into a clean list of lowercase words without punctuation.
-   `count_total_words(word_list)`: Returns the total number of words in a list.
-   `count_word_frequency(word_list, target_word)`: Counts how many times a specific word appears.
-   `find_longest_word(word_list)`: Finds and returns the longest word from a list.
-   `display_analysis_results(...)`: Prints the final results in a specific format.

Good luck!