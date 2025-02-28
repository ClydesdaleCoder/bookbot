def get_book_text(path_to_file):
    with open(f"{path_to_file}") as f:
        file_contents = f.read()
    return file_contents    

def word_count(file_contents):
    words= file_contents.split()
    num_words = len(words)
    return num_words

def get_letter_count(file_contents) :
    char_count = {}
    letter = file_contents.lower()
    for char in letter:
        if char in char_count:
            char_count[char] += 1
        else:       
            char_count[char] = 1
    return char_count

def sort_count_by_char(char_count):
    chars_list = []
    for char,count in char_count.items():
        chars_list.append({char: count})

    def sort_on(dict_l) :
        return list(dict_l.values())[0]

    chars_list.sort(reverse=True, key=sort_on)  

    return chars_list

