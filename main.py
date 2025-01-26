def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = count_words(text)
    num_chars = count_characters(text)
    print_report(text, num_words, num_chars)


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

def print_report(text, num_words, num_chars):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in document\n")
    for i in num_chars:
        if i.isalpha():
            print(f"The '{i}' character was found {num_chars[i]} times")
    print("--- End report ---")



main()