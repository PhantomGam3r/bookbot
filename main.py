import sys
from stats import get_num_words, get_char_counts, get_char_stats

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_counts = get_char_counts(book_text)
    chars = get_char_stats(char_counts)
    print("--------- Character Count -------")
    for char in chars:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")
    

main()