# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project! 


## Overview

Amaruhx-bookbot is a simple Python application that analyzes text files of books. It provides a word count and a character count for the given book file.

## Files

- `main.py`: The main script that runs the book analysis.
- `stats.py`: Contains functions for counting words and characters in the book text.
- `books/`: Directory containing sample book text files.

## Usage

To run the book analysis, use the following command:

```sh
python3 main.py <path_to_book>
```

Replace `<path_to_book>` with the path to the book text file you want to analyze.

## Example

```sh
python3 main.py books/frankenstein.txt
```

## `main.py` Explanation

The `main.py` script performs the following steps:

1. Imports necessary modules and functions from `stats.py`.
2. Defines a function `get_book_text(filepath)` to read the content of the book file.
3. Defines the `main()` function which:
   - Checks if the correct number of command-line arguments is provided.
   - Reads the book text from the specified file.
   - Counts the total number of words in the book text using the `count_words` function from `stats.py`.
   - Counts the occurrences of each character in the book text using the `count_characters` function from `stats.py`.
   - Sorts the characters by their count using the `sort_characters` function from `stats.py`.
   - Prints the analysis results, including the total word count and the character counts.

4. Executes the `main()` function if the script is run directly.

## Functions in `main.py`

- `get_book_text(filepath)`: Reads and returns the content of the book file.
- `main()`: The main function that orchestrates the book analysis.

## Sample Output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 78456 total words
--------- Character Count -------
a: 4567
b: 1234
c: 2345
...
```