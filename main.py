def count_letters(file_contents):
    character_dict = {}
    lowered_file_contents = file_contents.lower()
    for character in lowered_file_contents:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    print(character_dict)
    return None

    pass

def count_words(file_contents):
    words_list = file_contents.split()
    count = 0
    for word in words_list:
        count += 1
    print(count)
    return None


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()  
    count_words(file_contents)
    count_letters(file_contents)


main()


