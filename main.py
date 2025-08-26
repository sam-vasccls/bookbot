import sys
from stats import get_words, count_char

def get_book_text(filepath):
    # num_words = 0
    # chars = None
    with open(filepath) as file:
        file_contents = file.read()
        file_name = filepath[6:]
        num_words = get_words(file_contents)
        chars = count_char(file_contents)

    print(f"============ BOOKBOT ============\nAnalyzing book found at books/{file_name}...\n----------- Word Count ----------")
    print(f"Found {num_words} total words\n--------- Character Count -------")
    for data in chars:
        print(f"{data}: {chars[data]}")

    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        get_book_text(sys.argv[1])

main()