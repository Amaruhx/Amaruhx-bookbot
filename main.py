import sys
from stats import *

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    sorted_characters = sort_characters(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in sorted_characters:
        print(f"{char}: {count}")

if __name__ == "__main__":
    main()

