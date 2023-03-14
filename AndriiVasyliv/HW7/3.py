def count_characters(string):
    character_counts = {}

    for char in string:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    return character_counts

print(count_characters("HELLO"))