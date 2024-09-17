import string


def alphabet_position(text):
    alphabet = string.ascii_lowercase

    return " ".join([str(alphabet.index(c.lower())+1) for c in text if c.lower() in alphabet])
