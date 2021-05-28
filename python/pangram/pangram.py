import string

def is_pangram(sentence):
    only_lower_alphas = ''.join(filter(str.isalpha, sentence)).lower()
    is_panagram = len(set(only_lower_alphas)) == len(string.ascii_lowercase)
    return True if is_panagram else False