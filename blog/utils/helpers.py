def sub_words(text:str, length):
    words = text.split(" ")
    if length > len(words): return text
    return " ".join(words[0:length])

