import sys 

from stats import count_words
from stats import count_character
from stats import sorting

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # use second argument
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    character_count = count_character(text)
    sorted_characters = sorting(character_count)
    for c, count in sorted_characters:
        if c.isalpha():
            print(f"{c}: {count}")

main()