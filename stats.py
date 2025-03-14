
def count_words(book_text):
    words = book_text.split()
    return len(words)

"""
TODO: takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
Each dictionary should have two key-value pairs: one for the character and one for the count.
Sort from greatest to least by the count.
The .sort() method will be helpful here (see the hint).
"""

def sort_characters(characters):
    sorted_characters = sorted(characters.items(), key=lambda x: x[1], reverse=True)
    return sorted_characters
    
def count_characters(book_text):
    book_text = book_text.lower()
    characters = {}
    for char in book_text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters