import unittest
import os
import io
import sys
from assessment import (
    get_filename,
    read_text_file,
    clean_and_tokenize_text,
    count_total_words,
    count_word_frequency,
    find_longest_word,
    display_analysis_results
)

class TestTextAnalyzer(unittest.TestCase):

    # --- Test file setup ---
    def setUp(self):
        # Create a dummy test file
        self.test_filename = "test_file.txt"
        with open(self.test_filename, "w") as f:
            f.write("This is a test. Simple, right?")

        # Redirect stdout to capture print statements
        self.held_stdout = sys.stdout
        sys.stdout = self.captured_output = io.StringIO()

    def tearDown(self):
        # Remove the dummy file
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

        # Restore stdout
        sys.stdout = self.held_stdout

    # --- Unit Tests ---
    def test_get_filename(self):
        self.assertEqual(get_filename("my_file.txt"), "my_file.txt")
        self.assertEqual(get_filename(""), "sample_text.txt")
        self.assertEqual(get_filename(None), "sample_text.txt")

    def test_read_text_file_success(self):
        content = read_text_file(self.test_filename)
        self.assertEqual(content, "This is a test. Simple, right?")

    def test_read_text_file_not_found(self):
        content = read_text_file("non_existent_file.txt")
        self.assertEqual(content, "")
        output = self.captured_output.getvalue().strip()
        self.assertEqual(output, "Error: File not found.")

    def test_clean_and_tokenize_text(self):
        text = "Hello, World! This is A TEST."
        expected = ["hello", "world", "this", "is", "a", "test"]
        self.assertEqual(clean_and_tokenize_text(text), expected)

    def test_count_total_words(self):
        words = ["this", "is", "a", "list", "of", "words"]
        self.assertEqual(count_total_words(words), 6)
        self.assertEqual(count_total_words([]), 0)

    def test_count_word_frequency(self):
        words = ["apple", "banana", "apple", "cherry", "apple"]
        self.assertEqual(count_word_frequency(words, "apple"), 3)
        self.assertEqual(count_word_frequency(words, "cherry"), 1)
        self.assertEqual(count_word_frequency(words, "grape"), 0)

    def test_find_longest_word(self):
        words = ["short", "longer", "longest", "tiny"]
        self.assertEqual(find_longest_word(words), "longest")
        words_tie = ["one", "two", "three", "four"] # 'three' is longest
        self.assertEqual(find_longest_word(words_tie), "three")
        self.assertEqual(find_longest_word([]), "")

    def test_display_analysis_results(self):
        display_analysis_results(150, 5, "programming", "python")
        output = self.captured_output.getvalue()
        expected = (
            "--- Text Analysis Results ---\n"
            "Total words: 150\n"
            "Longest word: 'programming'\n"
            "Frequency of the word 'python': 5\n"
        )
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)