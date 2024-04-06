def sort_on(dict):
    return dict["num"]

def sort_list(list):
    list.sort(reverse=True,key=sort_on)
    return list

def dict_to_list(dict):
    char_list = []
    for char,num in dict.items():
        char_dict = {"char": char, "num": num}
        char_list.append(char_dict)
    sort_list(char_list)
    return char_list

def count_letters(file_contents):
    leters_dict = {}
    lowered_file_contents = file_contents.lower()
    for letter in lowered_file_contents:
        if letter.isalpha():
            if letter in leters_dict:
                leters_dict[letter] += 1
            else:
                leters_dict[letter] = 1
    return leters_dict

def count_words(file_contents):
    words_list = file_contents.split()
    count = 0
    for word in words_list:
        count += 1
    return count

def book_report_start():
    print("--- Begin report of books/frankenstein.txt")



def main():
    book_report_start()
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() 
    word_count = count_words(file_contents) 
    print(f"{word_count} words found in the document.")
    letters_dict = count_letters(file_contents)
    letters_list = dict_to_list(letters_dict)
    for letter in letters_list:
        print(f"The '{letter['char']}' character was found {letter['num']} times.")
    print("--- End report ---")


main()


