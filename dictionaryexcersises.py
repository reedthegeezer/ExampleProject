DICTIONARY = {
    "apple": "A shiny red round fruit.",
    "banana": "A yellow, boomerang-shaped fruit.",
    "orange": "A round orange citrus fruit.",
    "grape": "A small juicy fruit that grows in bunches.",
    "watermelon": "A large green fruit with red juicy flesh inside.",
    "kiwi": "A small brown fruit with green flesh inside.",
    "mango": "A sweet tropical fruit with orange flesh.",
    "strawberry": "A small red fruit with tiny seeds on the outside."
}


def get_word_from_user():
    return input("Enter a word (or type 'list', 'mostcommon', or 'quit'): ").lower()


def print_definition(word):
    if word == "list":
        print("Available words:")
        for key in DICTIONARY:
            print("-", key)
    elif word in DICTIONARY:
        print(f"The definition of '{word}' is:")
        print(DICTIONARY[word])
    else:
        print("Sorry, I don't know that word.")


def count_word_occurrences(history):
    word_occurrences = {}

    for word in history:
        if word not in word_occurrences:
            word_occurrences[word] = 1
        else:
            word_occurrences[word] += 1

    return word_occurrences


def print_most_common_word(word_occurrences):
    most_common_word = ""
    highest_count = 0

    for word, count in word_occurrences.items():
        if count > highest_count:
            highest_count = count
            most_common_word = word

    if most_common_word:
        print(f"The most commonly entered word is '{most_common_word}'.")
        print(f"It was entered {highest_count} times.")
    else:
        print("No words have been entered yet.")


def main():
    print("Welcome to the Mini Dictionary!")

    history = []

    while True:
        word = get_word_from_user()

        if word == "quit":
            print("Goodbye!")
            break

        if word == "mostcommon":
            occurrences = count_word_occurrences(history)
            print_most_common_word(occurrences)
            continue

        history.append(word)
        print_definition(word)


if __name__ == "__main__":
    main()