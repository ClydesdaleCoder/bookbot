from stats import get_book_text,word_count,get_letter_count,sort_count_by_char
import sys
argument= sys.argv
path=sys.argv[1]
def main(): 
    if len(argument)  != 2:
        print("Usage: python3 main.py <path_to_book> ")
        sys.exit(1)
    else:

        file_contents = get_book_text(path)
        num_words = word_count(file_contents)
        letter_count = get_letter_count(file_contents) 
        sorted_count = sort_count_by_char(letter_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path} ")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in sorted_count: 
            char = list(item.keys())[0]
            count = item[char]
            if not char.isalpha():
                continue 
            print(f"{char}:{count}")

        print("============= END ===============")
            
main()

