def log_plagiat_check(func):
    def wrapper(word1, word2):
        return f'Check \'{word1}\' vs \'{word2}\' -> {func(word1, word2)}'

    return wrapper


def is_plagiat(word1: str, word2: str) -> bool:
    word1 = word1.lower()
    word2 = word2.lower()

    if word1 == word2:
        return True

    letters1 = set(word1)
    letters2 = set(word2)

    return len(letters2 - letters1) <= 1


with open('words.txt') as f:
    lines = f.readlines()

    for line in lines:
        elems = line.replace('\n', '').split()

        decorated = log_plagiat_check(is_plagiat)

        print(decorated(elems[0], elems[1]))
