from stats import get_book_text,word_count,get_letter_count

def main(): 
    file_contents = get_book_text("books/frankenstein.txt")
    num_words = word_count(file_contents)
    print(f"{num_words} words found in the document")
    letter_count = get_letter_count(file_contents) 
    print(letter_count) 

main()

