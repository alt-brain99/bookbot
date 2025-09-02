import sys
from stats import get_num_words
from stats import get_char_count
from stats import sort_char_count

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    text = get_book_text(path)
    num_count = get_num_words(text)
    char_count = get_char_count(text)
    sorted_char_list = sort_char_count(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_list :
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
