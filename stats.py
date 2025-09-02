def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    lowercase_text = text.lower()
    char_count = {}
    for c in lowercase_text :
        if c in char_count :
            char_count[c] += 1
        else :
            char_count[c] = 1

    return char_count

def sort_char_count(char_count):
    char_list = [{"char": key, "num": value} for key, value in char_count.items()]
    alpha_list = [item for item in char_list if item["char"].isalpha()]
    alpha_list.sort(reverse=True, key=lambda item: item["num"])

    return alpha_list


