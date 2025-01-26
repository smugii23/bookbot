def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    print(text)
    num_words = count_words(text)
    print(num_words)


def get_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)


main()