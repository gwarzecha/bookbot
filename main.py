def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words in the book")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"the '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_chars_dict(text):
    chars = {}
    for c in text:
        lower_case = c.lower()
        if lower_case in chars:
            chars[lower_case] += 1
        else:
            chars[lower_case] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

main()
