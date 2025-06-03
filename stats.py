def get_num_words(text):
    return len(text.split())

def get_char_counts(text):
    characters = {}
    for character in text:
        if character.lower() in characters:
            characters[character.lower()] += 1
        else:
            characters[character.lower()] = 1
    return characters

def get_char_stats(characters):
    stats = []
    for character in characters:
        if character.isalpha():
            stats.append({"char": character, "num": characters[character]})
    stats.sort(key=lambda x: x["num"], reverse=True)
    return stats