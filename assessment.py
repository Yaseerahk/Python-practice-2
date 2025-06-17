
# A predefined list of common words to ignore in some analyses.
COMMON_WORDS = ["the", "a", "is", "in", "of", "to", "and", "be", "that", "it"]

def get_filename(user_input: str or None) -> str:
    """
    TODO: Step 1 - Handle filename selection.
    
    This function should:
    - Return the user_input if it's a non-empty string.
    - Return 'sample_text.txt' as the default if user_input is empty or None.
    
    Args:
        user_input (str or None): The filename provided by the user.
        
    Returns:
        str: The effective filename to use.
    """
    return user_input.strip() if user_input else 'sample_text.txt'
    pass


def read_text_file(filename: str) -> str:
    """
    TODO: Step 2 - Read the content of a file.
    
    This function should:
    - Open and read the entire content of the specified file.
    - Return the file's content as a single string.
    - Handle a FileNotFoundError by printing an error message "Error: File not found."
      and returning an empty string.
      
    Args:
        filename (str): The name of the file to read.
        
    Returns:
        str: The content of the file, or an empty string if an error occurs.
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
    return ""
    pass


def clean_and_tokenize_text(text: str) -> list[str]:
    """
    TODO: Step 3 - Process the raw text into a list of words.
    
    This function should:
    1. Convert the entire text to lowercase.
    2. Remove all punctuation (e.g., '.', ',', '!', '?').
       Hint: You can use `string.punctuation`.
    3. Split the text into a list of individual words.
    
    Args:
        text (str): The raw string content from the file.
        
    Returns:
        list[str]: A list of cleaned, lowercase words.
        
    Example:
        clean_and_tokenize_text("Hello, World!") should return ['hello', 'world']
    """
    import string 
    text=text.lower
    text=text.translate(str.maketrans('','',string.punctuation))
    return text.split

    pass


def count_total_words(word_list: list[str]) -> int:
    """
    TODO: Step 4 - Count the total number of words.
    
    This function should:
    - Take a list of words.
    - Return the total number of items in the list.
    
    Args:
        word_list (list[str]): A list of words.
        
    Returns:
        int: The total count of words in the list.
    """
    return len(word_list)
    pass


def count_word_frequency(word_list: list[str], target_word: str) -> int:
    """
    TODO: Step 5 - Count the frequency of a specific word.
    
    This function should:
    - Count how many times `target_word` (case-insensitive) appears in `word_list`.
    
    Args:
        word_list (list[str]): A list of words (assumed to be lowercase).
        target_word (str): The word to count the frequency of.
        
    Returns:
        int: The number of times the target word appears.
    """
    return word_list.count(target_word.lower())
    pass


def find_longest_word(word_list: list[str]) -> str:
    """
    TODO: Step 6 - Find the longest word in the text.
    
    This function should:
    - Iterate through the `word_list`.
    - Find and return the longest word.
    - If there's a tie in length, return the first one found.
    - If the list is empty, return an empty string.
    
    Args:
        word_list (list[str]): A list of words.
        
    Returns:
        str: The longest word found in the list.
    """
    if not word_list:
        return " "
    return max(word_list,key=len)
    pass


def display_analysis_results(total_words: int, frequency: int, longest_word: str, target_word: str)-> None:
    """
    TODO: Step 7 - Display the final analysis in a formatted way.
    
    This function should print the results exactly as follows:
    
    --- Text Analysis Results ---
    Total words: [total_words]
    Longest word: '[longest_word]'
    Frequency of the word '[target_word]': [frequency]
    
    Args:
        total_words (int): The total word count.
        frequency (int): The frequency of the target word.
        longest_word (str): The longest word found.
        target_word (str): The word whose frequency was counted.
    """
    print("--- Text Analysis Results ---")
    print(f"Total words: {total_words}")
    print(f"Longest word: '{longest_word}'")
    print(f"Frequency of the word '{target_word}': {frequency}")
    pass


if __name__ == "__main__":
    """
    This main block orchestrates the analysis. Please leave this as is.
    """
    # Step 1: Get filename
    user_filename = input("Enter filename to analyze [default: sample_text.txt]: ")
    filename = get_filename(user_filename)
    print(f"Analyzing file: {filename}\n")

    # Step 2: Read file
    file_content = read_text_file(filename)

    if file_content:
        # Step 3: Clean and tokenize
        words = clean_and_tokenize_text(file_content)

        # Step 4: Calculate total words
        total = count_total_words(words)
        
        # Step 5: Count frequency of a specific word
        word_to_find = "programming"
        freq = count_word_frequency(words, word_to_find)

        # Step 6: Find the longest word
        longest = find_longest_word(words)

        # Step 7: Display results
        display_analysis_results(total, freq, longest, word_to_find)
