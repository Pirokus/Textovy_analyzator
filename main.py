import string


USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.''',
]


def end_program(message):
    print(message)
    raise SystemExit


def main():
    separator = "-" * 40

    username = input("username:").strip()
    password = input("password:").strip()

    if USERS.get(username) != password:
        end_program("unregistered user, terminating the program..")

    print(separator)
    print(f"Welcome to the app, {username}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print(separator)

    choice = input(
        f"Enter a number btw. 1 and {len(TEXTS)} to select: "
    ).strip()

    if not choice.isdigit():
        end_program("invalid input, terminating the program..")

    index = int(choice) - 1
    if index not in range(len(TEXTS)):
        end_program("invalid input, terminating the program..")

    words = TEXTS[index].split()
    cleaned = [
        word.strip(string.punctuation) for word in words
        if word.strip(string.punctuation)
    ]

    title_count = sum(word.istitle() for word in cleaned)
    upper_count = sum(word.isupper() for word in cleaned)
    lower_count = sum(word.islower() for word in cleaned)
    numeric_values = [word for word in cleaned if word.isdigit()]
    numeric_sum = sum(int(number) for number in numeric_values)

    print(separator)
    print(f"There are {len(cleaned)} words in the selected text.")
    print(f"There are {title_count} titlecase words.")
    print(f"There are {upper_count} uppercase words.")
    print(f"There are {lower_count} lowercase words.")
    print(f"There are {len(numeric_values)} numeric strings.")
    print(f"The sum of all the numbers {numeric_sum}")
    print(separator)
    print("LEN|  OCCURRENCES  |NR.")
    print(separator)

    lengths = {}
    for word in cleaned:
        lengths[len(word)] = lengths.get(len(word), 0) + 1

    for length in sorted(lengths):
        count = lengths[length]
        stars = "*" * count
        print(f"{length:>3}|{stars:<18}|{count}")


if __name__ == "__main__":
    main()
