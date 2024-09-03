def is_plagiat(word1: str, word2: str) -> bool:
    word1 = word1.lower()
    word2 = word2.lower()

    if word1 == word2:
        return True

    letters1 = set(word1)
    letters2 = set(word2)

    return len(letters2 - letters1) <= 1


in1 = input()
in2 = input()

print(is_plagiat(in1, in2))
