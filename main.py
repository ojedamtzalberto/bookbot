def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        words = file_contents.split()
        char_dict = generate_char_dict(file_contents)
        print_report(words, char_dict)

def generate_char_dict(file_contents):
    char_dict = {}

    for char in file_contents:
        key = char.lower()

        if key < 'a' or key > 'z':
            continue

        if key in char_dict:
            char_dict[key] = char_dict[key] + 1
        else:
            char_dict[key] = 1
    
    return char_dict

def print_report(words, char_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document\n")

    for char in char_dict:
        print(f"The '{char}' character was found {char_dict[char]} times")

main()