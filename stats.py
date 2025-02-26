def get_book_text(path_to_file):
    with open(f"{path_to_file}") as f:
        file_contents = f.read()
    return file_contents    

def word_count(file_contents):
    words= file_contents.split()
    num_words = len(words)
    return num_words

def get_letter_count(file_contents) :
    count = {}
    letter = file_contents.lower()
    for char in letter:
        if char in count:
            count[char] += 1
        else:       
            count[char] = 1
    return count

