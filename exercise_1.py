def count_letters(word):
    letter_count = {}

    for char in word:
        char_lower = char.lower()
        if char_lower.isalpha():
            if char_lower in letter_count:
                letter_count[char_lower] += 1
            else:
                letter_count[char_lower] = 1

    return letter_count


word = "Hello World"
print(count_letters(word))
