def get_words(text):
    num_words = len(text.split())
    return num_words

def count_char(text):
    chars = {}
    for char in text:
        if char.lower() in chars:
            chars[f"{char.lower()}"] += 1
        else:
            chars[f"{char.lower()}"] = 1
    return chars