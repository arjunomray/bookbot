
def count_words(content):
    words = content.split()
    num_words = len(words)
    return num_words

def get_text(path):
    with open(path) as f:
        return f.read()

def get_letter_count(string):
    lower_string = string.lower()

    letter_collection = {}

    for i in lower_string:
        if i in letter_collection.keys():
            letter_collection[i] += 1
        else:
            letter_collection[i] = 1

    return letter_collection

def book_report(book_path):
    content = get_text(book_path)
    print(f"--- Begin book report of {book_path}\n\n")
    print(f"{count_words(content)} words found in document.\n\n")
    letter_dict = get_letter_count(content)
    
    for key, value in letter_dict.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times.")

def main():
    book_report("books/frankenstein.txt")




if __name__ == "__main__":
    main()