def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = count_words(text)
    num_chars = count_characters(text)
    sorted_char_list = sort_character_list(num_chars)
    print(sorted_char_list)
    print_report(book_path, text, num_words, sorted_char_list)


def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowercase_text = text.lower()
    char_count = {}
    for i in lowercase_text:
        char_count[i] = char_count.get(i, 0) + 1
    return char_count

def sort_character_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=lambda item: item["num"])
    return sorted_list


def print_report(book_path, text, num_words, sorted_char_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in document\n")
    for i in sorted_char_list:
        if i["char"].isalpha():
            print(f"The '{i["char"]}' character was found {i["num"]} times")
    print("--- End report ---")



main()